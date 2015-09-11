#!/usr/bin/env python
from gmpy2 import comb
count = 0
for n in range(1, 101):
    for r in range(1, n):
        c = comb(n,r)
        if c > 1000000:
            count += 1
print(count)
