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
    input = [line.rstrip() for line in f]

# part a
target = "XMAS"
count = 0

def check_bounds(coordinates):
    return 0 <= coordinates[0] < len(input) and 0 <= coordinates[1] < len(input[0])


def count_at_pos(i, j):
    count = 0
    dirs = [
        [1,0],[0,1],[1,1],[1,-1]
    ]

    start = i, j

    for d in dirs:
        str = ""
        for k in range(len(target)):
            c = np.add(start, np.multiply(d, k))
            if not check_bounds(c):
                break
            str += input[c[0]][c[1]]

        if str == target or str[::-1] == target:
            count += 1

    return count

for i in range(len(input)):
    for j in range(len(input[0])):
        count += count_at_pos(i, j)

ans = count
print("Answer A:", ans)
t_a = dt.now()

# part b
count = 0
target = "MAS"

def count_at_pos(i, j):
    count = 0

    start = i, j

    c0 = np.add(start, [0,0])
    c1 = np.add(start, [1,1])
    c2 = np.add(start, [-1,-1])
    c3 = np.add(start, [-1,1])
    c4 = np.add(start, [1,-1])

    for c in [c0, c1, c2, c3, c4]:
        if not check_bounds(c):
            return 0

    d1 = input[c1[0]][c1[1]] + input[c0[0]][c0[1]] + input[c2[0]][c2[1]]
    d2 = input[c3[0]][c3[1]] + input[c0[0]][c0[1]] + input[c4[0]][c4[1]]

    if d1 == target and d2 == target:
        count += 1
    elif d1[::-1] == target and d2 == target:
        count += 1
    elif d1 == target and d2[::-1] == target:
        count += 1
    elif d1[::-1] == target and d2[::-1] == target:
        count += 1

    return count


for i in range(len(input)):
    for j in range(len(input[0])):
        count += count_at_pos(i, j)

ans = count
print("Answer B:", ans)
t_b = dt.now()

sp.run("pbcopy", input=str(ans), text=True)

print(t_0, t_a, t_b, sep="\n")
