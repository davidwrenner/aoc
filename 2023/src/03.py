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
directions = [[1,0], [-1,0], [0,1], [0,-1], [1,1], [-1,-1], [1,-1], [-1,1]]
regex = re.compile("\d+")

def is_part(y, pair):
    start, end = pair
    for x in range(start, end):
        for d in directions:
            _y, _x = np.add([y,x],d)
            if _x < 0 or _y < 0 or _x >= len(line) or _y >= len(input):
                continue
            d_val = input[_y][_x]
            if d_val != "." and not d_val.isdigit():
                return True
    return False

sum = 0
for i, line in enumerate(input):
    matches = regex.findall(line)
    indexes = [(m.start(0), m.end(0)) for m in regex.finditer(line)]
    for match_idx, pair in enumerate(indexes):
        if is_part(i, pair):
            sum += int(matches[match_idx])
    
ans = sum
print("Answer A:", ans)

# part b
def gear_loc(y, pair):
    start, end = pair
    for x in range(start, end):
        for d in directions:
            _y, _x = np.add([y,x],d)
            if _x < 0 or _y < 0 or _x >= len(line) or _y >= len(input):
                continue
            d_val = input[_y][_x]
            if d_val != "." and not d_val.isdigit():
                if d_val == "*":
                    return _y, _x

sum = 0
gear_candidates = {}
for i, line in enumerate(input):
    matches = regex.findall(line)
    indexes = [(m.start(0), m.end(0)) for m in regex.finditer(line)]
    for match_idx, pair in enumerate(indexes):
        loc = gear_loc(i, pair)
        if loc:
            if loc in gear_candidates:
                ratio = int(matches[match_idx]) * gear_candidates[loc]
                sum += ratio
            else:
                gear_candidates[loc] = int(matches[match_idx])
            
ans = sum
print("Answer B:", ans)
sp.run("pbcopy", input=str(ans), text=True)
