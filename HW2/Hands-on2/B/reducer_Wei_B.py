#!/usr/bin/python3
import sys
from math import sqrt


def update(existingAggregate, newValue):
    (count, mean, M2) = existingAggregate
    count += 1
    delta = newValue - mean
    mean += delta / count
    delta2 = newValue - mean
    M2 += delta * delta2
    return (count, mean, M2)


(last_key, last_val) = (None, 0)
(count, mean, M2) = (0, 0, 0)
for line in sys.stdin:
    (key, val) = line.strip().split('\t')
    if last_key and last_key != key:
        print('%s\t%s' % (last_key, str(round(sqrt(M2/count), 2))))
        (last_key, last_val) = (key, val)
        (count, mean, M2) = update((0, 0, 0), float(val))
    else:
        (count, mean, M2) = update((count, mean, M2), float(val))
        last_key = key
if last_key:
    print('%s\t%s' % (last_key, str(round(sqrt(M2/count), 2))))
