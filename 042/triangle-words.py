#!/usr/bin/env python
import os
from string import ascii_uppercase

def letter_value(letter):
    return ascii_uppercase.index(letter.upper())+1

def word_value(word):
    return sum(letter_value(letter) for letter in word)

def triangle(n):
    return int((0.5) * n * (n+1))

def main():
    triangle_numbers = [triangle(n) for n in range(1, 100)]
    words = [word.strip('"') for word in open(os.path.join(os.path.dirname(__file__), 'words.txt')).read().split(',')]
    total = 0
    for word in words:
        if word_value(word) in triangle_numbers:
            total += 1
    print(total)

if __name__ == "__main__":
    main()

