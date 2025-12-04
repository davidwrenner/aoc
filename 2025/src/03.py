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
joltage = 0

for bank in input:
    joltage += max(int(bank[i]+max(bank[i+1:])) for i in range(len(bank)-1))

ans = joltage

print("Answer A:", ans)
t_a = dt.now()

# part b
joltage = 0

for bank in input:
    j = ""
    n = 12
    prev = None

    for k in range(n, 0, -1):
        i = k
        m = i
        while prev is None or i < prev:
            if bank[-i] >= bank[-m]:
                m = i
            if i == len(bank) or bank[-i] > max(bank[:-i]):
                break
            i += 1
        j += bank[-m]
        prev = m
    joltage += int(j)

ans = joltage

print("Answer B:", ans)
t_b = dt.now()

sp.run("pbcopy", input=str(ans), text=True)

print(t_0, t_a, t_b, sep="\n")
