import pygame
import sys

# Drawing our data
def update_data(surface, data, swap1 = None, swap2 = None):
	# Depending on number of elements we will have
	# various spaces and thickness
	k = 1024/len(data)
	surface.fill((255, 255, 255))
	for i in range(len(data)):
		color = (0, 0, 0)
		# If numbers are swapping we highlight them
		if i == swap1:
			color = (0, 255, 0)
		elif i == swap2:
			color = (255, 0, 0)
		pygame.draw.rect(surface, color, (i*k, 512-(data[i]*(k/2)), 1*k, data[i]*(k/2)))
	pygame.display.update()

# Function that helps us check if QUIT was clicked during
# work of algorithm
def end_check():
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

class Algorithm:
	def __init__(self, algo, data, surface):
		self.surface = surface
		self.data = data
		algorithms = {"Selection sort" : self.selection_sort,
		"Bubble sort" : self.bubble_sort,
		"Insertion sort" : self.insertion_sort,
		"Merge sort" : self.mergesort,
		"Quick sort" : self.quick_sort,
		"Heap sort" : self.heap_sort,
		"Comb sort" : self.comb_sort}
		self.sort = algorithms[algo]

#########################################################################################################################################
	#  Selection sort
	def selection_sort(self):
		for i in range(len(self.data)):
			min_val = i

			for j in range(i+1, len(self.data)):
				if self.data[j] < self.data[min_val]:
					min_val = j

			self.data[i], self.data[min_val] = self.data[min_val], self.data[i]
			update_data(self.surface, self.data, i, min_val)
			end_check()
		return True

#########################################################################################################################################
	# Bubble sort
	def bubble_sort(self):
		for i in range(len(self.data)):
			swapped =  False

			for j in range(len(self.data)-i-1):
				if self.data[j] > self.data[j+1]:
					self.data[j], self.data[j+1] = self.data[j+1], self.data[j]
					swapped = True

					update_data(self.surface, self.data, j, j+1)
					end_check()

			if swapped == False:
				break

		return True

#########################################################################################################################################
	# Insertion sort
	def insertion_sort(self):
		for i in range(1, len(self.data)):
			key = self.data[i]
			j = i-1
			while j >= 0 and key < self.data[j]:
				self.data[j+1] = self.data[j]
				j -= 1

			self.data[j+1] = key
			update_data(self.surface, self.data, j+1, i)
			end_check()

		return True

#########################################################################################################################################
	# Merge sort
	# in this program is used iterative version of merge sort
	# to facilitate visualization
	def mergesort(self, data=[]):
		def merge(data, l, m, r):
			n1 = m - l + 1
			n2 = r - m
			L = [0] * n1
			R = [0] * n2
			for i in range(0, n1):
				L[i] = data[l + i]
			for i in range(0, n2):
				R[i] = data[m + i + 1]

			i, j, k = 0, 0, l
			while i < n1 and j < n2:
				if L[i] > R[j]:
					data[k] = R[j]
					j += 1
				else:
					data[k] = L[i]
					i += 1
				update_data(self.surface, self.data, k)
				end_check()
				k += 1

			while i < n1:
				data[k] = L[i]
				update_data(self.surface, self.data, k)
				end_check()
				i += 1
				k += 1

			while j < n2:
				data[k] = R[j]
				update_data(self.surface, self.data, k)
				end_check()
				j += 1
				k += 1

		if data == []:
			data = self.data

		current_size = 1

		while current_size < len(data) - 1:
			left = 0

			while left < len(data) - 1:
				mid = min((left + current_size - 1), len(data) - 1)

				R = ((2 * current_size + left - 1, len(data) - 1)[2 * current_size + left - 1 > len(data) - 1])

				merge(data, left, mid, R)
				left += current_size * 2

			current_size *= 2

		return True

#########################################################################################################################################
	# Quick sort
	def quick_sort(self, data=[], start=0, end=0):
		if data == []:
			data = self.data
			end = len(data) - 1

		if start < end:
			pivot_index = start
			pivot = data[end]

			for i in range(start, end):
				if(data[i] < pivot):
					data[i], data[pivot_index] = data[pivot_index], data[i]
					pivot_index += 1
					update_data(self.surface, data)
					end_check()

			data[end], data[pivot_index] = data[pivot_index], data[end]
			update_data(self.surface, data, end, pivot_index)
			end_check()

			self.quick_sort(data, start, pivot_index - 1)
			self.quick_sort(data, pivot_index + 1, end)

#########################################################################################################################################
	# Heap sort
	def heapify(self, data, n, i):
	    largest = i
	    l = 2 * i + 1
	    r = 2 * i + 2

	    if l < n and self.data[largest] < self.data[l]:
	        largest = l
	 
	    if r < n and self.data[largest] < self.data[r]:
	        largest = r

	    if largest != i:
	        self.data[i], self.data[largest] = self.data[largest], self.data[i]
	        update_data(self.surface, self.data, i, largest)
	        end_check()

	        self.heapify(data, n, largest)

	def heap_sort(self):
	    n = len(self.data)

	    for i in range(n//2 - 1, -1, -1):
	        self.heapify(self.data, n, i)

	    for i in range(n-1, 0, -1):
	        self.data[i], self.data[0] = self.data[0], self.data[i]
	        self.heapify(self.data, i, 0)

	        end_check()
	    return True

#########################################################################################################################################
	# Comb sort
	def getNextGap(self, gap):
	    gap = (gap * 10)/13
	    if gap < 1:
	        return 1
	    return int(gap)
	 
	def comb_sort(self):
	    n = len(self.data)
	 
	    gap = n
	 
	    swapped = True

	    while gap !=1 or swapped == 1:

	        gap = self.getNextGap(gap)

	        swapped = False

	        for i in range(0, n-gap):
	            if self.data[i] > self.data[i + gap]:
	                self.data[i], self.data[i + gap] = self.data[i + gap], self.data[i]
	                swapped = True

	                update_data(self.surface, self.data, i, i+gap)
	                end_check()
	    return True