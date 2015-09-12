#!/usr/bin/env python
def sum_diagonals_of_spiral(size):
    n = 1
    step = 2
    total = 0
    since_last = 0
    while n <= size**2:
        total += n
        n += step
        since_last += 1
        if since_last == 4:
            step += 2
            since_last = 0
    return total

print(sum_diagonals_of_spiral(1001))
