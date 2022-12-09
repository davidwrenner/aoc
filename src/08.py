#!/usr/bin/env python3
import os
import subprocess as sp
import sys
from numpy import sign

ans = None
input_path = "../input/" + __file__.replace('py', 'txt')
with open(input_path, "r") as f:
    input = [line.rstrip() for line in f]

# part a
hx, hy, tx, ty, hx_prev, hy_prev = 0, 0, 0, 0, 0, 0
visited = set()
for line in input:
    dir, amount = line.split(" ")
    for _ in range(int(amount)):
        hx_prev, hy_prev = hx, hy
        if dir == "U":
            hy += 1
        elif dir == "D":
            hy -= 1
        elif dir == "R":
            hx += 1
        elif dir == "L":
            hx -= 1
        if abs(hx - tx) > 1 or abs(hy - ty) > 1:
            tx, ty = hx_prev, hy_prev
        if not (tx, ty) in visited:
            visited.add((tx, ty))
ans = len(visited)
print("Answer A:", ans)

# part b

print("Answer B:", ans)
sp.run("pbcopy", input=str(ans), text=True)
