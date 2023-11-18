# aoc
My solutions to [Advent of Code](https://adventofcode.com).

### Automatic file generation
Parameters in `config` must be set to run `gen.sh`. This script looks for existing solution files and will generate input and solution files for the earliest day in the current year without a solution file based on a predefined template. This allows for puzzles to be completed in sequence the day they unlock or asynchronously thereafter. To use for a different year, ensure the repo is setup with the minimum structure below.
```
aoc/
├─ <year>/
│  ├─ input/
│  ├─ src/
│  │  ├─ template.py
├─ ...
├─ config
├─ gen.sh
```
This script follows the automation [guidelines](https://www.reddit.com/r/adventofcode/wiki/faqs/automation/). Note that input is cached and only downloaded when not found locally.
