#!/usr/bin/env python
# Euler published the remarkable quadratic formula:
#
#   n**2 + n + 41
#
# It turns out that the formula will produce 40 primes 
# for the consecutive values n = 0 to 39. However, when 
# n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible 
# by 41, and certainly when n = 41, 41**2 + 41 + 41 is 
# clearly divisible by 41.
# 
# Using computers, the incredible formula  n**2 - 79n + 1601 
# was discovered, which produces 80 primes for the 
# consecutive values n = 0 to 79. The product of the 
# coefficients, 79 and 1601, is 126479.
# 
# Considering quadratics of the form:
# 
#   n**2 + an + b, where |a| < 1000 and |b| < 1000
# 
# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |4| = 4
# Find the product of the coefficients, a and b, for 
# the quadratic expression that produces the maximum 
# number of primes for consecutive values of n, 
# starting with n = 0.
from collections import defaultdict
import math

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
        return reduce(mul, [exponent + 1 for exponent in histogram.values()])
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
    best = ''
    for a in range(-9999,10000):
        for b in range(-9999, 10000):
            formula = lambda n: n**2 + a*n + b
            num = num_primes(formula) 
            if num > 70:
                most = num
                best = "n**2 + %(a)s*n + %(b)s" % {'a' : a, 'b' : b}
                print best,'=', most
    print best,'=',most

if __name__ == "__main__":
    main()
