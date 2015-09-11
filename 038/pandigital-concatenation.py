#!/usr/bin/env python

def is_pandigital(*args, **kwargs):
    num = sorted(''.join(str(arg) for arg in args))

    try:
        if kwargs['length'] and len(num) != kwargs['length']:
            return False
    except KeyError:
        pass

    for i in range(len(num)):
        if str(i+1) != str(num[i]):
            return False
    return True

def concatenated_product(number, n):
    try:
        return int(''.join(str(number * i) for i in range(1,n+1)))
    except ValueError:
        print(number, n)

def main():
    print(max(concatenated_product(i, n) for i in range(10000) for n in range(1, 10) if is_pandigital(concatenated_product(i, n))))

if __name__ == "__main__":
    main()
