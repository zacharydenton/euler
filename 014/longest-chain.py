#!/usr/bin/env python
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
print(max_i)
