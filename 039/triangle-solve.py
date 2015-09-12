#!/usr/bin/env python
from collections import defaultdict
        
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
    most = max(len(s) for s in list(solutions.values()))
    for p, s in sorted(solutions.items()):
        if len(s) == most:
            print(p)

if __name__ == "__main__":
    main()
