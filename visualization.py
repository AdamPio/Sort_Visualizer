import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import algorithms as algo

N = 100
data = random.sample(range(1, N+1), N)

def update_fig(data, rects, iteration, text):
	for rect, val in zip(rects, data):
		rect.set_height(val)
	iteration[0] += 1
	text.set_text("# of operations: {}".format(iteration[0]))

def main():
	print("""
		1 - Selection sort
		2 - Bubble sort
		3 - Insertion sort
		4 - Merge sort
		5 - Quick sort
		6 - Heap sort
		7 - Comb sort
		""")
	choice = int(input("Prosze wybrac algorytm sortujacy: "))
	# create a list of integers
	if choice == 1:
		title = "Selection sort"
		solver = algo.selection_sort(data)
	elif choice == 2:
		title = "Bubble sort"
		solver = algo.bubble_sort(data)
	elif choice == 3:
		title = "Insertion sort"
		solver = algo.insertion_sort(data)
	elif choice == 4:
		title = "Merge Sort"
		solver = algo.merge_sort(data)
		return
	elif choice == 5:
		title = "Quick sort"
		solver = algo.quick_sort(data, 0, N-1)
	elif choice == 6:
		title = "Heap sort"
		solver = heap_sort(data)
	elif choice == 7:
		title = "Comb sort"
		solver = comb_sort(data)

	# Creating plot with values and counter
	fig, ax = plt.subplots()
	ax.set_title(title)
	bar_rects  = ax.bar(range(len(data)), data, align="edge")
	text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

	# Animation
	iteration = [0]
	anim = animation.FuncAnimation(fig, func=update_fig,
		fargs=(bar_rects, iteration, text), frames=solver, interval=1, repeat=False)
	plt.show()

if __name__ == "__main__":
	main()