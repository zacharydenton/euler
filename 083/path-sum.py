#!/usr/bin/env python2
import os
import heapq

def parse(matfile):
    return [[int(n) for n in row.split(',')] for row in matfile]

def distance(a, b):
    return sum(abs(a[i] - b[i]) for i in range(len(a)))

def astar(matrix, targets, sources):
    def neighbors(position):
        (x, y) = position
        candidates = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        return [(x, y) for (x, y) in candidates if x >= 0 and x < len(matrix)
                                               and y >= 0 and y < len(matrix[0])]

    def evaluate(path):
        f = sum(matrix[y][x] for (x, y) in path)
        h = min(distance(path[-1], target) for target in targets)
        return f + h

    targets = set(targets)
    frontier = set(sources)
    explored = set()
    frontier_queue = []
    for source in sources:
        path = [source]
        heapq.heappush(frontier_queue, (evaluate(path), path))

    while frontier:
        (_, path) = heapq.heappop(frontier_queue)
        frontier.remove(path[-1])
        explored.add(path[-1])
        if path[-1] in targets:
            return path
        for neighbor in neighbors(path[-1]):
            if neighbor not in frontier | explored:
                frontier.add(neighbor)
                new_path = path + [neighbor]
                heapq.heappush(frontier_queue, (evaluate(new_path), new_path))

def main():
    with open(os.path.join(os.path.dirname(__file__), "matrix.txt")) as matfile:
        matrix = parse(matfile)
    targets = [(len(matrix) - 1, len(matrix[0]) - 1)]
    sources = [(0, 0)]
    print(sum(matrix[y][x] for (x, y) in astar(matrix, targets, sources)))

if __name__ == "__main__": main()
