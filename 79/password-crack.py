#!/usr/bin/env python
# A common security method used for online banking is to 
# ask the user for three random characters from a passcode. 
# For example, if the passcode was 531278, they may ask 
# for the 2nd, 3rd, and 5th characters; the expected reply 
# would be: 317.
# 
# The text file, keylog.txt, contains fifty successful 
# login attempts.
# 
# Given that the three characters are always asked for in 
# order, analyse the file so as to determine the shortest 
# possible secret passcode of unknown length.
from itertools import *
from collections import defaultdict

def possibilities(seq,length=7):
    # seq is seq with length 3
    # we need to put combine it into a length 6
    slots = sorted(set(permutations('111'+'0'*(length-3))))
    for slot in slots:
        slot = list(slot)
        j = 0
        for i,s in enumerate(slot):
            if s == '1':
                slot[i] = seq[j]
                j += 1

        yield slot

def main():
    appearances = defaultdict(list)
    attempts = [line.strip() for line in open('keylog.txt').readlines()]
    for attempt in attempts:
        for i, n in enumerate(attempt):
            appearances[n].append(i)
    for k,v in appearances.items():
        appearances[k] = float(sum(v))/float(len(v))
    import operator
    a = [k for k,v in sorted(appearances.items(),key=operator.itemgetter(1))]
    print ''.join(str(x) for x in a)
if __name__ == "__main__":
    main()

    
