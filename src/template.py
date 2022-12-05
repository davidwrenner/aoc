import sys
import os

# file I/O
input_file = sys.argv[0][0:2] + ".txt"
input_path = "../input/" + input_file

if not os.path.exists(input_path):
    raise FileNotFoundError(f"Did not find expected input {input_path}")

with open(input_path, "r") as f:
    input = [line.rstrip() for line in f]

ans = None
# part a

print("Answer A:", ans)

# part b
 

print("Answer B:", ans)


 
