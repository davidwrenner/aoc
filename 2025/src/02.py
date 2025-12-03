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
sum = 0

for r in input[0].split(","):
    l, h = r.split("-")
    for i in range(int(l), int(h)+1):
        s = str(i)
        if len(s) % 2 == 0 and s.endswith(s[:len(s)//2]):
            sum += i

ans = sum

print("Answer A:", ans)
t_a = dt.now()

# part b
sum = 0

for r in input[0].split(","):
    l, h = r.split("-")
    for i in range(int(l), int(h)+1):
        s = str(i)
        for candidate_window_size in range(1, len(s)//2+1):
            if len(s) % candidate_window_size == 0 and str(s[:candidate_window_size]) * (len(s) // candidate_window_size) == s:
                sum += i
                break

ans = sum

print("Answer B:", ans)
t_b = dt.now()

sp.run("pbcopy", input=str(ans), text=True)

print(t_0, t_a, t_b, sep="\n")
