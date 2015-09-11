#!/usr/bin/env python
from itertools import product, takewhile

def euler(n):
    # Create a candidate list within which non-primes will
    # marked as None, noting that only candidates below
    # sqrt(n) need be checked. 
    candidates = list(range(n+1))
    fin = int(n**0.5)
 
    # Loop over the candidates, marking out each multiple.
    # If the current candidate is already checked off then
    # continue to the next iteration.
    for i in range(2, fin+1):
        if not candidates[i]:
            continue
 
        candidates[2*i::i] = [None] * (n//i - 1)
 
    # Filter out non-primes and return the list.
    return [i for i in candidates[2:] if i]

def main():
    limit = 50000000
    primes = euler(int(limit**0.5))
    squares = takewhile(lambda x: x < limit, (prime**2 for prime in primes))
    cubes = takewhile(lambda x: x < limit, (prime**3 for prime in primes))
    tesseracts = takewhile(lambda x: x < limit, (prime**4 for prime in primes))
    print((len(set(s + c + t for (s, c, t) in product(squares, cubes, tesseracts) if s + c + t < limit))))

if __name__ == "__main__": main()
