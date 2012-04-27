#!/usr/bin/env python
from itertools import *
from fractions import Fraction

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)

def digits(n):
    return map(int, str(n))

def is_increasing(n):
    ds = digits(n)
    return ds != sorted(ds)

def is_decreasing(n):
    ds = digits(n)
    return ds != reversed(sorted(ds))

def is_bouncy(n):
    return not is_increasing(n) and not is_decreasing(n)

def main():
    bouncy = 0
    for n in count(1):
        if is_bouncy(n):
            bouncy += 1
        if Fraction(bouncy, n) == Fraction(99, 100):
            print n
            break

if __name__ == "__main__": main()
