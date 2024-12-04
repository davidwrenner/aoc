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
mul_regex = re.compile(r"mul\([\d]{1,3},[\d]{1,3}\)")
digit_regex = re.compile(r"[\d]{1,3}")
sum = 0

input_str = "".join(input)
matches = mul_regex.findall(input_str)
for match in matches:
    pairs = digit_regex.findall(match)
    sum += int(pairs[0]) * int(pairs[1])

ans = sum
print("Answer A:", ans)
t_a = dt.now()

# part b
sum = 0

input_str = re.sub(r"(don't\(\)).*?(do\(\))", "", input_str)
matches = mul_regex.findall(input_str)
for match in matches:
    pairs = digit_regex.findall(match)
    sum += int(pairs[0]) * int(pairs[1])

ans = sum
print("Answer B:", ans)
t_b = dt.now()

sp.run("pbcopy", input=str(ans), text=True)

print(t_0, t_a, t_b, sep="\n")
