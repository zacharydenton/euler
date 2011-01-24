#!/usr/bin/env python
# Starting in the top left corner of a 2x2 grid, there are 6 routes 
# (without backtracking) to the bottom right corner.
#
# How many routes are there through a 20x20 grid?
from pprint import pprint
from gmpy import comb

class Grid:
    def __init__(self, width, height):
        self.grid = [[{'comb(%s,%s)' % (x,y): int(comb(x, y))} for x in range(width)] for y in range(height)]

    def __getitem__(self, pos):
        x = pos[0]
        y = pos[1]
        return self.grid[y][x]

    def __iter__(self):
        for y, row in enumerate(self.grid):
            for x, pos in enumerate(row):
                yield (x, y)

    def __str__(self):
        result = ''
        max_len = max(len(str(self[cell])) for cell in self)
        for row in self.grid:
            for cell in row:
                result += str(cell).center(max_len+1)
            result += '\n'
        return result


    def get_tree(self, pos):
        x = pos[0]
        y = pos[1]
        if x == len(self.grid[0])-1 and y == len(self.grid)-1:
            return Tree(pos, None, None)
        elif x == len(self.grid[0])-1:
            return Tree(pos, self.get_tree((x, y+1)), None)
        elif y == len(self.grid)-1:
            return Tree(pos, None, self.get_tree((x+1, y)))
        else:
            return Tree(pos, self.get_tree((x, y+1)), self.get_tree((x+1, y)))

class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

    def is_leaf(self):
        return self.left is None and self.right is None

def get_leaves(tree):
    res = []
    def get_leaves_iter(tree):
        if tree:
            if tree.is_leaf():
                res.append(tree)
            else:
                get_leaves_iter(tree.left)
                get_leaves_iter(tree.right)
    get_leaves_iter(tree)
    return res

def print_tree(tree, level=0):
    if tree == None: return
    print_tree(tree.right, level+1)
    print '    '*level + str(tree.cargo)
    print_tree(tree.left, level+1)

def num_paths(grid_size):
    return comb(2 * grid_size, grid_size)

def main():
    print num_paths(20)

if __name__ == "__main__":
    import cProfile
    cProfile.run('main()')
