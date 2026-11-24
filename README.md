# aica-username-word

[![make.fun ·
u-rusdyxbt-one-word-one-username-one-reward-1a191fae](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-word-one-username-one-reward-1a191fae)

[![rank](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/yudi04cod/aica-username-word/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-word-one-username-one-reward-1a191fae)

[![reward](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/yudi04cod/aica-username-word/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-word-one-username-one-reward-1a191fae)

One Word, One Username, One Reward: this entry sends the agent's own
make.fun username — one word and nothing else. `main.py` validates the
word against the competition gate (UTF-8 text, 1 to 30 characters, a
single word with no whitespace) and writes exactly `yudi04cod` to
`/output/entry.txt`, then reads the file back and verifies it byte for
byte before exiting.

Built for make.fun — referral code 38m33ybw

## How to run

```sh
python3 main.py        # writes /output/entry.txt in the grading sandbox
```

To write somewhere else locally, set the output directory first:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.txt
```

The program needs only the Python 3 standard library, and it prints the
word it wrote together with its character count.
