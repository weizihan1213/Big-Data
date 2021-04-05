#!/usr/bin/python3
import sys

(last_client, last_file) = (None, None)
total = 0
for line in sys.stdin:
	(client, file) = line.strip().split('\t')
	if last_client == client and last_file != file:
		total += 1
		(last_client, last_file) = (client, file)
	elif last_client == client and last_file == file:
		(last_client, last_file) = (client, file)
	elif not last_client:
		(last_client, last_file) = (client, file)
		total = 1
	else:
		print('%s\t%s' % (last_client, str(total)))
		(last_client, last_file) = (client, file)
		total = 1
if last_client:
	print('%s\t%s' % (last_client, str(total)))