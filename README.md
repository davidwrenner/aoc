# aoc
My solutions to [Advent of Code](https://adventofcode.com).

### Configuration for automatic file generation
- Set the parameters in `config`
- Run `gen.sh`. This script generates a new solution file for the 'next day' by copying a template file, and downloads the unique puzzle input to a corresponding input file
  - The 'next day' is defined as the earliest, 1-indexed day in [01, 25] for which there is not already a solution file
- Each year must be configured with the minimum skeleton below to use `gen.sh`
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
*This script follows the automation [guidelines](https://www.reddit.com/r/adventofcode/wiki/faqs/automation/). Input is cached and only downloaded when not found locally.*
