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
connections = {}
for conn in input:
    a, b = conn.split("-")
    if not a in connections:
        connections[a] = []
    if not b in connections:
        connections[b] = []
    connections[a].append(b)
    connections[b].append(a)

triples = set()
for conn in input:
    a, b = conn.split("-")
    a_vals = connections[a]
    b_vals = connections[b]
    for i in range(len(a_vals)):
        for j in range(len(b_vals)):
            if a_vals[i] == b_vals[j]:
                triples.add(tuple(sorted((a, b, a_vals[i]))))

count = 0
for t in triples:
    a,b,c = t
    if a[0] == "t" or b[0] == "t" or c[0] == "t":
        count += 1

ans = count
print("Answer A:", ans)
t_a = dt.now()

# part b

print("Answer B:", ans)
t_b = dt.now()

sp.run("pbcopy", input=str(ans), text=True)

print(t_0, t_a, t_b, sep="\n")
