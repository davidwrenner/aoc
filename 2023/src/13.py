#!/usr/bin/env python3
import os
import subprocess as sp
import sys
import numpy as np
import re
from datetime import datetime

print("Run started at", datetime.now())
ans = None
input_path = "../input/" + (__file__.replace('py', 'txt') if "-t" not in sys.argv else "testcase.txt")

with open(input_path, "r") as f:
    input = f.read().split("\n\n")

# part a
def transpose(arr):
    return ["".join(c) for c in [list(i) for i in zip(*arr)]]

def reflection_rows(p):
    rows = [0]
    for r in range(1, len(p)):
        if p[r-1] == p[r]:
            i = r-1
            j = r
            is_true_reflection = True
            while i >= 0 and j < len(p):
                if p[i] != p[j]:
                    is_true_reflection = False
                    break
                i -= 1
                j += 1
            if is_true_reflection:
                rows.append(r)
    return rows

sum = 0
og_reflections = {}
for i, pattern in enumerate(input):
    pattern = pattern.rstrip().split("\n")
    row = reflection_rows(pattern)[-1]
    col = reflection_rows(transpose(pattern))[-1]
    og_reflections[i] = (row, col)
    sum += 100*row + col
    
ans = sum
print("Answer A:", ans)
timestamp_a = datetime.now()

# part b
def smudge(p, i, j):
    if p[i][j] == ".":
        p[i] = p[i][:j] + "#" + p[i][j+1:]
    elif p[i][j] == "#":
        p[i] = p[i][:j] + "." + p[i][j+1:]
    return p

def unsmudge(p, i, j):
    return smudge(p, i, j)

def compute(pattern, og):
    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            pattern = smudge(pattern, i, j)
            rows = reflection_rows(pattern)
            cols = reflection_rows(transpose(pattern))
            row = rows[0]
            col = cols[0]
            a = 0
            while a < len(rows) and (row == 0 or row == og[0]):
                row = rows[a]
                a += 1
            b = 0
            while b < len(cols) and (col == 0 or col == og[1]):
                col = cols[b]
                b += 1
            pattern = unsmudge(pattern, i, j)
            if any((row, col)) and (row, col) != og:
                if row == og[0]:
                    return col
                elif col == og[1]:
                    return row*100


sum = 0
for k, pattern in enumerate(input):
    pattern = pattern.rstrip().split("\n")
    sum += compute(pattern, og_reflections[k])

ans = sum
print("Answer B:", ans)
timestamp_b = datetime.now()

sp.run("pbcopy", input=str(ans), text=True)

print(timestamp_a)
print(timestamp_b)
