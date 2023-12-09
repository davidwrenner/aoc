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
def build_diffs(history):
    diffs = []
    for i in range(1, len(history)):
        diffs.append(history[i] - history[i-1])
    if any(diffs):
        return history[-1] + build_diffs(diffs)
    return history[-1]

sum = 0
for line in input:
    history = [int(x) for x in line.split()]
    next_history = build_diffs(history)
    sum += next_history
        
ans = sum
print("Answer A:", ans)

# part b
def build_diffs(history):
    diffs = []
    for i in range(1, len(history)):
        diffs.append(history[i] - history[i-1])
    if any(diffs):
        return history[0] - build_diffs(diffs)
    return history[0]

sum = 0
for line in input:
    history = [int(x) for x in line.split()]
    next_history = build_diffs(history)
    sum += next_history
        
ans = sum
print("Answer B:", ans)
sp.run("pbcopy", input=str(ans), text=True)
