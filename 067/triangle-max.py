#!/usr/bin/env python
# By starting at the top of the triangle below and moving to 
# adjacent numbers on the row below, the maximum total from 
# top to bottom is 23.
# 
# 3
# 7 4
# 2 4 6
# 8 5 9 3
# 
# That is, 3 + 7 + 4 + 9 = 23.
# 
# Find the maximum total from top to bottom in triangle.txt 
# (right click and 'Save Link/Target As...'), a 15K text file 
# containing a triangle with one-hundred rows.
# 
# NOTE: This is a much more difficult version of Problem 18. 
# It is not possible to try every route to solve this problem, 
# as there are 299 altogether! If you could check one trillion 
# (10^12) routes every second it would take over twenty billion 
# years to check them all. There is an efficient algorithm to 
# solve it. ;o)
def find_sum(triangle):
    def get_options(row, index):
        return triangle[row+1][index], triangle[row+1][index+1]
    row = len(triangle) - 2
    while True:
        try:
            for index, node in enumerate(triangle[row]):
                best = max([node + option for option in get_options(row, index)])
                triangle[row][index] = best
            row -= 1
        except:
            return triangle[0][0]

def main():
    triangle = [[int(digit) for digit in line.split()] for line in open('triangle.txt').readlines()]
    print find_sum(triangle)

if __name__ == "__main__":
    main()
