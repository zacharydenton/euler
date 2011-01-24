#!/usr/bin/env python
# The following iterative sequence is defined for the set of positive integers:
#
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13  40  20  10  5  16  8  4  2  1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 
# terms. Although it has not been proved yet (Collatz Problem), it is thought that all
# starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

def next_collatz(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3*n + 1

def collatz(start):
    if start < 1:
        raise ValueError("start must be greater than or equal to 1")
    elif start == 1:
        return [1]

    res = [start]
    done = False
    while not done:
        res += [next_collatz(res[-1])]
        if res[-1] == 1: done = True
    return res

_collatz_cache = {}
def lencollatz(start):
    if start < 1:
        raise ValueError("start must be greater than or equal to 1")
    elif start == 1:
        return 1

    n = start
    length = 1
    done = False
    while not done:
        n = next_collatz(n)
        try:
            length += _collatz_cache[n]
            done = True
        except:
            length += 1
            if n == 1: done = True
    _collatz_cache[start] = length
    return length

max_len = 0
max_i = None
for i in range(1, 1000000):
    l = lencollatz(i)
    if l > max_len:
        max_len = l
        max_i = i
print max_i
