#!/usr/bin/env python
from itertools import product

def sieve(n):
    numbers = list(range(2, n+1))
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
    composites = set(n for n in range(2,10000) if n not in primes)
    twicesquares = set(2*(n**2) for n in range(100))

    sums = set(sum(c) for c in product(primes, twicesquares))
    print(min(n for n in composites if n not in sums and n % 2 != 0))

if __name__ == "__main__":
    main()
