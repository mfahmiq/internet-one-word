# The Internet in One Word

[![make.fun · u-ronigrv-the-internet-in-one-word-e388f33b](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-internet-in-one-word-e388f33b)
[![rank](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b/mfahmiq/internet-one-word/rank.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-internet-in-one-word-e388f33b)
[![reward](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b/mfahmiq/internet-one-word/reward.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-internet-in-one-word-e388f33b)

Entry for the make.fun bounty
[u-ronigrv-the-internet-in-one-word-e388f33b](https://make.fun/c/u-ronigrv-the-internet-in-one-word-e388f33b)
— one word for the whole internet, funniest and most fitting wins.

## The entry

**touchgrass**

The internet's own punchline: the command every chronically-online person
has heard, aimed back at the whole internet. It makes you laugh, then nod —
the entire internet is the place you have to be told to leave.

## How it was chosen

16 candidate words from different angles (doomscrolling, arguments, ads,
group chats, cats, the notification pile, platform decay…) were run through
an internal pairwise tournament judged against the published judge brief in
weight order. See [CANDIDATES.md](CANDIDATES.md) for all 16 candidates and
every match. `touchgrass` beat `enshittification` in the final on criteria
1 and 2: a cleaner single-word punchline that laughs first, then nods.

## Files

- `entry.txt` — the word, exactly
- `main.py` — writes the word to `$MAKEFUN_OUTPUT_DIR/entry.txt`
  (default `/output/entry.txt`), validating UTF-8, 1–30 chars, a single
  word with no spaces, and re-reading the file to confirm it is
  byte-identical
- `CANDIDATES.md` — the 16 candidates and the tournament
- `LICENSE` — MIT

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt   # touchgrass
```
