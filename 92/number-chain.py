#!/usr/bin/env python
# A number chain is created by continuously adding the 
# square of the digits in a number to form a new number 
# until it has been seen before.
# 
# For example,
# 
# 44  32  13  10  1  1
# 85  89  145  42  20  4  16  37  58  89
# 
# Therefore any chain that arrives at 1 or 89 will become 
# stuck in an endless loop. What is most amazing is that 
# EVERY starting number will eventually arrive at 1 or 89.
# 
# How many starting numbers below ten million will arrive at 89?

def get_digits(n):
    return [int(d) for d in str(n)]

_cache = {}
def chain(start):
    n = start
    prev = None
    res = []
    while prev != 1 and prev != 89:
        if n in _cache:
            _cache[start] = res[-1]
            return _cache[n]
        res.append(n)
        prev = n
        n = sum(d ** 2 for d in get_digits(n))
    _cache[start] = res[-1]
    return res[-1]

def main():
    count = 0
    for i in range(1,10000000):
        if chain(i) == 89:
            count += 1
    print count

if __name__ == "__main__":
    import cProfile
    cProfile.run('main()')
