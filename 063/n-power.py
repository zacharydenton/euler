#!/usr/bin/env python
# The 5-digit number, 16807=7**5, is also a fifth power. 
# Similarly, the 9-digit number, 134217728=8**9, is a ninth power.
# 
# How many n-digit positive integers exist which are also an nth power?
from itertools import *

def get_digits(n):
    return str(n)

def is_npower(n):
    digits = str(n)
    ndigits = len(digits)
    for i in range(2,10):
        if i ** ndigits == n:
            return True
    return False

def main():
    count = 0
    i = 0
    for i, x in product(range(1,100), range(1,100)):
        if len(get_digits(i ** x)) == x:
            count += 1
    print count

if __name__ == "__main__":
    main()
