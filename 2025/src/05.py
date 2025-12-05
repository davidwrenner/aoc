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
fresh = 0
ranges, available = input[:input.index("")], input[input.index("")+1:]
ranges = [(int(r.split("-")[0]), int(r.split("-")[1])) for r in ranges]

for e in available:
    for start, end in ranges:
        if start <= int(e) <= end:
            fresh += 1
            break

ans = fresh
print("Answer A:", ans)
t_a = dt.now()

# part b
ranges.sort()
merged = []
for r in ranges:
    if not merged or r[0] > merged[-1][1]:
        merged.append(r)
        continue
    merged[-1] = (merged[-1][0], max(r[1], merged[-1][1]))

ans = sum(m[1]-m[0]+1 for m in merged)
print("Answer B:", ans)
t_b = dt.now()

sp.run("pbcopy", input=str(ans), text=True)

print(t_0, t_a, t_b, sep="\n")
