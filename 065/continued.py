#!/usr/bin/env python
from itertools import islice

def take(iterable, n):
    return list(islice(iterable, n))

def e():
    yield 2
    k = 1
    while True:
        yield 1
        yield 2*k
        yield 1
        k += 1

def rationalize(frac):
    if len(frac) == 0:
        return (1, 0)
    elif len(frac) == 1:
        return (frac[0], 1)
    else:
        remainder = frac[1:len(frac)]
        (num, denom) = rationalize(remainder)
        return (frac[0] * num + denom, num)

numerator = rationalize(take(e(), 100))[0]
print(sum(int(d) for d in str(numerator)))
