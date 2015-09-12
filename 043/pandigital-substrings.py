#!/usr/bin/env python
from itertools import *

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
    print(sum(convert_list_to_int(p) for p in pandigitals if has_property(p)))

if __name__ == "__main__":
    main()
