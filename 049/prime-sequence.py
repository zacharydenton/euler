#!/usr/bin/env python
# The arithmetic sequence, 1487, 4817, 8147, in which each of the 
# terms increases by 3330, is unusual in two ways: (i) each of the 
# three terms are prime, and, (ii) each of the 4-digit numbers are 
# permutations of one another.
# 
# There are no arithmetic sequences made up of three 1-, 2-, or 
# 3-digit primes, exhibiting this property, but there is one other 
# 4-digit increasing sequence.
# 
# What 12-digit number do you form by concatenating the three terms 
# in this sequence?
import math
from itertools import *
from collections import defaultdict

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

def is_permutations(seq):
    s = [str(x) for x in seq]
    p = [''.join(x) for x in permutations(s[0])]
    for i in s:
        if i not in p:
            return False
    return True

def is_prime(num):
    if num % 2 == 0:
        return False
    if num % 3 == 0:
        return False

    if num_divisors(num) == 2 and num > 1:
        return True
    else:
        return False

def sieve(n):
    numbers = range(2, n+1)
    p = 2
    j = 0
    done = False
    while not done:
        for i, n in enumerate(numbers):
            if n % p == 0 and n!=p:
                numbers.pop(i)
        j += 1
        p = numbers[j]
        if p**2 > n:
            done = True
    return numbers

def arithmetic_subsequences(seq, length=3):
    for x in seq:
        steps = [y-x for y in seq[seq.index(x):]]
        for step in steps:
            if step == 0: continue
            found = True
            for i in range(length):
                if not x + (i*step) in seq:
                    found = False
            if found:
                yield [x + (i*step) for i in range(length)]

def main():
    primes = [p for p in sieve(10000) if len(str(p)) == 4]
    print max(''.join(str(x) for x in seq) for seq in arithmetic_subsequences(primes, 3) if is_permutations(seq))

if __name__ == "__main__":
    main()
