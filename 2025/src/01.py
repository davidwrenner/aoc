#!/usr/bin/env python3
import subprocess as sp
import sys
from datetime import datetime as dt

t_0 = dt.now()
ans = None
fp = "../input/" + (__file__.replace('py', 'txt') if "-t" not in sys.argv else "small.txt")

with open(fp, "r") as f:
    input = [line.rstrip() for line in f]

# part a
zeros = 0

curr = 50
for turn in input:
    direction, amount = turn[0], int(turn[1:])
    if direction == "L":
        curr = (curr - amount) % 100
    else:
        curr = (curr + amount) % 100
    if curr == 0:
        zeros += 1

ans = zeros

print("Answer A:", ans)
t_a = dt.now()

# part b
zeros = 0

curr = 50
for turn in input:
    direction, amount = turn[0], int(turn[1:])
    while amount > 0:
        if direction == "L":
            curr = (curr - 1) % 100
        else:
            curr = (curr + 1) % 100
        if curr == 0:
            zeros += 1
        amount -= 1

ans = zeros

print("Answer B:", ans)
t_b = dt.now()

sp.run("pbcopy", input=str(ans), text=True)

print(t_0, t_a, t_b, sep="\n")
