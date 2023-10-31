#!/usr/bin/env python3
import os
import subprocess as sp
import sys
from numpy import inf

ans = None
input_path = "../input/" + __file__.replace('py', 'txt')
input_path = "../input/small.txt"
with open(input_path, "r") as f:
    input = [line.rstrip() for line in f]
# NOTE: modified input used for this solution
# i.e. 2899860, 3122031, 2701269, 3542780...

# part a

print("Answer A:", ans)

# part b

print("Answer B:", ans)
sp.run("pbcopy", input=str(ans), text=True)
