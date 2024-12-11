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
trailheads = find_all_char_in_list_strs(input, "0")

def search(arr, loc):
    if input[loc[0]][loc[1]] == "9":
        return [loc]
    
    L = (loc[0], loc[1]-1)
    R = (loc[0], loc[1]+1)
    U = (loc[0]+1, loc[1])
    D = (loc[0]-1, loc[1])
    peaks = []

    for new_loc in [L, R, U, D]:
        if not is_loc_in_2d_grid(arr, new_loc):
            continue
        if int(input[new_loc[0]][new_loc[1]]) - int(input[loc[0]][loc[1]]) == 1:
            peaks += search(arr, new_loc)

    return peaks

ans = sum([len(set(search(input, t))) for t in trailheads])
print("Answer A:", ans)
t_a = dt.now()

ans = sum([len(search(input, t)) for t in trailheads])
print("Answer B:", ans)
t_b = dt.now()

sp.run("pbcopy", input=str(ans), text=True)

print(t_0, t_a, t_b, sep="\n")
