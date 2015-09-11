#!/usr/bin/env python

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
    print(sum(chain))

if __name__ == "__main__":
    main()
