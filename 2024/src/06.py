#!/usr/bin/env python3
import os
import subprocess as sp
import sys
import numpy as np
import re
from datetime import datetime as dt
from utils import *

t_0 = dt.now()
ans = None
fp = "../input/" + (__file__.replace('py', 'txt') if "-t" not in sys.argv else "small.txt")

with open(fp, "r") as f:
    input = [line.rstrip() for line in f]

# part a
locs = set()
dirs = [[-1,0],[0,1],[1,0],[0,-1]]
loc = find_single_char_in_list_strs(input, "^")

d = 0
while is_loc_in_2d_grid(input, loc):
    locs.add((loc[0],loc[1]))
    try_loc = np.add(loc, dirs[d])
    while is_loc_in_2d_grid(input, try_loc) and input[try_loc[0]][try_loc[1]] == "#":
        d = (d + 1) % len(dirs)
        try_loc = np.add(loc, dirs[d])
    loc = try_loc

ans = len(locs)
print("Answer A:", ans)
t_a = dt.now()

# part b
num_obstruction_positions = 0

for i, _ in enumerate(input):
    for j, _ in enumerate(input[0]):
        if input[i][j] == "^" or input[i][j] == "#":
            continue
        input[i] = input[i][:j] + "#" + input[i][j + 1:]
        locs_with_dirs = set()
        loc = find_single_char_in_list_strs(input, "^")
        d = 0
        while is_loc_in_2d_grid(input, loc) and (loc[0],loc[1],dirs[d][0],dirs[d][1]) not in locs_with_dirs:
            locs_with_dirs.add((loc[0],loc[1],dirs[d][0],dirs[d][1]))
            try_loc = np.add(loc, dirs[d])
            while is_loc_in_2d_grid(input, try_loc) and input[try_loc[0]][try_loc[1]] == "#":
                d = (d + 1) % len(dirs)
                try_loc = np.add(loc, dirs[d])
            loc = try_loc
        if is_loc_in_2d_grid(input, loc):
            num_obstruction_positions += 1
        input[i] = input[i][:j] + "." + input[i][j + 1:]

ans = num_obstruction_positions
print("Answer B:", ans)
t_b = dt.now()

sp.run("pbcopy", input=str(ans), text=True)

print(t_0, t_a, t_b, sep="\n")
