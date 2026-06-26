---
source_file: /Users/bearj/coding_projects/netmaster/.opencode/plans/web-terminal-plan.md
ingested: 2026-06-01
sha256: 7370b6cc67af
category: project
original_title: Web Terminal Plan
---

# Web Terminal Plan

## Files to Create/Modify

1. **NEW** `src/protocols/web_terminal.py` — Interactive SSH/Telnet session manager
2. **MODIFY** `src/ui/app.py` — Add SocketIO terminal events
3. **MODIFY** `src/ui/templates/dashboard.html` — Add xterm.js terminal panel

---

## 1. `src/protocols/web_terminal.py`

### Classes:

- **SSHSession**: Wraps paramiko `invoke_shell()`, background thread reads channel → callback
- **TelnetSession**: Wraps raw socket with telnet negotiation, background thread reads socket → callback
- **WebTerminalManager**: Registry of sessions, factory methods, I/O dispatch

### Key implementation details:
- SSH: `paramiko.SSHClient().invoke_shell(term='xterm-256color')` for PTY
- Telnet: raw socket with IAC/DONT/DO/WONT/WILL negotiation stripping
- Each session runs a daemon thread reading from the transport
- Output pushed via `on_output(session_id, data)` callback
- Disconnect pushed via `on_disconnect(session_id)` callback

### Code:

