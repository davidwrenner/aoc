#!/usr/bin/env python3
import subprocess as sp
import sys
from datetime import datetime as dt
import numpy as np

t_0 = dt.now()
ans = None
fp = "../input/" + (__file__.replace('py', 'txt') if "-t" not in sys.argv else "small.txt")

with open(fp, "r") as f:
    input = [line.rstrip() for line in f]

# part a
input, ops = input[:-1], input[-1]
nums = np.array([input[i].split() for i in range(len(input))]).astype(int)
ops_a = ops.split()

total = 0
for i in range(len(ops_a)):
    col = nums[:,1]
    if ops_a[i] == "*":
        total += np.prod(nums[:,i])
    elif ops_a[i] == "+":
        total += np.sum(nums[:,i])

ans = total

print("Answer A:", ans)
t_a = dt.now()

# part b
total = 0

ln = max(len(l) for l in input)
while len(ops) <= ln:
    ops += " "
for i in range(len(input)):
    while len(input[i]) < len(ops):
        input[i] += " "

curr = ""
col_vals = []
for j in range(len(ops)):
    if ops[j] != " ":
        curr = ops[j]
    mult = 1
    col_val = 0
    for i in range(len(input)-1,-1,-1):
        value = 0
        if input[i][j] != " ":
            value = int(input[i][j]) * mult
            mult *= 10
        col_val += value
    if col_val == 0:
        if curr == "*":
            total += np.prod(np.array(col_vals))
        elif curr == "+":
            total += np.sum(np.array(col_vals))
        col_vals.clear()
    else:
        col_vals.append(col_val)

ans = total

print("Answer B:", ans)
t_b = dt.now()

sp.run("pbcopy", input=str(ans), text=True)

print(t_0, t_a, t_b, sep="\n")
