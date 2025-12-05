#!/usr/bin/env python3
import subprocess as sp
import sys
from datetime import datetime as dt

t_0 = dt.now()
ans = None
fp = "../input/" + (__file__.replace('py', 'txt') if "-t" not in sys.argv else "small.txt")

with open(fp, "r") as f:
    input = [line.rstrip() for line in f]

# part a
accessible = 0

def check_sq(i, j) -> bool:
    return 0 <= i < len(input) and 0 <= j < len(input[0]) and input[i][j] == "@"

def check_adj(i, j) -> int:
    eight_adj = [
        (i-1, j-1),
        (i, j-1),
        (i+1, j-1),
        (i+1, j),
        (i+1, j+1),
        (i, j+1),
        (i-1, j+1),
        (i-1, j)
    ]
    return 1 if sum(check_sq(y, x) for y, x in eight_adj) < 4 else 0

for i in range(len(input)):
    for j in range(len(input[0])):
        if input[i][j] == "@":
            accessible += check_adj(i, j)

ans = accessible

print("Answer A:", ans)
t_a = dt.now()

# part b
accessible = 0
removable = []

def check_sq(i, j) -> bool:
    return 0 <= i < len(input) and 0 <= j < len(input[0]) and input[i][j] == "@"

def check_adj(i, j) -> int:
    eight_adj = [
        (i-1, j-1),
        (i, j-1),
        (i+1, j-1),
        (i+1, j),
        (i+1, j+1),
        (i, j+1),
        (i-1, j+1),
        (i-1, j)
    ]
    return 1 if sum(check_sq(y, x) for y, x in eight_adj) < 4 else 0

while True:
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == "@" and check_adj(i, j) == 1:
                removable.append((i, j))

    if not removable:
        break

    for i, j in removable:
        input[i] = input[i][:j] + "." + input[i][j+1:]
        accessible += 1
    removable.clear()

ans = accessible

print("Answer B:", ans)
t_b = dt.now()

sp.run("pbcopy", input=str(ans), text=True)

print(t_0, t_a, t_b, sep="\n")
