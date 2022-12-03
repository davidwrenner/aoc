import sys
import os

# file I/O
input_file = sys.argv[0][0:2] + ".txt"
input_path = "../input/" + input_file

if not os.path.exists(input_path):
    raise FileNotFoundError(f"Did not find expected input {input_path}")

with open(input_path, "r") as f:
    input = [line.rstrip() for line in f if line != "\n"]


def priority(char: str) -> int:
    return ord(char) + ((27 - ord('A')) if char.isupper() else (1 - ord('a')))


def shared_item(sack: str) -> str:
    med = len(sack) // 2
    first_half_items = sack[:med]
    for item in sack[med:]:
        if item in first_half_items:
            return item


ans = None
# part a
priorities = 0
for rucksack in input:
    priorities += priority(shared_item(rucksack))
ans = priorities
print("Answer A:", ans)

# part b
priorities = 0
for i in range(0, len(input), 3):
    elf_1 = set(input[i])
    elf_2 = set(input[i+1])
    elf_3 = set(input[i+2])

    common_item = elf_1.intersection(elf_2, elf_3).pop()
    priorities += priority(common_item)

ans = priorities
print("Answer B:", ans)



