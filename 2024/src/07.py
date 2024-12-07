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
ans = 0

def do_recursion(vals, tv, curr):
    product = curr * int(vals[0])
    sum = curr + int(vals[0])
    if len(vals) == 1:
        return product == tv or sum == tv
    if product > tv and sum > tv:
        return False
    else:
        return do_recursion(vals[1:], tv, sum) or do_recursion(vals[1:], tv, product)

for equation in input:
    test_val, rhs = equation.split(": ")
    values = rhs.split()
    if do_recursion(values, int(test_val), 0):
        ans += int(test_val)
    
print("Answer A:", ans)
t_a = dt.now()

# part b
ans = 0

def do_recursion(vals, tv, curr):
    product = curr * int(vals[0])
    sum = curr + int(vals[0])
    cat = int(str(curr) + vals[0])
    if len(vals) == 1:
        return product == tv or sum == tv or cat == tv
    if product > tv and sum > tv and cat > tv:
        return False
    else:
        return do_recursion(vals[1:], tv, sum) or do_recursion(vals[1:], tv, product) or do_recursion(vals[1:], tv, cat)

for equation in input:
    test_val, rhs = equation.split(": ")
    values = rhs.split()
    if do_recursion(values, int(test_val), 0):
        ans += int(test_val)

print("Answer B:", ans)
t_b = dt.now()

sp.run("pbcopy", input=str(ans), text=True)

print(t_0, t_a, t_b, sep="\n")
