#!/usr/bin/env python3
# A perfect number is a number for which the 
# sum of its proper divisors is exactly equal 
# to the number. For example, the sum of the 
# proper divisors of 28 would be 
# 1 + 2 + 4 + 7 + 14 = 28, 
# which means that 28 is a perfect number.
#
# A number n is called deficient if the sum 
# of its proper divisors is less than n and 
# it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 
# 1 + 2 + 3 + 4 + 6 = 16, the smallest number 
# that can be written as the sum of two abundant 
# numbers is 24. By mathematical analysis, it 
# can be shown that all integers greater than 
# 28123 can be written as the sum of two abundant 
# numbers. However, this upper limit cannot be 
# reduced any further by analysis even though it 
# is known that the greatest number that cannot be 
# expressed as the sum of two abundant numbers is 
# less than this limit.
#
# Find the sum of all the positive integers which 
# cannot be written as the sum of two abundant numbers.
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
    print(sum(number for number in range(1,30000) if number not in sums))
    
if __name__ == "__main__":
    main()

