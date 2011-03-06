#!/usr/bin/env python
# We shall say that an n-digit number is pandigital if 
# it makes use of all the digits 1 to n exactly once; 
# for example, the 5-digit number, 15234, is 1 through 
# 5 pandigital.
#
# The product 7254 is unusual, as the identity, 
# 39 * 186 = 7254, containing multiplicand, multiplier, 
# and product is 1 through 9 pandigital.
#
# Find the sum of all products whose 
# multiplicand/multiplier/product identity can be written 
# as a 1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one 
# way so be sure to only include it once in your sum.

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

def main():
    pandigital = set()
    total = 0
    for multiplicand in range(1, 5000):
        for multiplier in range(1, 100):
            product = multiplicand * multiplier
            if is_pandigital(multiplicand, multiplier, product, length=9):
                pandigital.add(product)
                #print "%s * %s = %s" % (multiplicand, multiplier, product)
    #print sorted(pandigital)
    print sum(pandigital)

if __name__ == "__main__":
    main()
