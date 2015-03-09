#!/usr/bin/python
import re

def readFileToList(filename):
	with open(filename) as f:
		data = f.read()
	data = re.sub("\"|\.|\!|\?|'|,|;|- | -", "", data)
	return {s.lower() for s in data.strip().split()}


set1 = readFileToList(raw_input("first filename>> "))
set2 = readFileToList(raw_input("second filename>> "))

print sum([1 for word in set1 if word in set2])

