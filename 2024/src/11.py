#!/usr/bin/env python3
import os
import subprocess as sp
import sys
import numpy as np
import re
from datetime import datetime as dt
from utils import *

t_0 = dt.now()
ans = None
fp = "../input/" + (__file__.replace('py', 'txt') if "-t" not in sys.argv else "small.txt")

with open(fp, "r") as f:
    input = [line.rstrip() for line in f][0]

# part a
stones = input.split()
count = 0

def dfs(stone, depth):
    if depth == 0:
        return 1
    elif stone == "0":
        return dfs("1", depth-1)
    elif len(stone) % 2 == 0:
        return dfs(stone[0:len(stone)//2], depth-1) + dfs(str(int(stone[len(stone)//2:])), depth-1)
    else:
        return dfs(str(int(stone)*2024), depth-1)

for stone in stones:
    count += dfs(stone, 25)

ans = count
print("Answer A:", ans)
t_a = dt.now()

# part b
stones = input.split()
count = 0
cache = {}

def dfs(stone, depth):
    if depth == 0:
        return 1
    elif (stone, depth) in cache:
        return cache[(stone, depth)]
    elif stone == "0":
        res = dfs("1", depth-1)
    elif len(stone) % 2 == 0:
        res = dfs(stone[0:len(stone)//2], depth-1) + dfs(str(int(stone[len(stone)//2:])), depth-1)
    else:
        res = dfs(str(int(stone)*2024), depth-1)
    cache[(stone, depth)] = res
    return res

for stone in stones:
    count += dfs(stone, 75)

ans = count
print("Answer B:", ans)
t_b = dt.now()

sp.run("pbcopy", input=str(ans), text=True)

print(t_0, t_a, t_b, sep="\n")
