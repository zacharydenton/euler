#!/usr/bin/env python
from itertools import *

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)

def digits(n):
    return map(int, str(n))

def is_increasing(n):
    return all(prev <= curr for prev, curr in pairwise(digits(n)))

def is_decreasing(n):
    return all(prev >= curr for prev, curr in pairwise(digits(n)))

def is_bouncy(n):
    return not is_increasing(n) and not is_decreasing(n)

def running_total(iterable):
    total = 0
    for element in iterable:
        total += element
        yield total

def main():
    nums = count(1)
    bouncy = running_total(imap(lambda n: float(is_bouncy(n)), count(1)))
    print (n for n, b in izip(nums, bouncy) if b / n == 0.99).next()

if __name__ == "__main__": main()
