#!/usr/bin/env python
import gmpy
count = 0
for n in range(1, 101):
    for r in range(1, n):
        c = gmpy.comb(n,r)
        if c > 1000000:
            count += 1
print count
