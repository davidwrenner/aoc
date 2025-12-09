#!/usr/bin/env python3
import subprocess as sp
import sys
from datetime import datetime as dt
from typing import Tuple, List
import numpy as np

t_0 = dt.now()
ans = None
fp = "../input/" + (__file__.replace('py', 'txt') if "-t" not in sys.argv else "small.txt")

with open(fp, "r") as f:
    input = [line.rstrip().split(",") for line in f]
for i, (a, b, c) in enumerate(input):
    input[i] = (int(a), int(b), int(c))

def dist(p: Tuple[int, int, int], q: Tuple[int, int, int]) -> float:
    return np.sqrt((p[0]-q[0])**2+(p[1]-q[1])**2+(p[2]-q[2])**2)

def find_in_circuits(cs: List[List[int]], val: int) -> int:
    for i, lst in enumerate(cs):
        if val in lst:
            return i
    return -1

# part a
circuits = [[i] for i in range(len(input))]
dists = np.array([[dist(p, q) for q in input] for p in input])
dists[dists == 0] = np.inf

for i in range(1000):
    min_coords = np.unravel_index(np.argmin(dists), shape=dists.shape)
    p, q = min_coords
    dists[p][q], dists[q][p] = np.inf, np.inf

    loc_src = find_in_circuits(circuits, p)
    loc_dest = find_in_circuits(circuits, q)

    if loc_src != loc_dest:
        circuits[loc_dest] += circuits[loc_src]
        del circuits[loc_src]

circuits.sort(key=lambda lst: len(lst))
ans = np.prod([len(lst) for lst in circuits[-3:]])

print("Answer A:", ans)
t_a = dt.now()

# part b
circuits = [[i] for i in range(len(input))]
dists = np.array([[dist(p, q) for q in input] for p in input])
dists[dists == 0] = np.inf

while len(circuits) > 1:
    min_coords = np.unravel_index(np.argmin(dists), shape=dists.shape)
    p, q = min_coords
    dists[p][q], dists[q][p] = np.inf, np.inf

    loc_src = find_in_circuits(circuits, p)
    loc_dest = find_in_circuits(circuits, q)

    if loc_src != loc_dest:
        circuits[loc_dest] += circuits[loc_src]
        del circuits[loc_src]

ans = input[p][0] * input[q][0]

print("Answer B:", ans)
t_b = dt.now()

sp.run("pbcopy", input=str(ans), text=True)

print(t_0, t_a, t_b, sep="\n")
