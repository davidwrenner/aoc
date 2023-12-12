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

# part a
def rows_to_expand(arr):
    empty_rows = []
    for i, line in enumerate(arr):
        if all([c == "." for c in line]):
            empty_rows.append(i)
    return empty_rows

def cols_to_expand(arr):
    arr_T = ["".join(c) for c in [list(i) for i in zip(*arr)]]
    return rows_to_expand(arr_T)

points = set()
for i, line in enumerate(input):
    for j, c in enumerate(line):
        if input[i][j] == "#":
            points.add((i,j))

def manhattan(p1, p2, empty_rows, empty_cols, multiplier):
    num_rows = 0
    for i in empty_rows:
        if p1[0] < i < p2[0] or p1[0] > i > p2[0]:
            num_rows += 1
    num_cols = 0
    for i in empty_cols:
        if p1[1] < i < p2[1] or p1[1] > i > p2[1]:
            num_cols += 1        
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]) + num_cols*(multiplier-1) + num_rows*(multiplier-1)

sum = 0
empty_rows = rows_to_expand(input)
empty_cols = cols_to_expand(input)
for p1 in points:
    for p2 in points:
        sum += manhattan(p1, p2, empty_rows, empty_cols, 2)

ans = sum // 2
print("Answer A:", ans)

# part b
sum = 0
for p1 in points:
    for p2 in points:
        sum += manhattan(p1, p2, empty_rows, empty_cols, 1_000_000)

ans = sum // 2
print("Answer B:", ans)
sp.run("pbcopy", input=str(ans), text=True)
