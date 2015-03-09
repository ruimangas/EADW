#!/usr/bin/python
import quicksort

filename = raw_input("filename>> ")

with open(filename) as f:
	arr = map(int, f.readlines())

quicksort.quicksort(arr)
print arr
