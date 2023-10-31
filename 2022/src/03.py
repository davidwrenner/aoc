import sys
import os
import re

# file I/O
input_file = sys.argv[0][0:2] + ".txt"
input_path = "../input/" + input_file

if not os.path.exists(input_path):
    raise FileNotFoundError(f"Did not find expected input {input_path}")

with open(input_path, "r") as f:
    input = [line.rstrip() for line in f if line != "\n"]

input_re = re.compile(r"^(?P<elf1_begin>[\d]+)-(?P<elf1_end>[\d]+),(?P<elf2_begin>[\d]+)-(?P<elf2_end>[\d]+)$")


def val(match, group_name):
    return int(match.group(group_name))


ans = None
# part a
count_fully_contained = 0
for pairing in input:
    m = input_re.match(pairing)
    if val(m, "elf1_begin") <= val(m, "elf2_begin") and val(m, "elf1_end") >= val(m, "elf2_end"):
        count_fully_contained += 1
    elif val(m, "elf2_begin") <= val(m, "elf1_begin") and val(m, "elf2_end") >= val(m, "elf1_end"):
        count_fully_contained += 1

ans = count_fully_contained
print("Answer A:", ans)

# part b
count_overlapping = 0
for pairing in input:
    m = input_re.match(pairing)
    if val(m, "elf2_begin") in range(val(m, "elf1_begin"), val(m, "elf1_end")+1):
        count_overlapping += 1
    elif val(m, "elf1_begin") in range(val(m, "elf2_begin"), val(m, "elf2_end")+1):
        count_overlapping += 1

ans = count_overlapping
print("Answer B:", ans)
