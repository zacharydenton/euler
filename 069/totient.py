#!/usr/bin/env python
import math
from operator import mul
from functools import reduce

def factorize(n):
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

def totient(n):
    return n * reduce(mul, [1 - (1.0 / p) for p in set(factorize(n))])

def main():
    print(max((n / totient(n), n) for n in range(2, 1000001))[1])

if __name__ == "__main__": main()
