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
    limit = math.sqrt(n + 1)
    i = 3
    while i <= limit:
        if n % i == 0:
            res.append(i)
            n //= i
            limit = math.sqrt(n + i)
        else:
            i += 2
    if n != 1:
        res.append(n)
    return res

_triangle_cache = {1: 1}
def triangle(n):
    if n < 1:
        return 0
    try:
        return _triangle_cache[n]
    except KeyError:
        result = n + triangle(n - 1)
        _triangle_cache[n] = result
        return result

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

triangles = (triangle(i) for i in range(1, 100000))
divisible_triangles = (i for i in triangles if num_divisors(i) > 500)
print(next(divisible_triangles))
