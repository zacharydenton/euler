#!/usr/bin/env python
# The prime 41, can be written as the sum of six consecutive primes:
# 
#   41 = 2 + 3 + 5 + 7 + 11 + 13
# 
# This is the longest sum of consecutive primes that adds to a prime 
# below one-hundred.
# 
# The longest sum of consecutive primes below one-thousand that adds 
# to a prime, contains 21 terms, and is equal to 953.
# 
# Which prime, below one-million, can be written as the sum of the 
# most consecutive primes?
def euler(n):
    # Create a candidate list within which non-primes will
    # marked as None, noting that only candidates below
    # sqrt(n) need be checked. 
    candidates = range(n+1)
    fin = int(n**0.5)
 
    # Loop over the candidates, marking out each multiple.
    # If the current candidate is already checked off then
    # continue to the next iteration.
    for i in xrange(2, fin+1):
        if not candidates[i]:
            continue
 
        candidates[2*i::i] = [None] * (n//i - 1)
 
    # Filter out non-primes and return the list.
    return [i for i in candidates[2:] if i]

def largest_consecutive_seq(primes):
    largest = []
    for prime in primes:
        total = 0
        for i, a in enumerate(primes[:primes.index(prime)]):
            j = 0
            while total < prime:
                total += primes[i+j]
                j += 1
            if total == prime:
                seq = primes[i:i+j]
                if len(seq) > len(largest):
                    largest = seq
    return largest

def main():
    primes = euler(1000000)
    largest = 0
    chain = []
    for start in range(10):
        seq = primes[start:]
        i = 0
        total = 0
        for prime in seq:
            total += prime
            if total > 1000000:
                break
            i += 1
            if total in primes:
                c = seq[:i]
                if len(c) > len(chain):
                    chain = c
    print sum(chain)

if __name__ == "__main__":
    main()
