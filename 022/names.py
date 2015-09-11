#!/usr/bin/env python
import os
from string import ascii_uppercase

def calculate_score(name, index):
    alpha_score = sum(ascii_uppercase.index(letter)+1 for letter in name)
    return index * alpha_score

def main():
    names_file = open(os.path.join(os.path.dirname(__file__), 'names.txt'))
    names_string = names_file.read()
    names = [name.strip('"') for name in names_string.split(',')] 
    names.sort()
    print(sum(calculate_score(name, index+1) for index, name in enumerate(names)))
    names_file.close()

if __name__ == "__main__":
    main()
