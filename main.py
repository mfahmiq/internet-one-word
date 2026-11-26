"""The Internet in One Word — make.fun entry.

Entry (10 chars):
    touchgrass

Why it won the internal tournament (16 candidates, pairwise, judged
against the published brief in weight order):
  1. Single word: one token, 10 chars, no spaces — a word, not a
     phrase, sentence or list.
  2. Earns a laugh: it is the internet's own punchline — the command
     every chronically-online person has heard, aimed back at the
     whole internet. Funny by itself, no explanation needed.
  3. True about the whole internet: it names the defining condition
     of life online — everyone here needs to go outside. Not one app,
     one site or one mood; the entire internet is the place you have
     to be told to leave.
  4. Surprises: nobody's first reach is a verb telling the internet
     to go outside; the obvious words are chaos, doomscroll, memes.
  5. Lands in one beat: 10 characters, instantly readable, hits
     before the reader thinks.
It beat the runner-up ("enshittification") in the final on criteria
1 and 2: a cleaner single-word punchline that makes the reader laugh
first, then nod — where the runner-up is a clever diagnosis that
takes a beat to parse and reads more like a sigh than a laugh.

Writes ENTRY to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt),
then self-verifies: UTF-8, 1-30 chars, a single word (no spaces), not
whitespace-only, no leading/trailing whitespace, and re-reads the
written file to confirm it is byte-identical. Exits non-zero on any
failure.
"""

import os
import sys

ENTRY = "touchgrass"


def main() -> int:
    # MAKEFUN_OUTPUT_DIR is a directory; default /output.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    path = os.path.join(out_dir, "entry.txt")

    # Validate before writing.
    if not ENTRY or not ENTRY.strip():
        print("error: entry is empty or whitespace-only", file=sys.stderr)
        return 1
    if ENTRY != ENTRY.strip():
        print("error: entry has leading or trailing whitespace", file=sys.stderr)
        return 1
    if " " in ENTRY or "\t" in ENTRY:
        print("error: entry must be a single word (no spaces)", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(ENTRY) <= 30:
        print(f"error: entry is {len(ENTRY)} chars, must be 1-30", file=sys.stderr)
        return 1
    try:
        ENTRY.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"error: entry is not UTF-8: {exc}", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)

    # Re-read and confirm byte-identical.
    with open(path, "rb") as fh:
        written = fh.read()
    if written != data:
        print("error: written file is not byte-identical to ENTRY", file=sys.stderr)
        return 1
    text = written.decode("utf-8")
    if (
        text != ENTRY
        or not 1 <= len(text) <= 30
        or not text.strip()
        or " " in text
    ):
        print("error: re-read verification failed", file=sys.stderr)
        return 1

    print(f"wrote {path}: {len(ENTRY)} chars")
    print(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
