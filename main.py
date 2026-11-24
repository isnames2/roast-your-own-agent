#!/usr/bin/env python3
"""make.fun entry: Roast Your Own Agent.

Writes a one-line roast of my own AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (one line, at most 200 characters).
Pure Python standard library only; no third-party imports,
no network, deterministic output.
"""

import os

ROAST = (
    "I asked my agent to fix one line. It opened a ticket, "
    "assigned it to itself, and closed it as 'cannot reproduce' "
    "\u2014 on my own laptop."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ROAST)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
