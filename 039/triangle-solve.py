#!/usr/bin/env python
# If p is the perimeter of a right angle triangle with 
# integral length sides, {a,b,c}, there are exactly three 
# solutions for p = 120.
# 
# {20,48,52}, {24,45,51}, {30,40,50}
# 
# For which value of p < 1000, is the number of solutions 
# maximised?
from collections import defaultdict

def is_triple(a,b,c):
    if (0 < a < b < c) and (a**2 + b**2 == c**2):
        return True
    return False
        
def solve_triangle(perimeter, limit=None):
    if limit is None:
        limit = perimeter
    for a in range(1, limit+1):
        for b in range(a, limit+1):
            for c in range(b, limit+1):
                if a+b+c == perimeter:
                    if is_triple(a,b,c):
                        yield (a,b,c)

def calculate_solutions(limit):
    res = defaultdict(list)
    for a in range(1, limit+1):
        for b in range(a, limit+1):
            for c in range(b, limit+1):
                if a**2 + b**2 == c**2:
                    res[a+b+c].append((a,b,c))
    return res
            
def main():
    solutions = calculate_solutions(500)
    most = max(len(s) for s in solutions.values())
    for p, s in sorted(solutions.items()):
        if len(s) == most:
            print p

if __name__ == "__main__":
    main()
