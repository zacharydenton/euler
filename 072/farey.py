#!/usr/bin/env python
import math
from operator import mul
from functools import reduce

def prime_factors(n):
    res = set()
    # iterate over all even numbers first.
    while n % 2 == 0:
        res.add(2)
        n //= 2
    # try odd numbers up to sqrt(n)
    limit = math.sqrt(n+1)
    i = 3
    while i <= limit:
        if n % i == 0:
            res.add(i)
            n //= i
            limit = math.sqrt(n+i)
        else:
            i += 2
    if n != 1:
        res.add(n)
    return res

def totient(n):
    if n == 1: return 1
    return int(round(n * reduce(mul, [1 - 1.0 / p for p in prime_factors(n)])))

def farey_length(n):
    return sum(totient(m) for m in range(1, n+1)) - 1

def main():
    print(farey_length(1000000))

if __name__ == "__main__": main()
