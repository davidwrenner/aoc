#!/usr/bin/env python3
import os
import subprocess as sp
import sys

ans = None
input_path = "../input/" + __file__.replace('py', 'txt')
# input_path = "../input/small.txt"
with open(input_path, "r") as f:
    input = [line.rstrip().split(" ") for line in f if line != "\n"]

# NOTE: requires preprocessed input

# part a
rounds = 20
monkeys = 8
counts = [0 for _ in range(monkeys)]
for _ in range(rounds):
    for i in range(monkeys):
        monkey_items = [int(m) for m in input[i * 5]]
        ops = input[i * 5 + 1]
        worry_test = int(input[i * 5 + 2][0])
        true_dest = int(input[i * 5 + 3][0])
        false_dest = int(input[i * 5 + 4][0])
        for worry_level in monkey_items:
            counts[i] += 1
            if ops[0] == "*":
                if ops[1] == "old":
                    new_level = worry_level * worry_level
                else:
                    new_level = worry_level * int(ops[1])
            elif ops[0] == "+":
                if ops[1] == "old":
                    new_level = worry_level + worry_level
                else:
                    new_level = worry_level + int(ops[1])
            new_level = new_level // 3
            if new_level % worry_test == 0:
                input[true_dest * 5].append(new_level)
            else:
                input[false_dest * 5].append(new_level)
        input[i * 5].clear()

counts.sort()
ans = counts[-1] * counts[-2]
print("Answer A:", ans)

# part b
counts = [0 for _ in range(monkeys)]
rounds = 10000
lcm = 1
for i in range(monkeys):
    lcm *= int(input[i*5+2][0])

for _ in range(rounds):
    for i in range(monkeys):
        monkey_items = [int(m) for m in input[i * 5]]
        ops = input[i * 5 + 1]
        worry_test = int(input[i * 5 + 2][0])
        true_dest = int(input[i * 5 + 3][0])
        false_dest = int(input[i * 5 + 4][0])
        for worry_level in monkey_items:
            counts[i] += 1
            if ops[0] == "*":
                if ops[1] == "old":
                    new_level = worry_level * worry_level
                else:
                    new_level = worry_level * int(ops[1])
            elif ops[0] == "+":
                if ops[1] == "old":
                    new_level = worry_level + worry_level
                else:
                    new_level = worry_level + int(ops[1])
            new_level = new_level % lcm
            if new_level % worry_test == 0:
                input[true_dest * 5].append(new_level)
            else:
                input[false_dest * 5].append(new_level)
        input[i * 5].clear()
counts.sort()
ans = counts[-1] * counts[-2]
print("Answer B:", ans)
sp.run("pbcopy", input=str(ans), text=True)
