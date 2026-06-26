#!/bin/bash
DIR="$(cd "$(dirname "$0")" && pwd)"
VENV="$DIR/.venv"

if [ ! -d "$VENV" ]; then
  python3 -m venv "$VENV"
  "$VENV/bin/pip" install --quiet fastapi uvicorn markdown pygments jinja2 2>&1
fi

cd "$DIR"
"$VENV/bin/python3" web.py
