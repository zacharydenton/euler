#!/usr/bin/env python

def is_palindrome(s):
    return s == ''.join(reversed(s))

def is_lychrel(n):
    s = str(n)
    i = 0
    done = False
    while not done:
        if i > 50:
            return True
        s = str(int(s) + int(''.join(reversed(s))))
        i += 1
        if is_palindrome(s):
            done = True
    return False

def main():
    count = 0
    for n in range(10000):
        if is_lychrel(n):
            count += 1
    print(count) 

if __name__ == "__main__":
    main()
