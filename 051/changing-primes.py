#!/usr/bin/env python
from itertools import *
def primes(n): 
    if n==2: return [2]
    elif n<2: return []
    s=list(range(3,n+1,2))
    mroot = n ** 0.5
    half=(n+1)//2-1
    i=0
    m=3
    while m <= mroot:
        if s[i]:
            j=(m*m-3)//2
            s[j]=0
            while j<half:
                s[j]=0
                j+=m
        i=i+1
        m=2*i+3
    return [2]+[x for x in s if x]

from bisect import bisect_left
# sqrt(1000000000) = 31622
__primes = primes(31622)
def is_prime(n):
    # if prime is already in the list, just pick it
    if n <= 31622:
        i = bisect_left(__primes, n)
        return i != len(__primes) and __primes[i] == n
    # Divide by each known prime
    limit = int(n ** .5)
    for p in __primes:
        if p > limit: return True
        if n % p == 0: return False
    # fall back on trial division if n > 1 billion
    for f in range(31627, limit, 6): # 31627 is the next prime
        if n % f == 0 or n % (f + 4) == 0:
            return False
    return True

def number_families(num):
    digits = [d for d in str(num)]
    products = list(product((True, False), repeat=len(digits)))[1:-1]
    for p in products:
        pattern = ''
        for i, x in enumerate(p):
            if x:
                pattern += digits[i]
            else:
                pattern += 'X'
        yield [int(pattern.replace('X', str(n))) for n in range(10)]

def main():
    for prime in primes(1000000):
        for number_family in number_families(prime):
            prime_family = [n for n in number_family if is_prime(n) and len(str(n)) == len(str(prime))]
            if len(prime_family) == 8 and prime in prime_family:
                print(prime)
                return

if __name__ == "__main__":
    main()
