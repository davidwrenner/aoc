#!/usr/bin/env python3
import os
import subprocess as sp
import sys
import numpy as np
import re

ans = None
input_path = "../input/" + (__file__.replace('py', 'txt') if "-t" not in sys.argv else "testcase.txt")

with open(input_path, "r") as f:
    input = [line.rstrip().split(":")[1] for line in f]

# part 
total = 0
for game in input:
    winning, possessed = game.split("|")
    winning = set(winning.split())
    possessed = set(possessed.split())
    intersection = winning.intersection(possessed)
    score = 0
    if intersection:
        score = 1 << len(intersection)-1;
    total += score

ans = total
print("Answer A:", ans)

# part b
total = 0
cards = [1]*len(input)
for i, game in enumerate(input):
    winning, possessed = game.split("|")
    winning = set(winning.split())
    possessed = set(possessed.split())
    intersection = winning.intersection(possessed)
    for j in range(len(intersection)):
        cards[i+j+1] += cards[i]

ans = sum(cards)
print("Answer B:", ans)
sp.run("pbcopy", input=str(ans), text=True)
