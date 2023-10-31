#!/usr/bin/env python3
import os
import subprocess as sp
import sys
from numpy import inf
from ast import literal_eval
from functools import cmp_to_key

ans = None
input_path = "../input/" + __file__.replace('py', 'txt')
with open(input_path, "r") as f:
    input = [line.rstrip() for line in f]


def compare(v1, v2) -> int:
    if isinstance(v1, int) and isinstance(v2, int):
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        else:
            return 0
    elif isinstance(v1, list) and isinstance(v2, list):
        i, j = 0, 0
        while i < len(v1) and j < len(v2):
            cmp = compare(v1[i], v2[j])
            if cmp == 1:
                return 1
            elif cmp == -1:
                return -1
            i += 1
            j += 1
        if i == len(v1) and j < len(v2):
            return -1
        elif j == len(v2) and i < len(v1):
            return 1
        else:
            return 0
    elif isinstance(v1, int):
        return compare([v1], v2)
    else:
        return compare(v1, [v2])


# part a
pairs = [(literal_eval(input[l]), literal_eval(input[l+1])) for l in range(0, len(input), 3)]
correct = [i+1 for i, pair in enumerate(pairs) if compare(*pair) == -1]
ans = sum(correct)
print("Answer A:", ans)

# part b
packets = [literal_eval(line) for line in input if len(line) > 0]
d1 = [[2]]
d2 = [[6]]
packets.append(d1)
packets.append(d2)
packets.sort(key=cmp_to_key(compare))
ans = (packets.index(d1)+1) * (packets.index(d2)+1)
print("Answer B:", ans)
sp.run("pbcopy", input=str(ans), text=True)
