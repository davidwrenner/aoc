#!/usr/bin/env python3
import os
import subprocess as sp
import sys
from numpy import sign

ans = None
# input_path = "../input/" + __file__.replace('py', 'txt')
input_path = "../input/small.txt"
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
visited = set()
moves = 0
rope = [(0, 0) for _ in range(10)]
for line in input:
    dir, amount = line.split(" ")
    for _ in range(int(amount)):
        x, y = rope[0]
        # move head
        if dir == "U":
            rope[0] = (x, y+1)
        elif dir == "D":
            rope[0] = (x, y-1)
        elif dir == "R":
            rope[0] = (x+1, y)
        elif dir == "L":
            rope[0] = (x-1, y)
        # move knots following head
        moves += 1
        i = 0
        for i, _ in enumerate(rope):
            if i == 0:
                continue
            xdiff = rope[i-1][0] - rope[i][0]
            ydiff = rope[i-1][1] - rope[i][1]
            if abs(xdiff) > 1 and abs(ydiff) > 0:
                rope[i] = (rope[i][0] + sign(xdiff) * (abs(xdiff)-1), rope[i][1] + ydiff)
            elif abs(xdiff) > 0 and abs(ydiff) > 1:
                rope[i] = (rope[i][0] + xdiff, rope[i][1] + sign(ydiff) * (abs(ydiff)-1))
            elif abs(xdiff) > 1:
                rope[i] = (rope[i][0] + sign(xdiff) * (abs(xdiff)-1), rope[i][1])
            elif abs(ydiff) > 1:
                rope[i] = (rope[i][0], rope[i][1] + sign(ydiff) * (abs(ydiff)-1))
        if not rope[-1] in visited:
            visited.add(rope[-1])
            print(rope[-1])

ans = len(visited)
print("Answer B:", ans)
sp.run("pbcopy", input=str(ans), text=True)
