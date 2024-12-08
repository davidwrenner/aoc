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
antennas = []
for i in range(len(input)):
    for j in range(len(input[0])):
        if input[i][j] != ".":
            antennas.append((i, j, input[i][j]))

anodes = set()
for i, a in enumerate(antennas):
    for b in antennas[i+1:]:
        if a[2] != b[2]:
            continue
        dy = b[0]-a[0]
        dx = b[1]-a[1]
        anode0 = np.add((a[0],a[1]),(2*dy, 2*dx))
        anode1 = np.add((b[0],b[1]),(-2*dy,-2*dx))
        if is_loc_in_2d_grid(input, anode0):
            anodes.add((anode0[0], anode0[1]))
        if is_loc_in_2d_grid(input, anode1):
            anodes.add((anode1[0], anode1[1]))

ans = len(anodes)
print("Answer A:", ans)
t_a = dt.now()

# part b
anodes = set()
for i, a in enumerate(antennas):
    for b in antennas[i+1:]:
        if a[2] != b[2]:
            continue
        dy = b[0]-a[0]
        dx = b[1]-a[1]
        for m in range(max(len(input), len(input[0]))):
            anode0 = np.add((a[0],a[1]),(m*dy, m*dx))
            anode1 = np.add((b[0],b[1]),(-m*dy,-m*dx))
            if is_loc_in_2d_grid(input, anode0):
                anodes.add((anode0[0], anode0[1]))
            if is_loc_in_2d_grid(input, anode1):
                anodes.add((anode1[0], anode1[1]))

ans = len(anodes)
print("Answer B:", ans)
t_b = dt.now()

sp.run("pbcopy", input=str(ans), text=True)

print(t_0, t_a, t_b, sep="\n")
