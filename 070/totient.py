#!/usr/bin/env python
from math import sqrt
from operator import mul
from itertools import *

def primes(n): 
    if n == 2:
        return [2]
    elif n < 2:
        return []
    sieve = list(range(3, n+1, 2))
    mroot = n ** 0.5
    half = (n + 1) // 2 - 1
    i = 0
    m = 3
    while m <= mroot:
        if sieve[i]:
            j = (m * m - 3) // 2
            sieve[j] = 0
            while j < half:
                sieve[j] = 0
                j += m
        i = i + 1
        m = 2 * i + 3
    return [2] + [p for p in sieve if p]

def main():
    pairs = combinations(primes(2 * int(sqrt(1e7))), 2)
    minimum = (100, 0)
    for n, t in ((a * b, (a-1) * (b-1)) for a, b in pairs if a * b < 1e7):
        ratio = float(n) / t
        if ratio < minimum[0] and sorted(str(n)) == sorted(str(t)):
            minimum = (ratio, n)

    print(minimum[1])

if __name__ == "__main__": main()
