#!/usr/bin/env python
# It was proposed by Christian Goldbach that every odd 
# composite number can be written as the sum of a prime 
# and twice a square.
#
#   9 = 7 + 212
#   15 = 7 + 222
#   21 = 3 + 232
#   25 = 7 + 232
#   27 = 19 + 222
#   33 = 31 + 212
# 
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be 
# written as the sum of a prime and twice a square?
from itertools import product

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

def main():
    primes = sieve(10000)
    composites = set(n for n in range(10000) if n not in primes)
    twicesquares = set(2*(n**2) for n in range(100))

    sums = set(sum(c) for c in product(primes, twicesquares))
    print [n for n in composites if n not in sums and n % 2 != 0]

if __name__ == "__main__":
    main()
