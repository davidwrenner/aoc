import sys
import os

# file I/O
input_file = sys.argv[0][0:2] + ".txt"
# input_file = "smallcase.txt"
input_path = "../input/" + input_file

if not os.path.exists(input_path):
    sys.exit(f"Did not find expected input {input_path}")

with open(input_path, "r") as f:
    input = [line.rstrip() for line in f if line != "\n"]


class Play:
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Outcomes:
    LOSS = 0
    DRAW = 3
    WIN = 6


def char_to_oppo_play(char):
    if char == "A":
        return Play.ROCK
    elif char == "B":
        return Play.PAPER
    return Play.SCISSORS


def char_to_my_play(char):
    if char == "X":
        return Play.ROCK
    elif char == "Y":
        return Play.PAPER
    return Play.SCISSORS


ans = None
# part a
score = 0
for line in input:
    opponent_play = char_to_oppo_play(line[0])
    my_play = char_to_my_play(line[2])

    score += my_play

    if my_play == opponent_play:
        score += Outcomes.DRAW
    elif my_play == Play.ROCK and opponent_play == Play.SCISSORS:
        score += Outcomes.WIN
    elif my_play == Play.PAPER and opponent_play == Play.ROCK:
        score += Outcomes.WIN
    elif my_play == Play.SCISSORS and opponent_play == Play.PAPER:
        score += Outcomes.WIN
    else:
        score += Outcomes.LOSS

ans = score

print("Answer A:", ans)

# part b
def char_to_outcome(char):
    if char == "X":
        return Outcomes.LOSS
    elif char == "Y":
        return Outcomes.DRAW
    return Outcomes.WIN

score = 0
for line in input:
    opponent_play = char_to_oppo_play(line[0])
    desired_outcome = char_to_outcome(line[2])

    if desired_outcome == Outcomes.DRAW:
        my_play = opponent_play
    elif desired_outcome == Outcomes.WIN:
        if opponent_play == Play.ROCK:
            my_play = Play.PAPER
        elif opponent_play == Play.PAPER:
            my_play = Play.SCISSORS
        else:
            my_play = Play.ROCK
    else:
        if opponent_play == Play.ROCK:
            my_play = Play.SCISSORS
        elif opponent_play == Play.PAPER:
            my_play = Play.ROCK
        else:
            my_play = Play.PAPER

    score += my_play + desired_outcome

ans = score
print("Answer B:", ans)


 
