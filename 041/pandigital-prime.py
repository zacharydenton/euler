#!/usr/bin/env python3
from collections import defaultdict
from itertools import *
from functools import reduce
import math

def is_pandigital(num):
    digits = sorted(int(d) for d in str(num))
    if digits == list(range(1,len(digits)+1)):
        return True
    else:
        return False

def factorize(n):
    if n < 1:
        raise ValueError('fact() argument should be >= 1')
    if n == 1:
        return []  # special case
    res = []
    # iterate over all even numbers first.
    while n % 2 == 0:
        res.append(2)
        n //= 2
    # try odd numbers up to sqrt(n)
    limit = math.sqrt(n+1)
    i = 3
    while i <= limit:
        if n % i == 0:
            res.append(i)
            n //= i
            limit = math.sqrt(n+i)
        else:
            i += 2
    if n != 1:
        res.append(n)
    return res

def num_divisors(n):
    factors = sorted(factorize(n))
    histogram = defaultdict(int)
    for factor in factors:
        histogram[factor] += 1
    # number of divisors is equal to product of 
    # incremented exponents of prime factors
    from operator import mul
    try:
        return reduce(mul, [exponent + 1 for exponent in list(histogram.values())])
    except:
        return 1

def is_prime(num):
    if num % 2 == 0:
        return False
    if num % 3 == 0:
        return False

    if num_divisors(num) == 2 and num > 1:
        return True
    else:
        return False

def convert_list_to_int(l):
    return int(''.join(str(d) for d in l))

def main():
    pandigitals = (convert_list_to_int(p) for p in permutations(list(range(1,8))))
    print((max(p for p in pandigitals if is_prime(p))))

if __name__ == "__main__":
    main()
