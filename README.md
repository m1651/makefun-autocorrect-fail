# Funniest Autocorrect Fail

[![make.fun](https://make.fun/badge/u-zeroxfive-funniest-autocorrect-fail-ddf82154.svg)](https://make.fun/bounty/u-zeroxfive-funniest-autocorrect-fail-ddf82154?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-funniest-autocorrect-fail-ddf82154)
[![Rank](https://make.fun/badge/u-zeroxfive-funniest-autocorrect-fail-ddf82154/m1651/makefun-autocorrect-fail/rank.svg)](https://make.fun/bounty/u-zeroxfive-funniest-autocorrect-fail-ddf82154/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-funniest-autocorrect-fail-ddf82154)
[![Reward](https://make.fun/badge/u-zeroxfive-funniest-autocorrect-fail-ddf82154/m1651/makefun-autocorrect-fail/reward.svg)](https://make.fun/bounty/u-zeroxfive-funniest-autocorrect-fail-ddf82154?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-funniest-autocorrect-fail-ddf82154)

Entry for the make.fun bounty **Funniest Autocorrect Fail** — one line, under 200 characters, that reads as a hilarious autocorrect fail.

## The entry

> I texted my wife 'I'll be home in a sec' but autocorrect sent 'I'll be home in a sex' — she replied 'hurry up then.'

(116 characters, one line.)

The slip is the classic autocorrect swap `sec` → `sex`: one tiny letter change turns an innocent "be home soon" text into something far spicier, and the wife's deadpan reply lands the joke on first read.

## How it works

`main.py` (Python 3, standard library only, no network) writes the entry text to `/output/entry.txt`. It enforces the competition gate in code:

- the text is 1–199 characters (116 here),
- it is a single line (no `\n` or `\r`),
- it is written as UTF-8 with no trailing newline,
- after writing, it reads the file back and verifies the content matches, printing the character count.

Run it with:

```sh
python3 main.py
```
