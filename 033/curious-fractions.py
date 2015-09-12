#!/usr/bin/env python
from fractions import *
from itertools import *
from functools import reduce

def is_curious(n, d):
    f = Fraction(n, d)
    if f >= 1:
        return False
    n_digits = [int(digit) for digit in str(n)]
    d_digits = [int(digit) for digit in str(d)]

    if n_digits[1] == d_digits[0]:
        try:
            if Fraction(n_digits[0], d_digits[1]) == f:
                return True
        except:
            pass
    return False
def main():
    fractions = product(list(range(10, 100)), list(range(10, 100)))
    print(reduce(lambda a, b: a * b, (Fraction(*f) for f in fractions if is_curious(*f))).denominator)

if __name__ == "__main__":
    main()
