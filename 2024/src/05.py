#!/usr/bin/env python3
import os
import subprocess as sp
import sys
import numpy as np
import re
from datetime import datetime as dt
from utils import *
from itertools import permutations

t_0 = dt.now()
ans = None
fp = "../input/" + (__file__.replace('py', 'txt') if "-t" not in sys.argv else "small.txt")

with open(fp, "r") as f:
    input = f.read().split("\n\n")

# part a
before = {}
for ordering in input[0].split("\n"):
    first, second = ordering.split("|")
    if first in before:
        before[first].append(second)
    else:
        before[first] = [second]

middles = []
incorrect = []
for update in input[1].split("\n"):
    pages = update.split(",")
    is_correct = True
    for i, page in enumerate(pages):
        for p in pages[i+1:]:
            if page in before and p in before[page]:
                ...
            else:
                is_correct = False
                break
    if is_correct:
        middles.append(int(pages[len(pages)//2]))
    else:
        incorrect.append(update)

ans = sum(middles)
print("Answer A:", ans)
t_a = dt.now()

# part b
middles = []
for update in incorrect:
    pages = update.split(",")
    for i, _ in enumerate(pages):
            for j, _ in enumerate(pages[i+1:]):
                if pages[i] in before and pages[i+j+1] in before[pages[i]]:
                    ...
                else:
                    pages[i], pages[j+i+1] = pages[j+i+1], pages[i]
    middles.append(int(pages[len(pages)//2]))

ans = sum(middles)
print("Answer B:", ans)
t_b = dt.now()

sp.run("pbcopy", input=str(ans), text=True)

print(t_0, t_a, t_b, sep="\n")
