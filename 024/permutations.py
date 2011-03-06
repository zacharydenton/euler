#!/usr/bin/env python
# A permutation is an ordered arrangement of objects. 
# For example, 3124 is one possible permutation of the 
# digits 1, 2, 3 and 4. If all of the permutations are 
# listed numerically or alphabetically, we call it 
# lexicographic order. The lexicographic permutations 
# of 0, 1 and 2 are:
# 
# 012   021   102   120   201   210
# 
# What is the millionth lexicographic permutation of the 
# digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
def permutations(array):
    a = array[:]
    yield a

    done = False
    prev = a[:]
    while not done:
        N = len(a)
        i = len(a) - 1
    
        while a[i-1] >= a[i]:
            i -= 1
    
        j = N
    
        while a[j-1] <= a[i-1]:
            j -= 1
    
        a[i-1], a[j-1] = a[j-1], a[i-1]
    
        i += 1
        j = N
    
        while i < j:
            a[i-1], a[j-1] = a[j-1], a[i-1]
            i += 1
            j -= 1
    
        if int(''.join(a)) > int(''.join(prev)):
            yield a
        else:
            done = True
        prev = a[:]
    
array = [digit for digit in '0123456789']
#from itertools import permutations
for i, x in enumerate(permutations(array)):
    if i == 999999:
        print i+1, ''.join(x)
        break
