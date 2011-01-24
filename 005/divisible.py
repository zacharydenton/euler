#!/usr/bin/env python
# 2520 is the smallest number that can be divided by 
# each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly
# divisible by all of the numbers from 1 to 20?

def is_divisible_to(number, x):
    for i in reversed(range(1, x+1)):
        if number % i != 0:
            return False
    return True

def divisible_to(x):
    if x < 1:
        return False
    elif x == 1:
        return 1
    else:
        step = divisible_to(x-1)
        number = 0
        found = False
        while not found:
            number += step
            found = is_divisible_to(number, x)
        return number

print divisible_to(500)
