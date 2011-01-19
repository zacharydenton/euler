#!/usr/bin/env python
# The number, 1406357289, is a 0 to 9 pandigital number because 
# it is made up of each of the digits 0 to 9 in some order, but 
# it also has a rather interesting sub-string divisibility property.
# 
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In 
# this way, we note the following:
# 
#   d2d3d4=406 is divisible by 2
#   d3d4d5=063 is divisible by 3
#   d4d5d6=635 is divisible by 5
#   d5d6d7=357 is divisible by 7
#   d6d7d8=572 is divisible by 11
#   d7d8d9=728 is divisible by 13
#   d8d9d10=289 is divisible by 17
# 
# Find the sum of all 0 to 9 pandigital numbers with this property.
from itertools import *

def is_pandigital(n, length=10):
    digits = sorted([int(digit) for digit in str(n)])
    if digits == range(length):
        return True
    return False

def has_property(digits):
    primes = [1,2,3,5,7,11,13,17]
    for i in range(1, len(digits)-2):
        if not int(''.join(digits[i:i+3])) % primes[i] == 0:
            return False
    return True 

def convert_list_to_int(l):
    return int(''.join(str(i) for i in l))

def main():
    pandigitals = permutations((str(i) for i in range(10)))
    print sum(convert_list_to_int(p) for p in pandigitals if has_property(p))

if __name__ == "__main__":
    main()
