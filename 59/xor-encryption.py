#!/usr/bin/env python
# Each character on a computer is assigned a unique code 
# and the preferred standard is ASCII (American Standard 
# Code for Information Interchange). For example, 
# uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
# 
# A modern encryption method is to take a text file, convert 
# the bytes to ASCII, then XOR each byte with a given value, 
# taken from a secret key. The advantage with the XOR 
# function is that using the same encryption key on the 
# cipher text, restores the plain text; for example, 
# 65 XOR 42 = 107, then 107 XOR 42 = 65.
# 
# For unbreakable encryption, the key is the same length as 
# the plain text message, and the key is made up of random 
# bytes. The user would keep the encrypted message and the 
# encryption key in different locations, and without both 
# "halves", it is impossible to decrypt the message.
# 
# Unfortunately, this method is impractical for most users, 
# so the modified method is to use a password as a key. If 
# the password is shorter than the message, which is likely, 
# the key is repeated cyclically throughout the message. 
# The balance for this method is using a sufficiently long 
# password key for security, but short enough to be memorable.
# 
# Your task has been made easy, as the encryption key consists 
# of three lower case characters. Using cipher1.txt (right click 
# and 'Save Link/Target As...'), a file containing the encrypted 
# ASCII codes, and the knowledge that the plain text must 
# contain common English words, decrypt the message and find 
# the sum of the ASCII values in the original text.
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
    import cProfile
    cProfile.run('main()')
    #main()
