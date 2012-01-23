#!/usr/bin/env python
from math import log10
largest = [0, 0]
for i, line in enumerate(open('base_exp.txt')):
    a, x = map(int, line.split(','))
    if x * log10(a) > largest[0]:
        largest = [x * log10(a), i+1]
print largest[1]
