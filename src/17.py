#!/usr/bin/env python3
import os
import subprocess as sp
import sys
from numpy import inf

ans = None
input_path = "../input/" + __file__.replace('py', 'txt')
with open(input_path, "r") as f:
    input = [line.rstrip() for line in f]

points = []
for line in input:
    str_point = line.split(",")
    points.append(tuple(int(x) for x in str_point))

points = set(points)
adjacent = [
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1)
]

# part a
surfaces = 0
for point in points:
    for adj in adjacent:
        if tuple(sum(x) for x in zip(point, adj)) not in points:
            surfaces += 1

ans = surfaces
print("Answer A:", ans)

# part b
min_point = (min(points, key=lambda p: p[0])[0]-1,
             min(points, key=lambda p: p[1])[1]-1,
             min(points, key=lambda p: p[2])[2]-1)
max_point = (max(points, key=lambda p: p[0])[0]+1,
             max(points, key=lambda p: p[1])[1]+1,
             max(points, key=lambda p: p[2])[2]+1)


def is_in_range(pt):
    return False if any(pt[i] not in range(min_point[i], max_point[i]+1) for i in range(3)) else True


# DFS all space accessible around lava, then count those next to a cube
dfs_stack = [min_point]
visited = set()
while dfs_stack:
    pt = dfs_stack.pop()
    if pt in visited or pt in points:
        continue
    if is_in_range(pt):
        visited.add(pt)
        for adj in adjacent:
            dfs_stack.append(tuple(sum(x) for x in zip(pt, adj)))

count = 0
for point in points:
    for adj in adjacent:
        if tuple(sum(x) for x in zip(point, adj)) in visited:
            count += 1

ans = count
print("Answer B:", ans)
sp.run("pbcopy", input=str(ans), text=True)
