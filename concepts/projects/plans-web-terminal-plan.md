---
title: Web Terminal Plan
created: 2026-06-01
updated: 2026-06-01
type: concept
tags: [project, programming, python, javascript, web]
sources: [raw/local/project/plans-web-terminal-plan-2026-06-01.md]
source_file: /Users/bearj/coding_projects/netmaster/.opencode/plans/web-terminal-plan.md
confidence: high
links: [[plans-site-refinement|개인 사이트 자동화 고도화]], [[docs-phase1-planning|Phase 1 기획 문서]]
---

# Web Terminal Plan

> 📁 원본: `/Users/bearj/coding_projects/netmaster/.opencode/plans/web-terminal-plan.md`
> 📅 수집: 2026-06-01
> 🏷️ 카테고리: project

## 내용

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
            kwargs["key_filena

...(내용 생략)...
