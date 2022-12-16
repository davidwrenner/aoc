#!/usr/bin/env python3
import os
import subprocess as sp
import sys
from numpy import inf, sign

ans = None
input_path = "../input/" + __file__.replace('py', 'txt')
with open(input_path, "r") as f:
    input = [line.rstrip().split(" -> ") for line in f]

min_x = 0
min_y = 0
max_x = 1000
max_y = 1000


def process_lines():
    lines = []
    for line in input:
        lines.append([])
        for coordinate in line:
            c = coordinate.split(",")
            lines[-1].append((int(c[0]), int(c[1])))
    return lines


def initialize_grid(lines):
    grid = [list() for _ in range(max_x+1)]
    for row in grid:
        for _ in range(max_y+1):
            row.append(".")
    for line in lines:
        for i, _ in enumerate(line):
            if i == 0:
                continue
            curr = line[i]
            prev = line[i-1]
            if curr[0] == prev[0]:  # vertical line
                while prev != curr:
                    grid[prev[0]][prev[1]] = "#"
                    prev = (prev[0], prev[1] + sign(curr[1]-prev[1]))
            else:  # horizontal line
                while prev != curr:
                    grid[prev[0]][prev[1]] = "#"
                    prev = (prev[0] + sign(curr[0]-prev[0])*1, prev[1])
            grid[curr[0]][curr[1]] = "#"
    return grid


def next_move(grid, loc):
    if grid[loc[0]][loc[1]+1] == ".":
        return loc[0], loc[1] + 1
    elif grid[loc[0]-1][loc[1]+1] == ".":
        return loc[0] - 1, loc[1]
    elif grid[loc[0]+1][loc[1]+1] == ".":
        return loc[0] + 1, loc[1] + 1
    return inf, inf


def simulate_round(grid):
    loc = (500, 0)
    is_abyss = False
    next = next_move(grid, loc)
    can_move = (next != (inf, inf))
    while can_move and not is_abyss:
        next = next_move(grid, loc)
        can_move = (next != (inf, inf))
        if can_move and next[1] >= max_y:
            return grid, True
        if can_move:
            loc = next
    grid[loc[0]][loc[1]] = "o"
    return grid, is_abyss

# part a
lines = process_lines()
grid = initialize_grid(lines)
is_flowing_into_abyss = False
num_sand = 0

while not is_flowing_into_abyss:
    grid, is_flowing_into_abyss = simulate_round(grid)
    if not is_flowing_into_abyss:
        num_sand += 1
ans = num_sand
print("Answer A:", ans)

# part b
def initialize_grid_b(lines):
    grid = [list() for _ in range(max_x+1)]
    for row in grid:
        for _ in range(max_y+1):
            row.append(".")
    for line in lines:
        for i, _ in enumerate(line):
            if i == 0:
                continue
            curr = line[i]
            prev = line[i-1]
            if curr[0] == prev[0]:  # vertical line
                while prev != curr:
                    grid[prev[0]][prev[1]] = "#"
                    prev = (prev[0], prev[1] + sign(curr[1]-prev[1]))
            else:  # horizontal line
                while prev != curr:
                    grid[prev[0]][prev[1]] = "#"
                    prev = (prev[0] + sign(curr[0]-prev[0])*1, prev[1])
            grid[curr[0]][curr[1]] = "#"
    for x in range(min_x, max_x+1):
        grid[x][max_y] = "#"
    return grid


def simulate_round_b(grid):
    origin = (500, 0)
    loc = (500, 0)
    is_origin = False
    next = next_move(grid, loc)
    can_move = (next != (inf, inf))
    while can_move and not is_origin:
        next = next_move(grid, loc)
        can_move = (next != (inf, inf))
        if can_move:
            loc = next
    grid[loc[0]][loc[1]] = "o"
    if loc == origin:
        is_origin = True
    return grid, is_origin


max_y = -inf
for line in lines:
    for coord in line:
        max_y = max(max_y, coord[1])
max_y += 2
lines = process_lines()
grid = initialize_grid_b(lines)
is_at_origin = False
num_sand = 0

while not is_at_origin:
    grid, is_at_origin = simulate_round_b(grid)
    if not is_at_origin:
        num_sand += 1

ans = num_sand + 1
print("Answer B:", ans)
sp.run("pbcopy", input=str(ans), text=True)
