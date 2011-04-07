#!/usr/bin/env python
from itertools import *
from string import *
from collections import defaultdict
from operator import itemgetter

dictionary = set(word.strip() for word in open('/usr/share/dict/words').readlines())

def ncycle(iterable, n):
    c = cycle(iterable)
    for i in range(n):
        yield c.next()

def decipher(cipher, password):
    key = list(ncycle(password, len(cipher)))

    for c, k in zip(cipher, key):
        yield chr(c ^ k)

def dictionary_words(words):
    return [word for word in words if word.lower() in dictionary]

def is_english(plaintext):
    frequency = defaultdict(int)
    for char in plaintext:
        frequency[char] += 1
    f = sorted(frequency.iteritems(), key=itemgetter(1), reverse=True)
    top = [k for k,v in f[:4]]
    if ' ' in top and 'e' in top and 't' in top:
        words = plaintext.split()
        if float(len(dictionary_words(words))) / float(len(words)) > 0.5:
            return True
    return False

def main():
    cipher = [int(c) for c in open('cipher1.txt').read().strip().split(',')]

    candidates = ascii_lowercase

    passwords = product(candidates, candidates, candidates)
    for p in passwords:
        password = [ord(c) for c in p]
        plaintext = ''.join(list(decipher(cipher, password)))
        if is_english(plaintext):
            print sum(ord(c) for c in plaintext)
            return

if __name__ == "__main__":
    main()
