#!/usr/bin/env python3
import os
import subprocess as sp
import sys
from collections import deque
from numpy import inf

ans = None
input_path = "../input/" + __file__.replace('py', 'txt')
with open(input_path, "r") as f:
    input = [list(line.rstrip()) for line in f][::-1]


def find_coords(loc):
    for i, _ in enumerate(input):
        for j, _ in enumerate(input[0]):
            if input[i][j] == loc:
                input[i][j] = ("a" if loc == "S" else "z")
                return i, j


def loc_to_letter(loc):
    return input[loc[0]][loc[1]]


def do_bfs(start, end):
    steps = 0
    bfs_queue = deque()
    bfs_queue.appendleft(start)
    seen = {start: steps}

    while len(bfs_queue) > 0:
        curr_loc = bfs_queue.pop()
        curr_letter = loc_to_letter(curr_loc)
        l = (curr_loc[0] - 1, curr_loc[1])
        r = (curr_loc[0] + 1, curr_loc[1])
        u = (curr_loc[0], curr_loc[1] + 1)
        d = (curr_loc[0], curr_loc[1] - 1)
        for adj_loc in [l, r, u, d]:
            if not (adj_loc[0] in range(0, len(input)) and adj_loc[1] in range(0, len(input[0]))):
                continue
            if adj_loc in seen:
                continue
            if ord(loc_to_letter(adj_loc)) - ord(curr_letter) <= 1:
                bfs_queue.appendleft(adj_loc)
                seen[adj_loc] = seen[curr_loc] + 1
        steps += 1
    return seen[end] if end in seen else inf


# note we don't need a case for "S" since the input should be processed by the time
# this function is called
def find_all_a():
    a_list = []
    for i, _ in enumerate(input):
        for j, _ in enumerate(input[0]):
            if input[i][j] == "a":
                a_list.append((i,j))
    return a_list


# part a
start = find_coords("S")
end = find_coords("E")
ans = do_bfs(start, end)
print("Answer A:", ans)

# part b - slow, should probably use DP
ans = min(do_bfs(s, end) for s in find_all_a())
print("Answer B:", ans)
sp.run("pbcopy", input=str(ans), text=True)
