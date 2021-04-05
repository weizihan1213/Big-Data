#!/usr/bin/python3
import string 
import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split('	')
    for word in words[2:5:2]:
        print(str(word), end ='\t')
    print()