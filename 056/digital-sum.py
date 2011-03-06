#!/usr/bin/env python
# A googol (10**100) is a massive number: one followed by one-hundred zeros; 
# 100**100 is almost unimaginably large: one followed by two-hundred zeros. 
# Despite their size, the sum of the digits in each number is only 1.
# 
# Considering natural numbers of the form, a**b, where a, b < 100, what is 
# the maximum digital sum?
from itertools import *

def get_digits(n):
    return [int(digit) for digit in str(n)]

def main():
    largest = 0
    for a, b in product(range(1, 100), range(1, 100)):
        s = sum(get_digits(a ** b))
        if s > largest:
            largest = s
    print largest

if __name__ == "__main__":
    main()
