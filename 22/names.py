#!/usr/bin/env python
# Using names.txt (right click and 'Save Link/Target As...'), 
# a 46K text file containing over five-thousand first names, 
# begin by sorting it into alphabetical order. Then working 
# out the alphabetical value for each name, multiply this 
# value by its alphabetical position in the list to obtain 
# a name score.
# 
# For example, when the list is sorted into alphabetical order, 
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th 
# name in the list. So, COLIN would obtain a score of 
# 938 * 53 = 49714.
# 
# What is the total of all the name scores in the file?
from string import ascii_uppercase

def calculate_score(name, index):
    alpha_score = sum(ascii_uppercase.index(letter)+1 for letter in name)
    return index * alpha_score

def main():
    names_file = open('names.txt')
    names_string = names_file.read()
    names = [name.strip('"') for name in names_string.split(',')] 
    names.sort()
    print sum(calculate_score(name, index+1) for index, name in enumerate(names))
    names_file.close()

if __name__ == "__main__":
    main()
