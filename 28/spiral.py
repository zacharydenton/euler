#!/usr/bin/env python
# Starting with the number 1 and moving to the 
# right in a clockwise direction a 5 by 5 spiral 
# is formed as follows:
# 
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
# 
# It can be verified that the sum of the numbers 
# on the diagonals is 101.
# 
# What is the sum of the numbers on the diagonals 
# in a 1001 by 1001 spiral formed in the same way?

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

print sum_diagonals_of_spiral(1001)

