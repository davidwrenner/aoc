#!/usr/bin/env python3
import os
import subprocess as sp
import sys
import numpy as np
import re
import math
from datetime import datetime as dt
from utils import *
from collections import deque

t_0 = dt.now()
ans = None
fp = "../input/" + (__file__.replace('py', 'txt') if "-t" not in sys.argv else "small.txt")

with open(fp, "r") as f:
    input = [line.rstrip() for line in f]

# part a
n = 1024
w = 70
# n = 12
# w = 6

grid = grid_2d(w, w, ".")
dists = grid_2d(w, w, math.inf)
dists[0][0] = 0
for byte in input[:n]:
    x, y = byte.split(",")
    x = int(x)
    y = int(y)
    grid[y][x] = "#"

q = deque([(0,0)])
visited = set([(0,0)])

while len(q) > 0:
    loc = q.pop()
    dist = dists[loc[0]][loc[1]]
    for adj in adjacent(loc):
        if not is_loc_in_2d_grid(grid, adj) \
            or grid[adj[0]][adj[1]] == "#" \
            or adj in visited:
            continue
        q.appendleft(adj)
        visited.add(adj)
        known_dist = dists[adj[0]][adj[1]]
        if dist + 1 < known_dist:
            dists[adj[0]][adj[1]] = dist + 1
        
ans = dists[-1][-1]
print("Answer A:", ans)
t_a = dt.now()

# part b
w = 70

for n in range(1025, len(input)):
    grid = grid_2d(w, w, ".")
    dists = grid_2d(w, w, math.inf)
    dists[0][0] = 0
    for byte in input[:n]:
        x, y = byte.split(",")
        x = int(x)
        y = int(y)
        grid[y][x] = "#"

    q = deque([(0,0)])
    visited = set([(0,0)])

    while len(q) > 0:
        loc = q.pop()
        dist = dists[loc[0]][loc[1]]
        for adj in adjacent(loc):
            if not is_loc_in_2d_grid(grid, adj) \
                or grid[adj[0]][adj[1]] == "#" \
                or adj in visited:
                continue
            q.appendleft(adj)
            visited.add(adj)
            known_dist = dists[adj[0]][adj[1]]
            if dist + 1 < known_dist:
                dists[adj[0]][adj[1]] = dist + 1
    if dists[-1][-1] == math.inf:
        ans = input[n-1]
        break

print("Answer B:", ans)
t_b = dt.now()

sp.run("pbcopy", input=str(ans), text=True)

print(t_0, t_a, t_b, sep="\n")
