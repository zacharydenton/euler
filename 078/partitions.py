#!/usr/bin/env python
from itertools import *

def pentagonal(n):
    return n*(3*n - 1) / 2

partitions = {}
generalized_pentagonals = sorted(map(pentagonal, range(-250, 250)))[1:]
def partition(n):
    if n <= 1: return 1
    if n not in partitions:
        signs = cycle([1, 1, -1, -1])
        pentagonals = takewhile(lambda p: p <= n, generalized_pentagonals)
        partitions[n] = sum(sign * partition(n - p) for sign, p in izip(signs, pentagonals))

    return partitions[n]

def main():
    print (n for n in count(0) if partition(n) % 1000000 == 0).next()

if __name__ == "__main__": main()
