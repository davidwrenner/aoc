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
    input = f.read().split("\n\n")

# part a
schemas = [block.split("\n") for block in input]
count = 0

for a in range(len(schemas)):
    for b in range(a+1, len(schemas)):
        valid = True
        for i in range(len(schemas[a])):
            for j in range(len(schemas[a][i])):
                if schemas[a][i][j] == "#" and schemas[b][i][j] == "#":
                    valid = False
                    break
        if valid:
            count += 1

ans = count
print("Answer A:", ans)
t_a = dt.now()

# part b

print("Answer B:", ans)
t_b = dt.now()

sp.run("pbcopy", input=str(ans), text=True)

print(t_0, t_a, t_b, sep="\n")
