#!/usr/bin/python3
import sys
import string


for line in sys.stdin:
    line = line.strip()
    words = line.split(',')
    words.insert(0, words.pop())
    for word in words:
        print(word, end='\t')
    print()