#!/usr/bin/env python

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
    print(n)

if __name__ == "__main__":
    main()
