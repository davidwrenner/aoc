#!/usr/bin/env python3
import os
import subprocess as sp
import sys
import numpy as np
import re
from datetime import datetime as dt
from utils import *
from copy import deepcopy

t_0 = dt.now()
ans = None
fp = "../input/" + (__file__.replace('py', 'txt') if "-t" not in sys.argv else "small.txt")

with open(fp, "r") as f:
    input = f.read().split("\n\n")

towels = input[0].split(", ")
designs = input[1].split("\n")

# part a
trie = {}

def insert(t: dict, string: str) -> None:
    if not string:
        return
    first, rest = string[0], string[1:]
    if first not in t:
        t[first] = {}
    insert(t[first], rest)

def find(t: dict, string: str) -> bool:
    first, rest = string[0], string[1:]
    if not first in t:
        return False
    if "$" in t[first] and not rest:
        return True
    if not rest:
        return False
    if "$" in t[first]:
        return find(t[first], rest) or find(trie, rest)
    return find(t[first], rest)

for towel in towels:
    insert(trie, towel+"$")

ans = sum([find(trie, design) for design in designs])
print("Answer A:", ans)
t_a = dt.now()

# part b

print("Answer B:", ans)
t_b = dt.now()

sp.run("pbcopy", input=str(ans), text=True)

print(t_0, t_a, t_b, sep="\n")
