#!/usr/bin/python3
import sys

(last_key, last_v1, last_v2, last_v3, last_v4) = (None, 0, 0, 0, 0)
count = 0
for line in sys.stdin:
    (key, v1, v2, v3, v4) = line.strip().split('\t')
    if last_key and last_key != key:
        last_v1 = str(round(float(last_v1/count), 2))
        last_v2 = str(round(float(last_v2/count), 2))
        last_v3 = str(round(float(last_v3/count), 2))
        last_v4 = str(round(float(last_v4/count), 2))
        print('%s\t%s\t%s\t%s\t%s' % (last_key, last_v1, last_v2, last_v3, last_v4))
        count = 1
        (last_key, last_v1, last_v2, last_v3, last_v4) = (key, v1, v2, v3, v4)
    else:
        count += 1
        (last_key, last_v1, last_v2, last_v3, last_v4) = (key, float(last_v1) + float(v1), float(last_v2) + float(v2), float(last_v3) + float(v3), float(last_v4) + float(v4))
if last_key:
    last_v1 = str(round(float(last_v1/count), 2))
    last_v2 = str(round(float(last_v2/count), 2))
    last_v3 = str(round(float(last_v3/count), 2))
    last_v4 = str(round(float(last_v4/count), 2))
    print('%s\t%s\t%s\t%s\t%s' % (last_key, last_v1, last_v2, last_v3, last_v4))