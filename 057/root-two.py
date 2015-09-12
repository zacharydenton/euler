#!/usr/bin/env python
import fractions

def root_two(iterations):
    d = fractions.Fraction(1/2)
    for i in range(iterations):
        d = fractions.Fraction(1/(2+d))
        yield 1 + d

def main():
    print(len([f for f in root_two(1000) if len(str(f.numerator)) > len(str(f.denominator))]))

if __name__ == "__main__":
    main()
