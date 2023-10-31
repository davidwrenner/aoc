#!/usr/bin/env python3
import os
import subprocess as sp
import sys

ans = None
input_path = "../input/" + __file__.replace('py', 'txt')
with open(input_path, "r") as f:
    input = [line.rstrip() for line in f]


def is_visible(row, col, height):
    if all([height > input[row][i] for i in range(col)]):
        return True
    if all([height > input[row][i] for i in range(col+1, len(input[0]))]):
        return True
    if all([height > input[i][col] for i in range(row)]):
        return True
    if all([height > input[i][col] for i in range(row+1, len(input))]):
        return True
    return False


def calculate_score(row, col, height):
    a, b, c, d = 0,0,0,0
    for i in range(col-1, -1, -1):
        a += 1
        if input[row][i] >= height:
            break
    for i in range(col+1, len(input[0])):
        b += 1
        if input[row][i] >= height:
            break
    for i in range(row-1, -1, -1):
        c += 1
        if input[i][col] >= height:
            break
    for i in range(row+1, len(input)):
        d += 1
        if input[i][col] >= height:
            break
    return a*b*c*d



# part a
count_visible = 0
for i, row in enumerate(input):
    for j, height in enumerate(row):
        count_visible += 1 if is_visible(i, j, height) else 0
ans = count_visible
print("Answer A:", ans)

# part b
scores = []
for i, row in enumerate(input):
    for j, height in enumerate(row):
        scores.append(calculate_score(i, j, height))
ans = max(scores)
print("Answer B:", ans)
sp.run("pbcopy", input=str(ans), text=True)
