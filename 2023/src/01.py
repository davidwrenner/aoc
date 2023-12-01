#!/usr/bin/env python3
import os
import subprocess as sp
import sys
from numpy import inf

ans = None
input_path = "../input/" + __file__.replace('py', 'txt')

with open(input_path, "r") as f:
    input = [line.rstrip() for line in f]

# part a
sum = 0
for line in input:
    val = ""
    for char in line:
        if char.isdigit():
            val += char
            break
    for char in line[::-1]:
        if char.isdigit():
            val += char
            break
    sum += int(val)

ans = sum
print("Answer A:", ans)

# part b
spelled = {
    "zero" :    "0",
    "one" :     "1",
    "two" :     "2",
    "three" :   "3",
    "four" :    "4",
    "five" :    "5",
    "six" :     "6",
    "seven" :   "7",
    "eight" :   "8",
    "nine" :    "9"
}

sum = 0
for line in input:
    val = ""
    double_break_flag = False
    for i, char in enumerate(line):
        for s in spelled:
            if s == line[i : i+len(s)]:
                val += str(spelled[s])
                double_break_flag = True
                break
        if double_break_flag:
            break
        if char.isdigit():
            val += char
            break

    double_break_flag = False
    for i, char in enumerate(line[::-1]):
        for s in spelled:
            if s == line[len(line)-len(s)-i : len(line)-i]:
                val += str(spelled[s])
                double_break_flag = True
                break
        if double_break_flag:
            break
        if char.isdigit():
            val += char
            break
    sum += int(val)

ans = sum
print("Answer B:", ans)
sp.run("pbcopy", input=str(ans), text=True)
