#!/usr/bin/env python3
import os
import subprocess as sp
import sys
import numpy as np
import re
from datetime import datetime as dt
from utils import *
from collections import Counter

t_0 = dt.now()
ans = None
fp = "../input/" + (__file__.replace('py', 'txt') if "-t" not in sys.argv else "small.txt")

with open(fp, "r") as f:
    input = [line.rstrip() for line in f]

# part a
sum = 0

left = sorted([int(line.split()[0]) for line in input])
right = sorted([int(line.split()[1]) for line in input])

for l, r in zip(left, right):
    sum += abs(l - r)

ans = sum
print("Answer A:", ans)
t_a = dt.now()

# part b
sum = 0

counts = Counter(right)

for l in left:
    sum += l * (counts[l] if l in counts else 0)

ans = sum
print("Answer B:", ans)
t_b = dt.now()

sp.run("pbcopy", input=str(ans), text=True)

print(t_0, t_a, t_b, sep="\n")
