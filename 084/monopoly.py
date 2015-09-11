#!/usr/bin/env python
from random import randint, shuffle
from collections import deque, Counter

squares = ["GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3", "JAIL", "C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3", "FP", "E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3", "G2J", "G1", "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2"]
square_numbers = {square: i for i, square in enumerate(squares)}
num_squares = len(squares)

def build_deck(choices):
    numbers = [square_numbers[square] for square in choices]
    shuffle(numbers)
    return deque(numbers)

transitions = {
    "G2J": build_deck(["JAIL"]),
    "CH1": build_deck(["CH1", "CH1", "CH1", "CH1", "CH1", "CH1", "GO", "JAIL", "C1", "E3", "H2", "R1", "R2", "R2", "U1", "T1"]),
    "CH2": build_deck(["CH2", "CH2", "CH2", "CH2", "CH2", "CH2", "GO", "JAIL", "C1", "E3", "H2", "R1", "R2", "R3", "U2", "D3"]),
    "CH3": build_deck(["CH3", "CH3", "CH3", "CH3", "CH3", "CH3", "GO", "JAIL", "C1", "E3", "H2", "R1", "R1", "R1", "U1", "CC3"]),
    "CC1": build_deck(["CC1", "CC1", "CC1", "CC1", "CC1", "CC1", "CC1", "CC1", "CC1", "CC1", "CC1", "CC1", "CC1", "CC1", "GO", "JAIL"]),
    "CC2": build_deck(["CC2", "CC2", "CC2", "CC2", "CC2", "CC2", "CC2", "CC2", "CC2", "CC2", "CC2", "CC2", "CC2", "CC2", "GO", "JAIL"]),
    "CC3": build_deck(["CC3", "CC3", "CC3", "CC3", "CC3", "CC3", "CC3", "CC3", "CC3", "CC3", "CC3", "CC3", "CC3", "CC3", "GO", "JAIL"])
}
transitions = {square_numbers[square]: deck for square, deck in list(transitions.items())}

def transition(square_number):
    while square_number in transitions:
        deck = transitions[square_number]
        new_square_number = deck.pop()
        deck.appendleft(new_square_number)
        if square_number == new_square_number:
            break
        square_number = new_square_number
    return square_number

def move(square_number, die_size=6):
    roll = randint(1, die_size) + randint(1, die_size)
    square_number += roll
    square_number %= num_squares
    return transition(square_number)

def simulate(iterations=2000000, die_size=6):
    result = Counter()
    square_number = 0
    for i in range(iterations):
        square_number = move(square_number, die_size)
        result[square_number] += 1
    return result

def main():
    simulation = simulate(die_size=4)
    print(("".join("{:02}".format(square_number) for square_number, count in simulation.most_common(3))))

if __name__ == "__main__": main()
