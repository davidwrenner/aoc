#!/usr/bin/env python3
import os
import subprocess as sp
import sys
import numpy as np
import re

ans = None
input_path = "../input/" + (__file__.replace('py', 'txt') if "-t" not in sys.argv else "testcase.txt")

with open(input_path, "r") as f:
    input = [line.rstrip() for line in f]

vectors = [(1, 0), # south
           (0, 1), # east
           (-1, 0), # north
           (0, -1)] # west
mappings = {
    "S": vectors,
    "|": [vectors[0], vectors[2]],
    "-": [vectors[1], vectors[3]],
    "L": [vectors[1], vectors[2]],
    "J": [vectors[2], vectors[3]],
    "7": [vectors[0], vectors[3]],
    "F": [vectors[0], vectors[1]],
    ".": []
}

def find_S():
    for i, line in enumerate(input):
        j = line.find("S")
        if j > -1:
            return i, j

# part a
visited = set()
S = find_S()

def search(node):
    candidates = mappings[input[node[0]][node[1]]]
    for dir in candidates:
        _i, _j = np.add(node, dir)
        if not (0<=_i<len(input) and 0<=_j<len(input[0])):
            continue
        c = input[_i][_j]
        if not mappings[c]:
            continue
        # check if candidate pipe is compatible with current node
        for d in mappings[c]:
            _node = np.add((_i, _j), d)
            if all([a==b for a, b in zip(_node, node)]):
                if (_i, _j) not in visited:
                    return (_i, _j)


curr = search(S)
dist = 1 # repr dist from S to S in pipe
while curr != S:
    visited.add(curr)
    curr = search(curr)
    dist += 1

ans = dist // 2
print("Answer A:", ans)

# part b
visited.add(S)
ignore = ["7", "F", "-", "S"]
# including S leads to correct or off by +1 based on what piece S functions as

def search(i, j):
    inside = False
    for x in range(j+1):
        if (i, x) in visited and input[i][x] not in ignore:
            inside = not inside
    return 1 if inside else 0

sum = 0
for i, line in enumerate(input):
    for j, c in enumerate(line):
        if (i, j) not in visited:
            sum += search(i, j)

ans = sum
print("Answer B:", ans)
sp.run("pbcopy", input=str(ans), text=True)
