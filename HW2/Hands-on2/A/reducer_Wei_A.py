#!/usr/bin/python3
import sys
from operator import itemgetter

items = []
new_items = []
(last_key, count) = (None, 0)
for line in sys.stdin:
    (key, val) = line.strip().split('\t')
    if last_key and last_key != key:
        # print('%s\t%s' % (last_key, count))
        items.append((last_key, count))
        (last_key, count) = (key, 1)
    else:
        (last_key, count) = (key, count + 1)
if last_key:
    # print('%s\t%s' % (last_key, count))
    items.append((last_key, count))
    
items = sorted(items, key = itemgetter(1), reverse = True)
for item in items:
	new_items.append('%s\t%s' % (item[0], item[1]))

for newItem in new_items[0:10]:
	print(newItem)

