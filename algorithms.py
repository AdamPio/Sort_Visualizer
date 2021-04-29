#  Slection sort
# Best case: O(N^2)
# Average case: O(N^2)
# Worst case: O(N^2)
import random
def selection_sort(data):
	for i in range(len(data)):
		min_val = i

		for j in range(i+1, len(data)):
			if data[j] < data[min_val]:
				min_val = j

		data[i], data[min_val] = data[min_val], data[i]
		yield data

# Bubble sort
# Best case: O(N)
# Average case: O(N^2)
# Worst case: O(N^2)
def bubble_sort(data):
	for i in range(len(data)):
		swapped =  False

		for j in range(len(data)-i-1):
			if data[j] > data[j+1]:
				data[j], data[j+1] = data[j+1], data[j]
				yield data
				swapped = True

		if swapped == False:
			break

# Insertion sort
# Best case: O(N)
# Average case: O(N^2)
# Worst case: O(N^2)
def insertion_sort(data):
	for i in range(1, len(data)):
		key = data[i]
		j = i-1
		while j >= 0 and key < data[j]:
			data[j+1] = data[j]
			j -= 1
			yield data
		data[j+1] = key

# Merge sort
# Best case: O(N*log(N))
# Average case: O(N*log(N))
# Worst case: O(N*log(N))
def merge_sort(data, start):
	if len(data) > 1:
		mid = len(data)//2

		L = data[:mid]
		R = data[mid:]

		merge_sort(L, 0)
		merge_sort(R, mid)

		i = j = k = 0

		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				data[k] = L[i]
				i += 1
			else:
				data[k] = R[j]
				j += 1
			k += 1

		while i < len(L):
			data[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			data[k] = R[j]
			j += 1
			k += 1

# Quick sort
# Best case: O(N*log(N))
# Average case: O(N*log(N))
# Worst case: O(N^2)
def quick_sort(data, start, end):
    if start < end:
    	pivot_index = start
    	pivot = data[end]

    	for i in range(start, end):
    		if(data[i] < pivot):
    			data[i], data[pivot_index] = data[pivot_index], data[i]
    			pivot_index += 1
    			yield data

    	data[end], data[pivot_index] = data[pivot_index], data[end]
    	yield data

    	yield from quick_sort(data, start, pivot_index - 1)
    	yield from quick_sort(data, pivot_index + 1, end)

# Heap sort
# Best case: O(N*log(N))
# Average case: O(N*log(N))
# Worst case: O(N*log(N))
def heapify(data, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and data[largest] < data[l]:
        largest = l
 
    if r < n and data[largest] < data[r]:
        largest = r

    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        yield data

        yield from heapify(data, n, largest)

def heap_sort(data):
    n = len(data)

    for i in range(n//2 - 1, -1, -1):
        yield from heapify(data, n, i)

    for i in range(n-1, 0, -1):
        data[i], data[0] = data[0], data[i]
        yield data
        yield from heapify(data, i, 0)

# Comb sort
# Best case: O(N*log(N))
# Average case: O(N^2/2^P) where P is the nuimber of increments
# Worst case: O(N^2)
def getNextGap(gap):
    gap = (gap * 10)/13
    if gap < 1:
        return 1
    return int(gap)
 
def comb_sort(data):
    n = len(data)
 
    gap = n
 
    swapped = True

    while gap !=1 or swapped == 1:

        gap = getNextGap(gap)

        swapped = False

        for i in range(0, n-gap):
            if data[i] > data[i + gap]:
                data[i], data[i + gap]=data[i + gap], data[i]
                swapped = True
                yield data