#!/usr/bin/env python
def find_max_peek(triangle):
    """
    basically it goes through each level of the triangle,
    and picks the next option with the highest value.
    it only looks ahead one row.
    """
    def get_options(row, index):
        options = []
        try:
            options.append(triangle[row+1][index])
            options.append(triangle[row+1][index+1])
        except:
            pass
        return options

    current = 0
    res = []
    for i, row in enumerate(triangle):
        best = 0
        res.append(row[current])
        next_index = 0
        for j, option in enumerate(get_options(i, current)):
            if option > best:
                best = option
                next_index = j + current
        current = next_index
    return res

def find_max_brute(triangle):
    """
    calculates all possible paths,
    and figures out which one is best.
    """
    paths = []
    def get_options(row, index):
        options = []
        try:
            options.append(triangle[row+1][index])
            options.append(triangle[row+1][index+1])
        except:
            pass
        return options

    def get_paths(path, row, index):
        try:
            left = triangle[row+1][index]
            right = triangle[row+1][index+1]
        except:
            left = None
            right = None
        if left is None and right is None:
            paths.append(path)
            return
        else:
            get_paths(path + [left], row+1, index)
            get_paths(path + [right], row+1, index+1)
    
    get_paths([triangle[0][0]], 0, 0)
    max_sum = max(sum(path) for path in paths)
    max_paths = [path for path in paths if sum(path) == max_sum]
    return max_paths[0]

def print_triangle(triangle):
    max_row = len(' '.join("%02i" % item for item in triangle[-1]))
    max_item = max(len(str(item)) for item in triangle[-1])
    tri_str = ''
    for row in triangle:
        row_str = ''
        for item in row:
            row_str += "%02i".center(max_item) % (item) + ' '
        row_str = row_str.center(max_row)
        tri_str += row_str + '\n'
    print tri_str

triangle_str = '''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''
triangle = [[int(num) for num in line.strip().split()] for line in triangle_str.splitlines() if line]
#import random
#triangle = [[random.randint(1, 100) for i in range(x)] for x in range(1,1000)]

#print triangle_str
#for row in triangle:
    #print row
#print find_max_peek(triangle)
#print sum([int(node) for node in find_max_peek(triangle)])
print find_max_brute(triangle)
print sum(path for path in find_max_brute(triangle))
print_triangle(triangle)

