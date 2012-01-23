#!/usr/bin/env python
import os
import operator

numerals = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

def subtractive(roman):
    result = roman
    replacements = [
        ("VIIII", "IX"), 
        ("IIII", "IV"), 
        ("LXXXX", "XC"), 
        ("XXXX", "XL"),
        ("DCCCC", "CM"), 
        ("CCCC", "CD"),
    ]
    for old, new in replacements:
        result = result.replace(old, new)
    return result

current = 0
improved = 0
for line in open(os.path.join(os.path.dirname(__file__), 'roman.txt')):
    roman = line.strip()
    current += len(roman)
    improved += len(subtractive(roman))
print current - improved
