#!/usr/bin/env python
from collections import defaultdict
from itertools import product
from operator import mul
import math
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

def num_primes(formula):
    num = 0
    for n in range(1000):
        res = formula(n)
        if res < 1 or not is_prime(res):
            return num
        else:
            num += 1
 
def is_prime(num):
    if num_divisors(num) == 2 and num > 1:
        return True
    else:
        return False

def main():
    most = 0
    best = (0, 0)
    for a, b in product(list(range(-999,1000)), list(range(-999, 1000))):
        formula = lambda n: n**2 + a*n + b
        num = num_primes(formula) 
        if num > most:
            most = num
            best = (a, b)
    print(mul(*best))

if __name__ == "__main__":
    main()
