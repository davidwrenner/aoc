import sys
import os
import re
from collections import deque

# file I/O
input_file = sys.argv[0][0:2] + ".txt"
input_path = "../input/" + input_file

if not os.path.exists(input_path):
    raise FileNotFoundError(f"Did not find expected input {input_path}")

with open(input_path, "r") as f:
    input = [line.rstrip() for line in f if line != "\n"]

crate_re = re.compile(r"(\[(?P<crate>[\w]+)\]\s?)|(?P<_>[\s]{4})")
instruction_re = re.compile(r"^move (?P<quantity>[\d]+) from (?P<from>[\d]+) to (?P<to>[\d]+)$")

n_stacks = 9


def initialize_crates():
    stacks = [deque() for _ in range(n_stacks + 1)]
    for line in input:
        match = [m.groupdict()["crate"] for m in crate_re.finditer(line)]
        if not match:
            break
        for i, e in enumerate(match):
            if e:
                stacks[i].appendleft(e)
    return stacks


def val(match, group_name):
    return int(match.group(group_name))


def do_moves(stacks):
    for line in input:
        m = instruction_re.match(line)
        if not m:
            continue
        for _ in range(val(m, "quantity")):
            stacks[val(m, "to") - 1].append(stacks[val(m, "from") - 1].pop())


def get_top_crates(stacks):
    top_crates = ""
    for stack in stacks:
        top_crates += stack[-1] if stack else ""
    return top_crates


ans = None
# part a
stacks = initialize_crates()
do_moves(stacks)
ans = get_top_crates(stacks)
print("Answer A:", ans)

# part b
def do_moves_9001(stacks):
    for line in input:
        m = instruction_re.match(line)
        if not m:
            continue
        temp = []
        for _ in range(val(m, "quantity")):
            temp.append(stacks[val(m, "from") - 1].pop())
        for _ in range(val(m, "quantity")):
            stacks[val(m, "to") - 1].append(temp.pop())


stacks = initialize_crates()
do_moves_9001(stacks)
ans = get_top_crates(stacks)
print("Answer B:", ans)