```python
"""
Web-based Interactive Terminal Manager
SSH/Telnet interactive sessions bridged to WebSocket
"""
import time
import socket
import logging
import threading

logger = logging.getLogger("netmaster.protocols.terminal")


# ─── Telnet Protocol ──────────────────────────────

IAC = bytes([255])
DONT = bytes([254])
DO = bytes([253])
WONT = bytes([252])
WILL = bytes([251])
SB = bytes([250])
SE = bytes([240])


def _negotiate_telnet(data: bytes) -> bytes:
    result = bytearray()
    i = 0
    while i < len(data):
        if data[i] == 255 and i + 2 < len(data):
            cmd = data[i + 1]
            opt = data[i + 2]
            if cmd in (WILL, WONT, DO, DONT):
                i += 3
                continue
            elif cmd == SB:
                i += 3
                while i < len(data):
                    if data[i] == 255 and i + 1 < len(data) and data[i + 1] == SE:
                        i += 2
                        break
                    i += 1
                continue
        result.append(data[i])
        i += 1
    return bytes(result)


# ─── SSH Session ──────────────────────────────────

class SSHSession:
    def __init__(self, session_id, host, port, username, password=None, key_file=None):
        self.session_id = session_id
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.key_file = key_file
        self.client = None
        self.channel = None
        self.running = False
        self.thread = None
        self.on_output = None
        self.on_disconnect = None

    def connect(self):
        import paramiko
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        kwargs = {
            "hostname": self.host, "port": self.port,
            "username": self.username, "timeout": 10,
            "allow_agent": False, "look_for_keys": False,
        }
        if self.key_file:
            kwargs["key_filename"] = self.key_file
        elif self.password:
            kwargs["password"] = self.password
        else:
            kwargs["allow_agent"] = True
            kwargs["look_for_keys"] = True
        self.client.connect(**kwargs)
        self.channel = self.client.invoke_shell(term="xterm-256color")
        self.channel.settimeout(0.0)
        self.running = True
        self.thread = threading.Thread(target=self._read_loop, daemon=True)
        self.thread.start()

    def _read_loop(self):
        while self.running:
            try:
                if self.channel.recv_ready():
                    data = self.channel.recv(65535)
                    if data:
                        if self.on_output:
                            self.on_output(self.session_id, data)
                    else:
                        break
                else:
                    time.sleep(0.005)
            except Exception:
                break
        self._cleanup()

    def write(self, data: bytes):
        if self.channel and self.running:
            try:
                self.channel.send(data)
            except Exception:
                self._cleanup()

    def resize(self, cols: int, rows: int):
        if self.channel and self.running:
            try:
                self.channel.resize_pty(width=cols, height=rows)
            except Exception:
                pass

    def _cleanup(self):
        self.running = False
        try:
            if self.channel:
                self.channel.close()
        except Exception:
            pass
        try:
            if self.client:
                self.client.close()
        except Exception:
            pass
        if self.on_disconnect:
            self.on_disconnect(self.session_id)

    def close(self):
        self.running = False
        self._cleanup()


# ─── Telnet Session ───────────────────────────────

class TelnetSession:
    def __init__(self, session_id, host, port, username=None, password=None):
        self.session_id = session_id
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.sock = None
        self.running = False
        self.thread = None
        self.on_output = None
        self.on_disconnect = None
        self._buffer = b""

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(10.0)
        self.sock.connect((self.host, self.port))
        self.sock.setblocking(False)
        self.running = True
        self.thread = threading.Thread(target=self._read_loop, daemon=True)
        self.thread.start()
        if self.username:
            time.sleep(0.5)
            self.write(f"{self.username}\n".encode())
            if self.password:
                time.sleep(0.3)
                self.write(f"{self.password}\n".encode())

    def _read_loop(self):
        login_attempted = False
        while self.running:
            try:
                data = self.sock.recv(65535)
                if data:
                    text = _negotiate_telnet(data)
                    if text and self.on_output:
                        self.on_output(self.session_id, text)
                    if not login_attempted and self.username:
                        self._buffer += data
                        if b"login:" in self._buffer.lower():
                            login_attempted = True
                            time.sleep(0.3)
                            if self.password and b"password:" in self._buffer.lower():
                                pass
                else:
                    break
            except (socket.error, BlockingIOError):
                time.sleep(0.005)
            except Exception:
                break
        self._cleanup()

    def write(self, data: bytes):
        if self.sock and self.running:
            try:
                self.sock.send(data)
            except Exception:
                self._cleanup()

    def resize(self, cols: int, rows: int):
        if self.sock and self.running:
            try:
                NAWS = bytes([255, 250, 31, 0, cols & 0xFF,
                              (cols >> 8) & 0xFF, 0, rows & 0xFF,
                              (rows >> 8) & 0xFF, 255, 240])
                self.sock.send(NAWS)
            except Exception:
                pass

    def _cleanup(self):
        self.running = False
        try:
            if self.sock:
                self.sock.close()
        except Exception:
            pass
        if self.on_disconnect:
            self.on_disconnect(self.session_id)

    def close(self):
        self.running = False
        self._cleanup()


# ─── Session Manager ──────────────────────────────

class WebTerminalManager:
    def __init__(self):
        self._sessions = {}
        self._lock = threading.Lock()

    def create_ssh_session(self, host, port, username, password=None, key_file=None):
        port = port or 22
        import time as _time
        session_id = f"ssh-{username}@{host}:{port}-{int(_time.time() * 1000000)}"
        session = SSHSession(session_id, host, port, username, password, key_file)
        with self._lock:
            self._sessions[session_id] = session
        try:
            session.connect()
            return session_id
        except Exception:
            with self._lock:
                self._sessions.pop(session_id, None)
            raise

    def create_telnet_session(self, host, port, username=None, password=None):
        port = port or 23
        import time as _time
        session_id = f"telnet-{username or 'anon'}@{host}:{port}-{int(_time.time() * 1000000)}"
        session = TelnetSession(session_id, host, port, username, password)
        with self._lock:
            self._sessions[session_id] = session
        try:
            session.connect()
            return session_id
        except Exception:
            with self._lock:
                self._sessions.pop(session_id, None)
            raise

    def write(self, session_id, data):
        session = self._sessions.get(session_id)
        if session:
            session.write(data)

    def resize(self, session_id, cols, rows):
        session = self._sessions.get(session_id)
        if session:
            session.resize(cols, rows)

    def disconnect(self, session_id):
        with self._lock:
            session = self._sessions.pop(session_id, None)
        if session:
            session.close()
            return True
        return False

    def set_output_callback(self, session_id, callback):
        session = self._sessions.get(session_id)
        if session:
            session.on_output = callback

    def set_disconnect_callback(self, session_id, callback):
        session = self._sessions.get(session_id)
        if session:
            session.on_disconnect = callback

    def get_active_sessions(self):
        return list(self._sessions.keys())

    def disconnect_all(self):
        with self._lock:
            ids = list(self._sessions.keys())
            for sid in ids:
                session = self._sessions.pop(sid, None)
                if session:
                    session.close()
```

---

## 2. `src/ui/app.py` — SocketIO Events to Add

Add imports and manager initialization, plus 4 new SocketIO event handlers.

