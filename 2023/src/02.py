#!/usr/bin/env python3
import os
import subprocess as sp
import sys
from numpy import inf, prod
import re

ans = None
input_path = "../input/" + __file__.replace('py', 'txt')

red_re = re.compile("\d+ red")
green_re = re.compile("\d+ green")
blue_re = re.compile("\d+ blue")

with open(input_path, "r") as f:
    input = [line.rstrip().split(":")[1:] for line in f]

# part a
cubes_availible = (12, 13, 14)
sum = 0

for i, line in enumerate(input):
    subsets = line[0].split(";")
    game_is_possible = True
    for subset in subsets:
        red_match = red_re.findall(subset)
        green_match = green_re.findall(subset)
        blue_match = blue_re.findall(subset)
        red_count = int(red_match[0].split(" ")[0]) if red_match else 0
        green_count = int(green_match[0].split(" ")[0]) if green_match else 0
        blue_count = int(blue_match[0].split(" ")[0]) if blue_match else 0
        if any([red_count > cubes_availible[0], green_count > cubes_availible[1], blue_count > cubes_availible[2]]):
            game_is_possible = False
            break
    if game_is_possible:
        sum += i+1

ans = sum
print("Answer A:", ans)

# part b
sum = 0

for i, line in enumerate(input):
    subsets = line[0].split(";")
    min_each_color = [0,0,0]
    for subset in subsets:
        red_match = red_re.findall(subset)
        green_match = green_re.findall(subset)
        blue_match = blue_re.findall(subset)
        red_count = int(red_match[0].split(" ")[0]) if red_match else 0
        green_count = int(green_match[0].split(" ")[0]) if green_match else 0
        blue_count = int(blue_match[0].split(" ")[0]) if blue_match else 0
        min_each_color = [max(red_count, min_each_color[0]), max(green_count, min_each_color[1]), max(blue_count, min_each_color[2])]
    sum += prod(min_each_color)

ans = sum
print("Answer B:", ans)
sp.run("pbcopy", input=str(ans), text=True)
