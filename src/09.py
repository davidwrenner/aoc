#!/usr/bin/env python3
import os
import subprocess as sp
import sys

ans = None
input_path = "../input/" + __file__.replace('py', 'txt')
with open(input_path, "r") as f:
    input = [line.rstrip() for line in f]

# part a
x = 1
cycles_complete = 0
sum = 0
print(".", end="")
for instruction in input:
    if instruction == "noop":
        cycles_complete += 1
    else:
        _, dx = instruction.split(" ")
        dx = int(dx)
        cycles_complete += 1
        if cycles_complete % 40 == 20:
            sum += x * cycles_complete
        elif cycles_complete % 40 == 0:
            print()
        print("#", end="") if cycles_complete % 40 in range(x-1, x+2) else print(".", end="")
        cycles_complete += 1
        x += dx
    if cycles_complete % 40 == 20:
        sum += x * cycles_complete
    elif cycles_complete % 40 == 0:
        print()
    print("#", end="") if cycles_complete % 40 in range(x - 1, x + 2) else print(".", end="")
ans = sum
print("Answer A:", ans)
# Part B answer = PLULKBZH
"""
.##..#....#..#.#....#..#.###..####.#..#.
#..#.#....#..#.#....#.#..#..#....#.#..#.
#..#.#....#..#.#....##...###....#..####.
###..#....#..#.#....#.#..#..#..#...#..#.
#....#....#..#.#....#.#..#..#.#....#..#.
#....####..##..####.#..#.###..####.#..#.
"""