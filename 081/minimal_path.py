#!/usr/bin/env python
import os
import sys
from collections import defaultdict

def dijkstra(matrix):
    def neighbors(node):
        (x, y) = node
        n = []
        if x < len(matrix[0]) - 1:
            n.append((x + 1, y))
        if y < len(matrix) - 1:
            n.append((x, y + 1))
        return n

    def value(node):
        (x, y) = node
        return matrix[y][x]
    
    current = (0, 0)
    dest = (len(matrix[0]) - 1, len(matrix) - 1)
    unvisited = set((x, y) for x in range(dest[0] + 1) for y in range(dest[1] + 1))
    nodes = {}
    for node in unvisited: nodes[node] = sys.maxsize
    nodes[current] = value(current)

    while 1:
        for node in [n for n in neighbors(current) if n in unvisited]:
            distance = nodes[current] + value(node)
            if distance < nodes[node]:
                nodes[node] = distance

        unvisited.remove(current)
        if current == dest:
            break
        else:
            current = min((nodes[node], node) for node in unvisited)[1]

    return nodes[dest]

def main():
    matrix = []
    with open(os.path.join(os.path.dirname(__file__), "matrix.txt")) as matfile:
        for row in matfile:
            matrix.append([int(n) for n in row.split(',')])

    print(dijkstra(matrix))

if __name__ == "__main__": main()

