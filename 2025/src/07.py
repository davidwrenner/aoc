#!/usr/bin/env python3
import subprocess as sp
import sys
from datetime import datetime as dt
from utils import is_loc_in_2d_grid, find_single_char_in_list_strs

t_0 = dt.now()
ans = None
fp = "../input/" + (__file__.replace('py', 'txt') if "-t" not in sys.argv else "small.txt")

with open(fp, "r") as f:
    input = [line.rstrip() for line in f]

# part a
def dfs(loc, visited) -> int:
    if not is_loc_in_2d_grid(input, loc) or loc in visited:
        return 0
    elif input[loc[0]][loc[1]] == "^":
        val = 1 + dfs((loc[0], loc[1] - 1), visited) + dfs((loc[0], loc[1] + 1), visited)
        visited[loc] = val
        return val
    else:
        val = dfs((loc[0] + 1, loc[1]), visited)
        visited[loc] = val
        return val

ans = dfs(find_single_char_in_list_strs(input, "S"), visited={})

print("Answer A:", ans)
t_a = dt.now()

# part b
def dfs(loc, visited) -> int:
    if not is_loc_in_2d_grid(input, loc):
        return 1
    if loc in visited:
        return visited[loc]
    elif input[loc[0]][loc[1]] == "^":
        val = dfs((loc[0], loc[1] - 1), visited) + dfs((loc[0], loc[1] + 1), visited)
        visited[loc] = val
        return val
    else:
        val = dfs((loc[0] + 1, loc[1]), visited)
        visited[loc] = val
        return val

ans = dfs(find_single_char_in_list_strs(input, "S"), visited={})

print("Answer B:", ans)
t_b = dt.now()

sp.run("pbcopy", input=str(ans), text=True)

print(t_0, t_a, t_b, sep="\n")
