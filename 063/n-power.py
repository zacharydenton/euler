#!/usr/bin/env python
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
    for i, x in product(range(1,100), range(1,100)):
        if len(get_digits(i ** x)) == x:
            count += 1
    print count

if __name__ == "__main__":
    main()
