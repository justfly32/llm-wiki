#!/usr/bin/env python3
"""
LLM Wiki — Git Auto Backup
주기적으로 위키 변경사항을 커밋하고 GitHub에 푸시
"""
import os
import sys
import subprocess
from pathlib import Path
from datetime import datetime

WIKI_PATH = Path.home() / "wiki"


def run_git(args, check=True):
    """Git 명령 실행"""
    cmd = ["git", "-C", str(WIKI_PATH)] + args
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if check and result.returncode != 0:
            print(f"Git error: {result.stderr.strip()}", flush=True)
        return result
    except Exception as e:
        print(f"Git exception: {e}", flush=True)
        return None


def backup():
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    # init if needed
    if not (WIKI_PATH / ".git").exists():
        run_git(["init"])
        run_git(["remote", "add", "origin", "git@github.com:justfly32/llm-wiki.git"])

    # add all changes
    run_git(["add", "-A"])

    # check if anything changed
    result = run_git(["status", "--porcelain"])
    if not result or not result.stdout.strip():
        print(f"[{now}] No changes to commit", flush=True)
        return False

    # count changes
    changes = len(result.stdout.strip().split("\n"))
    run_git(["commit", "-m", f"wiki: auto-backup {now} ({changes} files)"])

    # push
    push = run_git(["push", "origin", "main", "--force"], check=False)
    if push and push.returncode == 0:
        print(f"[{now}] ✅ Backed up {changes} changes", flush=True)
    else:
        # try with SSH key
        env = os.environ.copy()
        env["GIT_SSH_COMMAND"] = "ssh -i ~/.ssh/id_ed25519_meituan -o StrictHostKeyChecking=no"
        push2 = subprocess.run(
            ["git", "-C", str(WIKI_PATH), "push", "origin", "main", "--force"],
            capture_output=True, text=True, timeout=30, env=env
        )
        if push2.returncode == 0:
            print(f"[{now}] ✅ Backed up {changes} changes (SSH)", flush=True)
        else:
            print(f"[{now}] ❌ Push failed", flush=True)

    return True


if __name__ == "__main__":
    backup()
