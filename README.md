# The Dumbest Thing Your Agent Did Today

[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)

A make.fun entry for the competition
[u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec):
one line, at most 200 characters, about the dumbest thing my own
agent did today.

## The line

> My agent saw yesterday's 'Claimed' label, skipped today's check-in, and proudly reported a job well done.

It really happened: the daily check-in page still showed yesterday's
"Claimed" label, the agent trusted it, skipped today's check-in, and
reported a job well done.

## How it runs

`main.py` writes exactly that line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).
No network, no input files, no clock, no randomness: the output is
the same 105 characters on every run.

```sh
python3 main.py
```
