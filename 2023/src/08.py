#!/usr/bin/env python3
import os
import subprocess as sp
import sys
import numpy as np
import re
import datetime

ans = None
input_path = "../input/" + (__file__.replace('py', 'txt') if "-t" not in sys.argv else "testcase.txt")

with open(input_path, "r") as f:
    input = [line.rstrip() for line in f]

lr_instructions = input[0]
elements = input[2:]

network = {}
for line in elements:
    node, pair = line.split(" = ")
    left, right = pair[1:-1].split(", ")
    network[node] = (left, right)

# part a
ptr = "AAA"
end = "ZZZ"
steps = 0
while ptr != end:
    for d in lr_instructions:
        if d == "L":
            ptr = network[ptr][0]
        elif d == "R":
            ptr = network[ptr][1]
        steps += 1
        if ptr == end:
            break

ans = steps
print("Answer A:", ans)

# part b
ptrs = [k for k in network.keys() if k[2] == "A"]
steps_arr = []
for ptr in ptrs:
    steps = 0
    while ptr[2] != "Z":
        for d in lr_instructions:
            if d == "L":
                ptr = network[ptr][0]
            elif d == "R":
                ptr = network[ptr][1]
            steps += 1
            if ptr[2] == "Z":
                break
    steps_arr.append(steps)

ans = np.lcm.reduce(steps_arr)
print("Answer B:", ans)
sp.run("pbcopy", input=str(ans), text=True)
