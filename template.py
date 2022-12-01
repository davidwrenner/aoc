import sys
import os

# file I/O
input_file = sys.argv[0][0:2] + ".txt"

if not os.path.exists(input_file):
	sys.exit(f"Did not find expected file {input_file}") 

with open(input_file, "r") as f:
    input = [line.rstrip() for line in f if line != "\n"]

ans = None
# part a

print("Answer A:", ans)

# part b
 

print("Answer B:", ans)


 
