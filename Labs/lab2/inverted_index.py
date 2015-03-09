#!/usr/bin/python
from __future__ import print_function

if raw_input:  input = raw_input



filename = input("filename>> ")
with open(filename) as f:
    data = f.read()
data = re.sub("\"|\.|\!|\?|'|,|;|- | -", "", data)

for word in data.strip().split():
    data.strip().
