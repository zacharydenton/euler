#!/usr/bin/env python
# The fraction 49/98 is a curious fraction, as an inexperienced 
# mathematician in attempting to simplify it may incorrectly 
# believe that 49/98 = 4/8, which is correct, is obtained by 
# cancelling the 9s.
# 
# We shall consider fractions like, 30/50 = 3/5, to be trivial 
# examples.
# 
# There are exactly four non-trivial examples of this type of 
# fraction, less than one in value, and containing two digits 
# in the numerator and denominator.
# 
# If the product of these four fractions is given in its lowest 
# common terms, find the value of the denominator.
from fractions import *
from itertools import *

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
    fractions = product(range(10, 100), range(10, 100))
    print reduce(lambda a, b: a * b, (Fraction(*f) for f in fractions if is_curious(*f))).denominator

if __name__ == "__main__":
    main()
