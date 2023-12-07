#!/usr/bin/env python3
import os
import subprocess as sp
import sys
import re
import datetime

ans = None
input_path = "../input/" + (__file__.replace('py', 'txt') if "-t" not in sys.argv else "testcase.txt")

digits = re.compile("\d+")
with open(input_path, "r") as f:
    input = [line.rstrip() for line in f]

# part a
locations = []
seeds = digits.findall(input[0])
for seed in seeds:
    value = int(seed)
    mapped_value = value
    for i in range(1, len(input)):
        line = input[i]
        if not line:
            value = mapped_value
            continue
        if value != mapped_value:
            continue
        mapping = digits.findall(line)
        if not mapping:
            continue
        dst, src, length = [int(x) for x in mapping]
        mapped_value = value
        mapping_range = range(src, src+length)
        if value in mapping_range:
            mapped_value = dst + mapping_range.index(value)
    locations.append(mapped_value)
    
ans = min(locations)
print("Answer A:", ans)

# part b
# atrocious runtime but it worked
print(datetime.datetime.now())
seed_ranges = [range(int(x), int(x)+int(seeds[i+1])) 
               for i, x in enumerate(seeds) if i % 2 == 0]
seed_ranges.sort(key=lambda r: r.start)

flag = False
for loc in range(seed_ranges[-1].start+seed_ranges[-1][1]):
    if flag:
        break
    value = loc
    mapped_value = value
    for i in range(len(input)-1, 0, -1):
        line = input[i]
        if not line:
            value = mapped_value
            continue
        if value != mapped_value:
            continue
        mapping = digits.findall(line)
        if not mapping:
            continue
        src, dst, length = [int(x) for x in mapping]
        mapped_value = value
        if src <= value < src+length:
            mapped_value = dst + value - src
    for r in seed_ranges:
        if mapped_value in r:
            ans = loc
            flag = True
            break

print("Answer B:", ans)
sp.run("pbcopy", input=str(ans), text=True)
