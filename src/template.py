#!/usr/bin/env python3
import os
import subprocess as sp
import sys

ans = None
input_path = "../input/" + __file__.replace('py', 'txt')
with open(input_path, "r") as f:
    input = [line.rstrip() for line in f]

# part a

print("Answer A:", ans)

# part b

print("Answer B:", ans)
sp.run("pbcopy", input=str(ans), text=True)