### Imports to add (top of file):
```python
from protocols.web_terminal import WebTerminalManager
```

### In `create_app()`, after app creation:
```python
app.terminal_manager = WebTerminalManager()
```

### SocketIO events to add (after existing `@socketio.on("start_monitor")`):

#### `terminal_connect`
```python
@socketio.on("terminal_connect")
def ws_terminal_connect(data):
    protocol = data.get("protocol", "ssh")
    host = data.get("host", "")
    port = int(data.get("port", 22))
    username = data.get("username", "")
    password = data.get("password", None)
    key_file = data.get("key_file", None)
    try:
        mgr = app.terminal_manager
        if protocol == "telnet":
            session_id = mgr.create_telnet_session(host, port, username, password)
        else:
            session_id = mgr.create_ssh_session(host, port, username, password, key_file)
        mgr.set_output_callback(session_id,
            lambda sid, data: emit("terminal_output",
                {"session_id": sid, "data": data.decode("utf-8", errors="replace")}))
        mgr.set_disconnect_callback(session_id,
            lambda sid: emit("terminal_disconnected", {"session_id": sid}))
        emit("terminal_connected", {"session_id": session_id})
    except Exception as e:
        emit("terminal_error", {"error": str(e)})
```

#### `terminal_input`
```python
@socketio.on("terminal_input")
def ws_terminal_input(data):
    session_id = data.get("session_id", "")
    input_data = data.get("data", "")
    if app.terminal_manager.is_valid(session_id) and input_data:
        app.terminal_manager.write(session_id, input_data.encode("utf-8"))
```

#### `terminal_resize`
```python
@socketio.on("terminal_resize")
def ws_terminal_resize(data):
    session_id = data.get("session_id", "")
    cols = int(data.get("cols", 80))
    rows = int(data.get("rows", 24))
    if app.terminal_manager.is_valid(session_id):
        app.terminal_manager.resize(session_id, cols, rows)
```

#### `terminal_disconnect`
```python
@socketio.on("terminal_disconnect")
def ws_terminal_disconnect(data):
    session_id = data.get("session_id", "")
    app.terminal_manager.disconnect(session_id)
    emit("terminal_disconnected", {"session_id": session_id})
```

### Also add `is_valid` method to WebTerminalManager:
```python
def is_valid(self, session_id):
    return session_id in self._sessions
```

---

## 3. `src/ui/templates/dashboard.html` — Frontend Changes

