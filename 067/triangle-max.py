#!/usr/bin/env python
import os

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
    triangle = [[int(digit) for digit in line.split()] for line in open(os.path.join(os.path.dirname(__file__), 'triangle.txt')).readlines()]
    print(find_sum(triangle))

if __name__ == "__main__":
    main()
