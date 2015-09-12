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

def main():
    pandigitals = set()
    total = 0
    for multiplicand in range(1, 5000):
        for multiplier in range(1, 100):
            product = multiplicand * multiplier
            if is_pandigital(multiplicand, multiplier, product, length=9):
                pandigitals.add(product)
    print(sum(pandigitals))

if __name__ == "__main__":
    main()
