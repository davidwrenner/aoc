#!/usr/bin/env python3
import os
import subprocess as sp
import sys
import numpy as np
import re

ans = None
input_path = "../input/" + (__file__.replace('py', 'txt') if "-t" not in sys.argv else "testcase.txt")

with open(input_path, "r") as f:
    input = [line.rstrip() for line in f]

# part a
digits = re.compile("\d+")
times = [int(x) for x in digits.findall(input[0])]
distances = [int(x) for x in digits.findall(input[1])]
num_ways = []

for t, d in zip(times, distances):
    ways = 0
    for rate in range(t):
        moving_time = t-rate
        if moving_time * rate > d:
            ways += 1
    num_ways.append(ways)

ans = np.prod(num_ways)
print("Answer A:", ans)

# part b
t = int("".join(digits.findall(input[0])))
d = int("".join(digits.findall(input[1])))

ways = 0
for rate in range(t):
    moving_time = t-rate
    if moving_time * rate > d:
        ways += 1
ans = ways

print("Answer B:", ans)
sp.run("pbcopy", input=str(ans), text=True)
