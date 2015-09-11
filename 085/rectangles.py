#!/usr/bin/env python
from operator import mul

def pack(w, h):
    return (w + 1) * (h + 1) * (w * h) / 4

def f(x, y):
    return abs(pack(x, y) - 2000000)

def main():
    candidates = ((x, y) for x in range(1000) for y in range(1000))
    print((mul(*min((f(*pair), pair) for pair in candidates)[1])))

if __name__ == "__main__": main()
