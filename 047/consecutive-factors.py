#!/usr/bin/env python
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

def distinct_prime_factors(n):
    return set(factorize(n))

def main():
    chain = []
    search = 4
    for n in range(1, 1000000):
        if len(distinct_prime_factors(n)) == search:
            chain.append(n)
    print(next(chain[i:i+search] for i, n in enumerate(chain) if chain[i:i+search] == list(range(n, n+search)))[0])

if __name__ == "__main__": main()
