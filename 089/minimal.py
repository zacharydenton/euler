#!/usr/bin/env python
import os

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
print(current - improved)
