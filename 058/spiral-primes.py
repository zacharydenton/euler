#!/usr/bin/env python
import math
from collections import defaultdict
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
    if num % 3 == 0 and num != 3:
        return False

    if num_divisors(num) == 2 and num > 1:
        return True
    else:
        return False

def spiral_diagonals():
    n = 1
    step = 2
    since_last = 0
    while True:
        yield n
        n += step
        since_last += 1
        if since_last == 4:
            step += 2
            since_last = 0

def main():
    level = 0
    primes = 0
    for i, n in enumerate(spiral_diagonals()):
        if (i-1) % 4 == 0:
            level += 1

        if is_prime(n):
            primes += 1
        side_length = (2 * level) + 1

        ratio =  float(primes) / float(i+1)
        if 0 < ratio < 0.1:
            print(side_length)
            return

if __name__ == "__main__":
    main()
