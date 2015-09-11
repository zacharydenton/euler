#!/usr/bin/env python
import os
from itertools import *
from operator import itemgetter

SCORE_FUNCS = []

def score_func(func):
    SCORE_FUNCS.append(func)
    return func

@score_func
def highest_card(cards):
    return max(value for value, suit in cards)

@score_func
def one_pair(cards):
    pairs = groups(cards, 2)
    if len(pairs) == 1:
        return 1e2 + 2e1 * max(pairs)
    return 0

@score_func
def two_pair(cards):
    pairs = groups(cards, 2)
    if len(pairs) == 2:
        return 1e3 + 2e2 * max(pairs)
    return 0

@score_func
def three_of_a_kind(cards):
    threes = groups(cards, 3)
    if len(threes) == 1:
        return 1e4 + 2e3 * max(threes)
    return 0

@score_func
def straight(cards):
    return 1e5 * int(all(b - a == 1 for a, b in pairwise(cards)))

@score_func
def flush(cards):
    return 1e6 * int(len(suits(cards)) == 1)

@score_func
def full_house(cards):
    return 1e7 * int(len(groups(cards, 2)) == 1 and len(groups(cards, 3)) == 1)

@score_func
def four_of_a_kind(cards):
    fours = groups(cards, 4)
    if len(fours) == 1:
        return 1e8 + 2e7 * max(fours)
    return 0

@score_func
def straight_flush(cards):
    return 1e9 * int(len(suits(cards)) == 1 and all(b - a == 1 for a, b in pairwise(cards)))

@score_func
def royal_flush(cards):
    return 1e10 * int(len(suits(cards)) == 1 and [value for value, suit in cards] == [10, 11, 12, 13, 14])

def score(cards):
    return sum(score_func(cards) for score_func in SCORE_FUNCS)

def groups(cards, length):
    return [k for k, g in groupby(value for value, suit in cards) if len(list(g)) == length]

def pairwise(cards):
    a, b = tee(value for value, suit in cards)
    next(b, None)
    return zip(a, b)

def suits(cards):
    return list({suit for value, suit in cards})

def cards(hand):
    faces = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return sorted(((int(faces.get(card[0], card[0])), card[1]) for card in hand), key=itemgetter(0))

def parse_hands(lines):
    return ((cards(line.split()[:5]), cards(line.split()[5:])) for line in lines)

def winner(hands):
    return int(score(hands[0]) < score(hands[1])) + 1

def main():
    with open(os.path.join(os.path.dirname(__file__), 'poker.txt')) as f:
        print(sum(1 for hands in parse_hands(f) if winner(hands) == 1))

if __name__ == "__main__":
    main()
