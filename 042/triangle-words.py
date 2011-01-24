#!/usr/bin/env python
# The nth term of the sequence of triangle numbers is given by, 
# tn = (1/2)n(n+1); so the first ten triangle numbers are:
# 
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# 
# By converting each letter in a word to a number corresponding 
# to its alphabetical position and adding these values we form 
# a word value. For example, the word value for SKY is:
# 
# 19 + 11 + 25 = 55 = t10
# 
# If the word value is a triangle number then we shall call the 
# word a triangle word.
# 
# Using words.txt (right click and 'Save Link/Target As...'), a 
# 16K text file containing nearly two-thousand common English 
# words, how many are triangle words?
from string import ascii_uppercase
def letter_value(letter):
    return ascii_uppercase.index(letter.upper())+1

def word_value(word):
    return sum(letter_value(letter) for letter in word)

def triangle(n):
    return int((0.5) * n * (n+1))

def main():
    triangle_numbers = [triangle(n) for n in range(1, 100)]
    words = [word.strip('"') for word in open('words.txt').read().split(',')]
    total = 0
    for word in words:
        if word_value(word) in triangle_numbers:
            total += 1
    print total

if __name__ == "__main__":
    main()

