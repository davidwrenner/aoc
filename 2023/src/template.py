#!/usr/bin/env python3
import os
import subprocess as sp
import sys
import numpy as np
import re
from datetime import datetime

print("Run started at", datetime.now())
ans = None
input_path = "../input/" + (__file__.replace('py', 'txt') if "-t" not in sys.argv else "testcase.txt")

with open(input_path, "r") as f:
    input = [line.rstrip() for line in f]

# part a

print("Answer A:", ans)
timestamp_a = datetime.now()

# part b

print("Answer B:", ans)
timestamp_b = datetime.now()

sp.run("pbcopy", input=str(ans), text=True)

print(timestamp_a)
print(timestamp_b)
