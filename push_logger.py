#!/usr/bin/env python3
"""
push_logger.py — appends a CHANGELOG.md entry for the current commit.

Run this manually after any commit (or wire it into a pre-existing workflow
that already has permission to run, e.g. voxel-book.yml / voxel-novel.yml,
by adding a call to this script as a step).

Usage:
    python push_logger.py
"""
import subprocess
import datetime

def run(cmd):
    return subprocess.check_output(cmd, shell=True, text=True).strip()

def main():
    sha_short = run("git rev-parse --short HEAD")
    author = run("git log -1 --pretty=%an")
    msg = run("git log -1 --pretty=%B").strip()
    files = run("git diff --name-only HEAD~1 HEAD 2>/dev/null || echo '(first commit)'")
    date = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    entry = f"\n## {date} — {sha_short}\n- Author: {author}\n- Message: {msg}\n- Files changed:\n"
    entry += "\n".join(f"    - {f}" for f in files.splitlines())

    with open("CHANGELOG.md", "a") as f:
        f.write(entry + "\n")

    print("Logged:", sha_short)

if __name__ == "__main__":
    main()
