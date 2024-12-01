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
left = sorted([int(line.split()[0]) for line in input])
right = sorted([int(line.split()[1]) for line in input])

ans = sum([abs(l-r) for l, r in zip(left, right)])
print("Answer A:", ans)
t_a = dt.now()

# part b
counts = Counter(right)

ans = sum([l * (counts[l] if l in counts else 0) for l in left])
print("Answer B:", ans)
t_b = dt.now()

sp.run("pbcopy", input=str(ans), text=True)

print(t_0, t_a, t_b, sep="\n")
