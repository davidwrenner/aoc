import sys
import os

# file I/O
input_file = sys.argv[0][0:2] + ".txt"
input_path = "../input/" + input_file

if not os.path.exists(input_path):
    sys.exit(f"Did not find expected input {input_path}")

with open(input_path, "r") as f:
    input = [line.rstrip() for line in f]

ans = None
# part a
elf = 0
elves = []
for line in input:
    if line == "":
        elves.append(elf)
        elf = 0
    else:
        elf += int(line)
ans = max(elves)
print("Answer A:", ans)

# part b
elves.sort()
ans = sum(elves[-3:])

print("Answer B:", ans)
