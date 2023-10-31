import sys
import os

# file I/O
input_file = sys.argv[0][0:2] + ".txt"
input_path = "../input/" + input_file

if not os.path.exists(input_path):
    raise FileNotFoundError(f"Did not find expected input {input_path}")

with open(input_path, "r") as f:
    input = [line.rstrip() for line in f][0]


def compute_start(num_unique):
    for i in range(len(input) - num_unique):
        window = input[i:i + num_unique]
        if len(set(window)) == num_unique:
            return i + num_unique


# part a
ans = compute_start(4)
print("Answer A:", ans)

# part b
ans = compute_start(14)
print("Answer B:", ans)


 
