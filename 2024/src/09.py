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
    input = list([line.rstrip() for line in f][0])

# part a
compacted = []
checksum = 0

for i, block in enumerate(input):
    if i % 2 == 0:
        for j in range(int(block)):
            compacted.append(i//2)
    else:
        for j in range(int(block)):
            compacted.append(None)

b = len(compacted) - 1
for i, block in enumerate(compacted):
    if block is not None:
        continue
    while compacted[b] is None:
        b -= 1
    if i >= b:
        break
    compacted[i], compacted[b] = compacted[b], compacted[i]

for i, block in enumerate(compacted[:b+1]):
    checksum += i * block

ans = checksum
print("Answer A:", ans)
t_a = dt.now()

# part b - slow brute force
compacted = []
checksum = 0

for i, block in enumerate(input):
    if i % 2 == 0:
        for j in range(int(block)):
            compacted.append(i//2)
    else:
        for j in range(int(block)):
            compacted.append(None)

be = len(compacted) - 1
bs = be
i = 0
while bs > 0:
    if compacted[i] is not None:
        i += 1
        continue
    while compacted[be] is None:
        be -= 1
    bs = be
    while compacted[bs-1] == compacted[bs]:
        bs -= 1
    n = be-bs+1
    l = i
    while l < bs:
        if all([compacted[k] is None for k in range(l, l+n)]):
            for j in range(n):
                compacted[l+j], compacted[bs+j] = compacted[bs+j], compacted[l+j]
            i += n
            break
        l += 1
    be = bs-1
    i = 0

for i, block in enumerate(compacted):
    if block is not None:
        checksum += i * block

ans = checksum
print("Answer B:", ans)
t_b = dt.now()

sp.run("pbcopy", input=str(ans), text=True)

print(t_0, t_a, t_b, sep="\n")
