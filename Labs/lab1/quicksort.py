#!/usr/bin/env python

def quicksort(array):
	_quicksort(array,0,len(array)-1)

def _quicksort(A, low, high):
	if low < high:
		pivot_location = _partition(A, low, high)
		_quicksort(A, low, pivot_location - 1)
		_quicksort(A, pivot_location + 1, high)

def _partition(A, low, high):
	pivot = A[low]
	leftwall = low
	for i in xrange(low+1, high+1):
		if A[i] < pivot:
			leftwall = leftwall + 1
			A[i], A[leftwall] = A[leftwall], A[i]
	A[low], A[leftwall] = A[leftwall], A[low]
	return leftwall


def main():
	lst = [3,5,1,7,2,6,8,2]
	quicksort(lst)
	print lst


if __name__=="__main__":
	main()
