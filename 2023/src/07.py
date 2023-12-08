#!/usr/bin/env python3
import os
import subprocess as sp
import sys
import numpy as np
import re
from collections import deque

ans = None
input_path = "../input/" + (__file__.replace('py', 'txt') if "-t" not in sys.argv else "testcase.txt")

with open(input_path, "r") as f:
    input = [line.rstrip() for line in f]

class Type:
    KIND5=6
    KIND4=5
    FULL=4
    KIND3=3
    PAIR2=2
    PAIR1=1
    HIGH=0

# part a
def rank_of_card(c):
    cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    return len(cards) - cards.index(c)

def get_type(cards):
    unique = set(cards)
    if len(unique) == len(cards):
        return Type.HIGH
    elif len(unique) == 1:
        return Type.KIND5
    elif len(unique) == 2:
        c1 = cards.count(cards[0])
        c2 = cards.count(cards[1])
        if max(sorted([c1, c2])) == 4:
            return Type.KIND4
        return Type.FULL
    elif len(unique) == 4:
        return Type.PAIR1
    # else 3 distinct
    c1 = cards.count(cards[0])
    c2 = cards.count(cards[1])
    c3 = cards.count(cards[2])
    if max(sorted([c1,c2,c3])) == 3:
        return Type.KIND3
    return Type.PAIR2

def insert_hand(hand, ranks):
    if not ranks:
        return [hand]
    hand_cards, _ = hand.split()
    hand_type = get_type(hand_cards)
    for i, rank in enumerate(ranks):
        rank_cards, _ = rank.split()
        rank_type = get_type(rank_cards)
        if hand_type > rank_type:
            continue
        elif hand_type < rank_type:
            return ranks[:i] + [hand] + ranks[i:]
        else:
            for (h, r) in zip(hand_cards, rank_cards):
                if rank_of_card(h) > rank_of_card(r):
                    break
                if rank_of_card(h) < rank_of_card(r):
                    return ranks[:i] + [hand] + ranks[i:]
    return ranks + [hand]

ranks = []   
for line in input:
    ranks = insert_hand(line, ranks)

total_winnings = 0
for i, hand in enumerate(ranks):
    _, bid = hand.split()
    total_winnings += (i+1)*int(bid)

ans = total_winnings
print("Answer A:", ans)

# part b
CARDS = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

def rank_of_card(c):
    return len(CARDS) - CARDS.index(c)

def get_type(cards):
    unique = set(cards)
    if len(unique) == len(cards):
        return Type.HIGH
    elif len(unique) == 1:
        return Type.KIND5
    elif len(unique) == 2:
        c1 = cards.count(cards[0])
        c2 = cards.count(cards[1])
        if max(sorted([c1, c2])) == 4:
            return Type.KIND4
        return Type.FULL
    elif len(unique) == 4:
        return Type.PAIR1
    # else 3 distinct
    c1 = cards.count(cards[0])
    c2 = cards.count(cards[1])
    c3 = cards.count(cards[2])
    if max(sorted([c1,c2,c3])) == 3:
        return Type.KIND3
    return Type.PAIR2

def insert_hand(hand, ranks):
    if not ranks:
        return [hand]
    hand_cards, _ = hand.split()
    hand_type = max([get_type(hand_cards.replace("J", c)) for c in CARDS])
    for i, rank in enumerate(ranks):
        rank_cards, _ = rank.split()
        rank_type = max([get_type(rank_cards.replace("J", c)) for c in CARDS])
        if hand_type > rank_type:
            continue
        elif hand_type < rank_type:
            return ranks[:i] + [hand] + ranks[i:]
        else:
            for (h, r) in zip(hand_cards, rank_cards):
                if rank_of_card(h) > rank_of_card(r):
                    break
                if rank_of_card(h) < rank_of_card(r):
                    return ranks[:i] + [hand] + ranks[i:]
    return ranks + [hand]

ranks = []   
for line in input:
    ranks = insert_hand(line, ranks)

total_winnings = 0
for i, hand in enumerate(ranks):
    _, bid = hand.split()
    total_winnings += (i+1)*int(bid)

ans = total_winnings
print("Answer B:", ans)
sp.run("pbcopy", input=str(ans), text=True)
