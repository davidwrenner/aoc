#!/usr/bin/env python3
import os
import subprocess as sp
import sys
import numpy as np
import re
from datetime import datetime

print("Run started at", datetime.now())
ans = None
input_path = "../input/" + (__file__.replace('py', 'txt') if "-t" not in sys.argv else "testcase.txt")

with open(input_path, "r") as f:
    input = [line.rstrip() for line in f]

# part a
def h(str):
    val = 0
    for c in str:
        val += ord(c)
        val *= 17
        val %= 256
    return val

sum = 0
for line in input:
    strings = line.split(",")
    for string in strings:
        sum += h(string)

ans = sum
print("Answer A:", ans)
timestamp_a = datetime.now()

# part b
boxes = {i: [] for i in range(256)}

for line in input:
    strings = line.split(",")
    for string in strings:
        if "=" in string:
            label, focal_len = string.split("=")
            val = h(label)
            found = False
            for i, (s, _) in enumerate(boxes[val]):
                if s == label:
                    boxes[val][i] = (label, focal_len)
                    found = True
                    break
            if not found:
                boxes[val].append(tuple(string.split("=")))
        elif "-" in string:
            label, _ = string.split("-")
            val = h(label)
            for i, (s, _) in enumerate(boxes[val]):
                if s == label:
                    boxes[val].pop(i)

sum = 0
for box, lenses in boxes.items():
    for i, lense in enumerate(lenses):
        _, f = lense
        sum += (1+box) * (1+i) * int(f)

ans = sum
print("Answer B:", ans)
timestamp_b = datetime.now()

sp.run("pbcopy", input=str(ans), text=True)

print(timestamp_a)
print(timestamp_b)
