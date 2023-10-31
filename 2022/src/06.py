#!/usr/bin/env python3
import os
import subprocess as sp
import sys

ans = None
input_path = "../input/" + __file__.replace('py', 'txt')
with open(input_path, "r") as f:
    input = [line.rstrip() for line in f]

# part a
sum = 0
total_size = 0
size_stack = []
name_stack = []
dir_sizes = {}
for line in input:
    tokens = line.split(" ")
    if tokens[0] == "$":
        if tokens[1] == "cd":
            if tokens[2] == "..":
                size = size_stack.pop()
                sum += size if size <= 100000 else 0
                size_stack[-1] += size
                dir_sizes[name_stack.pop()] = size
            else:
                size_stack.append(0)
                name_stack.append(tokens[2])
    elif tokens[0] != "dir":
        size_stack[-1] += int(tokens[0])
        total_size += int(tokens[0])
while size_stack:
    size = size_stack.pop()
    sum += size if size <= 100000 else 0
    if size_stack:
        size_stack[-1] += size

ans = sum
print("Answer A:", ans)
# part b
needed = 30000000 - (70000000 - total_size)
min_size = total_size
for _, v in dir_sizes.items():
    min_size = min(v, min_size) if v > needed else min_size

ans = min_size
print("Answer B:", ans)
sp.run("pbcopy", input=str(ans), text=True)
