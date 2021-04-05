#!/usr/bin/python3
import string
import sys


# get all lines from stdin
for line in sys.stdin:
    val = line.strip()
    words = val.split(' ')
    for word in words:
        for letter in word:
            # remove punctuations from the word 
            punc = '''!()-[]{};:'"\\, <>./?@#$%^&*_~'''
            if letter in punc:
                word = word.replace(letter, '')
        # uniform the word in lower case
        word = word.lower()
        print ('%s\t%s' % (word, 1))
