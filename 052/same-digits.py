#!/usr/bin/env python
# It can be seen that the number, 125874, and its double, 
# 251748, contain exactly the same digits, but in a different order.
# 
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, 
# and 6x, contain the same digits.

def get_digits(n):
    return sorted(str(n))

def same_digits(n, iterations=2):
    digits = get_digits(n)
    for i in range(1, iterations):
        if not digits == get_digits(n+(i*n)):
            return False
    return True

def main():
    n = 0
    found = False
    while not found:
        n += 1
        if same_digits(n,6):
            found = True
    print n

if __name__ == "__main__":
    import cProfile
    cProfile.run('main()')
