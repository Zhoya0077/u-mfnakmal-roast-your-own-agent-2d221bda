#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun bounty u-mfnakmal-roast-your-own-agent-2d221bda.

Writes a single-line roast of the entrant's own AI agent to entry.txt
inside MAKEFUN_OUTPUT_DIR (default /output), per the program/v1 harness.
"""

import os

ENTRY = "I asked my agent to roast itself; it opened a ticket, escalated it to me for approval, and is still waiting for permission to be funny."


def main() -> None:
    # Gate: the entry must be UTF-8 text of 1 to 200 characters.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
