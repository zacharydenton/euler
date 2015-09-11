#!/usr/bin/env python
from fractions import gcd

print(sum(1 for d in range(2, 12001) for n in range(1, d) if (n*3 > d) and (n*2 < d) and gcd(n, d) == 1))

