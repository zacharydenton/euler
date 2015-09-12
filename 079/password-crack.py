#!/usr/bin/env python
import os
from itertools import *
from collections import defaultdict

def main():
    attempts = [line.strip() for line in open(os.path.join(os.path.dirname(__file__), 'keylog.txt')).readlines()]
    appearances = defaultdict(list)
    for attempt in attempts:
        for i, n in enumerate(attempt):
            appearances[n].append(i)

    average_positions = {}
    for k,v in list(appearances.items()):
        average_positions[k] = float(sum(v))/float(len(v))

    a = [k for k,v in sorted(list(average_positions.items()), key=lambda a: a[1])]
    print(''.join(str(x) for x in a))

if __name__ == "__main__":
    main()
