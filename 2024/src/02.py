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
    input = [line.rstrip() for line in f]

# part a
def is_safe_diff(a, b):
    return 1 <= abs(b-a) <= 3

def check(levels):
    if levels == sorted(levels) or levels == sorted(levels, reverse=True):
        pass
    else:
        return False
    
    level = int(levels[0])

    for i, l in enumerate(levels):
        if i == 0:
            continue
        
        if is_safe_diff(level, int(l)):
            level = int(l)
            if i == len(levels) - 1:
                return True
        else:
            return False


num_safe = 0

for report in input:
    levels = [int(l) for l in report.split()]
    if check(levels):
        num_safe += 1 


ans = num_safe
print("Answer A:", ans)
t_a = dt.now()

# part b
num_safe = 0

def get_mutations(levels):
    mutations = [levels]
    for i in range(len(levels)):
        cpy = deepcopy(levels)
        del cpy[i]
        mutations.append(cpy)
    return mutations

for report in input:
    levels = [int(l) for l in report.split()]
    if any(check(m) for m in get_mutations(levels)):
        num_safe += 1 

ans = num_safe
print("Answer B:", ans)
t_b = dt.now()

sp.run("pbcopy", input=str(ans), text=True)

print(t_0, t_a, t_b, sep="\n")