### In `<head>`, add xterm.js CDN links:
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/xterm@5.3.0/css/xterm.min.css" />
<script src="https://cdn.jsdelivr.net/npm/xterm@5.3.0/lib/xterm.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/xterm-addon-fit@0.8.0/lib/xterm-addon-fit.min.js"></script>
```

### Add CSS for terminal:
```css
/* Terminal */
#terminal-container { width: 100%; height: calc(100vh - 200px); background: #000; border-radius: 6px; overflow: hidden; }
#terminal-connect-form { display: block; }
#terminal-connect-form.hidden { display: none; }
#terminal-session-area { display: none; }
#terminal-session-area.active { display: block; }
.terminal-bar { display: flex; align-items: center; gap: 8px; padding: 8px 12px; background: #1a1f35; border: 1px solid #21262d; border-radius: 6px 6px 0 0; font-size: 12px; color: #8b949e; }
.terminal-bar .session-info { flex: 1; }
.terminal-bar button { padding: 4px 12px; font-size: 11px; }
```

### Add nav button:
```html
<button onclick="showPanel('terminal')">💻 Terminal</button>
```

### Add terminal panel:
```html
<!-- Terminal Panel -->
<div id="panel-terminal" class="panel">
    <div class="card">
        <h4>💻 웹 터미널</h4>
        <div id="terminal-connect-form">
            <div style="display:grid;grid-template-columns:1fr 2fr 1fr 2fr;gap:8px;margin-bottom:8px">
                <select id="term-protocol">
                    <option value="ssh">SSH</option>
                    <option value="telnet">Telnet</option>
                </select>
                <input type="text" id="term-host" placeholder="호스트/IP">
                <input type="number" id="term-port" value="22" placeholder="Port">
                <input type="text" id="term-user" placeholder="사용자명">
            </div>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:12px">
                <input type="password" id="term-pass" placeholder="비밀번호">
                <button onclick="terminalConnect()">🔗 연결</button>
            </div>
            <div id="term-error" style="color:#da3633;font-size:13px;display:none"></div>
        </div>
        <div id="terminal-session-area">
            <div class="terminal-bar">
                <span class="session-info" id="term-session-info">연결됨</span>
                <button onclick="terminalDisconnect()" style="background:#da3633">🔒 종료</button>
            </div>
            <div id="terminal-container"></div>
        </div>
    </div>
</div>
```

### Add JavaScript:

```javascript
// ─── Terminal ───────────────────────────────
let term = null;
let termFit = null;
let termSessionId = null;

function terminalConnect() {
    const protocol = document.getElementById('term-protocol').value;
    const host = document.getElementById('term-host').value;
    const port = parseInt(document.getElementById('term-port').value);
    const username = document.getElementById('term-user').value;
    const password = document.getElementById('term-pass').value;

    if (!host || !username) {
        showTermError('호스트와 사용자명을 입력하세요');
        return;
    }

    document.getElementById('term-error').style.display = 'none';
    socket.emit('terminal_connect', { protocol, host, port, username, password });
}

socket.on('terminal_connected', (data) => {
    termSessionId = data.session_id;
    document.getElementById('terminal-connect-form').style.display = 'none';
    document.getElementById('terminal-session-area').classList.add('active');

    const container = document.getElementById('terminal-container');
    container.innerHTML = '';
    term = new Terminal({
        cursorBlink: true,
        cursorStyle: 'block',
        fontSize: 13,
        fontFamily: 'Menlo, Monaco, "Fira Code", monospace',
        theme: { background: '#0d1117', foreground: '#e0e6ed', cursor: '#58a6ff',
                 selectionBackground: '#58a6ff44', black: '#0d1117', red: '#da3633',
                 green: '#7ee787', yellow: '#d29922', blue: '#58a6ff',
                 magenta: '#a371f7', cyan: '#39c5cf', white: '#e0e6ed',
                 brightBlack: '#484f58', brightRed: '#ff7b72', brightGreen: '#7ee787',
                 brightYellow: '#d29922', brightBlue: '#58a6ff', brightMagenta: '#a371f7',
                 brightCyan: '#39c5cf', brightWhite: '#f0f6fc' }
    });
    termFit = new FitAddon.FitAddon();
    term.loadAddon(termFit);
    term.open(container);
    termFit.fit();

    term.onData((data) => {
        if (termSessionId) {
            socket.emit('terminal_input', { session_id: termSessionId, data });
        }
    });

    term.onResize(({ cols, rows }) => {
        if (termSessionId) {
            socket.emit('terminal_resize', { session_id: termSessionId, cols, rows });
        }
    });

    const info = document.getElementById('term-session-info');
    const proto = document.getElementById('term-protocol').value;
    const host = document.getElementById('term-host').value;
    const user = document.getElementById('term-user').value;
    info.textContent = `${proto.toUpperCase()} — ${user}@${host}`;
    term.focus();
});

socket.on('terminal_output', (data) => {
    if (term && data.session_id === termSessionId) {
        term.write(data.data);
    }
});

socket.on('terminal_error', (data) => {
    showTermError(data.error);
});

socket.on('terminal_disconnected', (data) => {
    if (data.session_id === termSessionId) {
        terminalCleanup();
    }
});

function terminalDisconnect() {
    if (termSessionId) {
        socket.emit('terminal_disconnect', { session_id: termSessionId });
    }
    terminalCleanup();
}

function terminalCleanup() {
    if (term) {
        term.dispose();
        term = null;
        termFit = null;
    }
    termSessionId = null;
    document.getElementById('terminal-connect-form').style.display = 'block';
    document.getElementById('terminal-session-area').classList.remove('active');
}

function showTermError(msg) {
    const el = document.getElementById('term-error');
    el.textContent = '❌ ' + msg;
    el.style.display = 'block';
}

// Window resize → refit terminal
window.addEventListener('resize', () => {
    if (term && termFit) {
        termFit.fit();
    }
});
```

---

## Implementation Order

1. Create `src/protocols/web_terminal.py` with all the code above
2. Modify `src/ui/app.py` — add imports, manager init, SocketIO handlers
3. Modify `src/ui/templates/dashboard.html` — add xterm.js, terminal panel, JS logic
