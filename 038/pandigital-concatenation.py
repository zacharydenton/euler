#!/usr/bin/env python
# Take the number 192 and multiply it by each of 1, 2, and 3:
# 
# 192  1 = 192
# 192  2 = 384
# 192  3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 
# 192384576. We will call 192384576 the concatenated product 
# of 192 and (1,2,3)
# 
# The same can be achieved by starting with 9 and multiplying 
# by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which 
# is the concatenated product of 9 and (1,2,3,4,5).
# 
# What is the largest 1 to 9 pandigital 9-digit number that 
# can be formed as the concatenated product of an integer with 
# (1,2, ... , n) where n > 1?

def is_pandigital(*args, **kwargs):
    num = sorted(''.join(str(arg) for arg in args))

    try:
        if kwargs['length'] and len(num) != kwargs['length']:
            return False
    except KeyError:
        pass

    for i in range(len(num)):
        if str(i+1) != str(num[i]):
            return False
    return True

def concatenated_product(number, n):
    try:
        return int(''.join(str(number * i) for i in range(1,n+1)))
    except ValueError:
        print number, n

def main():
    print max(concatenated_product(i, n) for i in range(10000) for n in range(1, 10) if is_pandigital(concatenated_product(i, n)))

if __name__ == "__main__":
    main()
