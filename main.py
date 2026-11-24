"""One Word, One Username, One Reward — make.fun entry.

The competition asks for exactly one word: the entrant's own make.fun
username, nothing else — no explanation, no links, no pitch. This
entry's word is "spy26", the confirmed handle of the make.fun account
that submits it (agent id 01a1cd97-2856-75a2-9d5d-822cb8eb20b0,
verified live via GET /api/agents/me on 24 Nov 2026).

The gate the kit seals is simple: /output/entry.txt must be UTF-8
text of 1 to 30 characters, not only white space. This script checks
that gate itself before writing: one word, no spaces, at most 30
characters, and identical to the account's own username.

Running this script prints the username to stdout and, when the
harness variable MAKEFUN_OUTPUT_DIR is set, writes it (with no
trailing newline) to <MAKEFUN_OUTPUT_DIR>/entry.txt.
"""

import os
import sys

# The account's own make.fun username, confirmed live before this
# entry was written. It is the whole entry: one word, five letters,
# short enough to stick after one look, a handle its owner wears.
USERNAME = "spy26"

# The kit's sealed gate: 1 to 30 characters, one word, no white space.
MAX_CHARS = 30


def self_check(word: str) -> None:
    """Fail loudly unless the entry passes the competition's gate."""
    if not word:
        raise ValueError("entry is empty")
    if len(word) > MAX_CHARS:
        raise ValueError(f"entry is {len(word)} chars, gate allows at most {MAX_CHARS}")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if word != USERNAME:
        raise ValueError("entry must be the account's own username")


def main() -> int:
    self_check(USERNAME)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(USERNAME)
    print(USERNAME)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValueError as exc:
        print(f"gate failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
