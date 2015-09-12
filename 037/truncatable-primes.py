#!/usr/bin/env python
from collections import defaultdict
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

def is_prime(num):
    if num_divisors(num) == 2 and num > 1:
        return True
    else:
        return False

def is_truncatable(prime):
    if not is_prime(prime):
        return False

    digits = [int(digit) for digit in str(prime)]
    if len(digits) == 1:
        return False

    for i in range(1, len(digits)):
        left = int(''.join(str(digit) for digit in digits[:i]))
        right = int(''.join(str(digit) for digit in digits[i:]))
        if not is_prime(left) or not is_prime(right):
            return False
    return True

def main():
    print(sum(n for n in range(1, 1000000) if is_truncatable(n)))

if __name__ == "__main__":
    main()
