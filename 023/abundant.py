#!/usr/bin/env python3
import math
from collections import defaultdict
from itertools import *
from functools import reduce
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
    factors = sorted(res)
    histogram = defaultdict(int)
    for factor in factors:
        histogram[factor] += 1

    return list(histogram.items())

def divisors(n):
    factors = factorize(n)
    nfactors = len(factors)
    f = [0] * nfactors
    while True:
        yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return

def proper_divisors(n):
    return list(divisors(n))[:-1]

def classify(n):
    total = sum(proper_divisors(n))
    if total == n:
        # perfect
        return 0
    elif total > n:
        # abundant
        return 1
    else:
        # deficient
        return -1

def main():
    abundant = set(number for number in range(2, 30000) if classify(number) == 1)
    sums = sorted(set(sum(c) for c in combinations_with_replacement(abundant, 2)))
    print((sum(number for number in range(1,30000) if number not in sums)))
    
if __name__ == "__main__":
    main()
