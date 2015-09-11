#!/usr/bin/env python
from collections import defaultdict
def cube(x): return x**3

def main():
    cubes = defaultdict(list)
    for i in range(10000):
        c = cube(i)
        digits = ''.join(sorted([d for d in str(c)]))
        cubes[digits].append(c)
    print(min([min(v) for k, v in list(cubes.items()) if len(v) == 5]))

if __name__ == "__main__":
    main()
