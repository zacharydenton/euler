#!/usr/bin/env python
def triangle(n):
    return n*(n+1)//2

def pentagonal(n):
    return n*(3*n-1)//2

def hexagonal(n):
    return n*(2*n-1)

def main():
    p = set(pentagonal(n) for n in range(100000))
    h = set(hexagonal(n) for n in range(100000))
    for n in range(100000):
        t = triangle(n)
        if t in p and t in h and t > 40755:
            print(t)

if __name__ == "__main__":
    main()
