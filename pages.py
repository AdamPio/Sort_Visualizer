import os
import random
from algorithms import *
pygame.init()

# INIT
FONT_PATH_SIGN = os.path.join("Fonts", "Bombing.ttf")
FONT_PATH_TEXT = os.path.join("Fonts", "leaves_and_ground.ttf")
FONT_PATH_INFO = os.path.join('Fonts', "Louis George Cafe Bold.ttf")

class Button:
	def __init__(self, surface, text, x, y, h, w, font, size, sign =  False):
		self.rect = pygame.Rect(x, y, w, h)
		self.text = text
		self.font = font
		self.size = size
		self.surface = surface
		self.sign = sign

	def draw_button(self):
		# If it is sign we just want it to have one color
		if self.sign == True:
			color = (180, 210, 180)
		# If it is button
		else:
			# if mouse is hovered on a button, different color and different if it is not
			if self.rect.collidepoint(pygame.mouse.get_pos()):
				color = (200, 255, 40)
			else:
				color = (180, 210, 180)

		pygame.draw.rect(self.surface, color, self.rect)
		points = [self.rect.topleft, self.rect.topright, self.rect.bottomright, self.rect.bottomleft]
		pygame.draw.lines(self.surface, (0, 0, 0), True, points, 3)

		font = pygame.font.Font(self.font, self.size)
		text = font.render(self.text, True, (0, 0, 0))
		textRect = text.get_rect()
		textRect.center = self.rect.center
		self.surface.blit(text, textRect)

def visualize(N, algo_name):
	# Setting new title
	text = "Sort Visualization    Algorithm: %s   Number of Elemetents: %s   Sorting: In progress"% (algo_name, N)
	pygame.display.set_caption(text)

	surface = pygame.display.set_mode((1024, 512)) # Changing display to bigger size to show up to 1024 elements
	data = []
	for i in range(N):
		number = random.randint(0, N)
		data.append(number)
	Sorter = Algorithm(algo_name, data, surface) # Get sorting algorithm


	while(True):
		# Drawing everything during sorting
		done = Sorter.sort() # Run algorithm
		pygame.display.update()

		# Getting true == end of the algorithm
		if done == True:
			break
		elif done == False:
			return

	# Setting new title
	text = "Sort Visualization    Algorithm: %s   Number of Elemetents: %s   Sorting: Done   Click Exit to go back"% (algo_name, N)
	pygame.display.set_caption(text)
	while(True):
		# Wait with sorted data until user exits
		update_data(surface, data)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

def algorithm_page(surface, logo):
	# Creating list of algorithms
	algorithms = ["Selection sort", "Bubble sort", "Insertion sort", "Merge sort", "Quick sort", "Heap sort", "Comb sort", "Radix sort"]

	# Creating buttons
	selection_button = Button(surface, "Selection sort", 70, 220, 50, 200, FONT_PATH_TEXT, 40)
	bubble_button = Button(surface, "Bubble sort", 330, 220, 50, 200, FONT_PATH_TEXT, 40)
	insertion_button = Button(surface, "Insertion sort", 70, 290, 50, 200, FONT_PATH_TEXT, 40)
	merge_button = Button(surface, "Merge sort", 330, 290, 50, 200, FONT_PATH_TEXT, 40)
	quick_button = Button(surface, "Quick sort", 70, 360, 50, 200, FONT_PATH_TEXT, 40)
	heap_button = Button(surface, "Heap sort", 330, 360, 50, 200, FONT_PATH_TEXT, 40)
	comb_button = Button(surface, "Comb sort", 70, 430, 50, 200, FONT_PATH_TEXT, 40)
	radix_button = Button(surface, "Radix sort", 330, 430, 50, 200, FONT_PATH_TEXT, 40)

	while(True):
		# Drawing everything
		surface.fill((80, 180, 50))
		logo.draw_button()
		selection_button.draw_button()
		bubble_button.draw_button()
		insertion_button.draw_button()
		merge_button.draw_button()
		quick_button.draw_button()
		heap_button.draw_button()
		comb_button.draw_button()
		radix_button.draw_button()
		pygame.display.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				# Returning new value (algorithm name) which depends on the clicked button
				if selection_button.rect.collidepoint(pygame.mouse.get_pos()):
					return algorithms[0]
				elif bubble_button.rect.collidepoint(pygame.mouse.get_pos()):
					return algorithms[1]
				elif insertion_button.rect.collidepoint(pygame.mouse.get_pos()):
					return algorithms[2]
				elif merge_button.rect.collidepoint(pygame.mouse.get_pos()):
					return algorithms[3]
				elif quick_button.rect.collidepoint(pygame.mouse.get_pos()):
					return algorithms[4]
				elif heap_button.rect.collidepoint(pygame.mouse.get_pos()):
					return algorithms[5]
				elif comb_button.rect.collidepoint(pygame.mouse.get_pos()):
					return algorithms[6]
				elif radix_button.rect.collidepoint(pygame.mouse.get_pos()):
					return algorithms[7]

def number_page(surface, logo):
	# Creating buttons
	button_1024 = Button(surface, "1024", 150, 220, 50, 300, FONT_PATH_TEXT, 40)
	button_512 = Button(surface, "512", 150, 290, 50, 300, FONT_PATH_TEXT, 40)
	button_256 = Button(surface, "256", 150, 360, 50, 300, FONT_PATH_TEXT, 40)
	button_128 = Button(surface, "128", 150, 430, 50, 300, FONT_PATH_TEXT, 40)

	while(True):
		# Drawing everything
		surface.fill((80, 180, 50))
		logo.draw_button()
		button_1024.draw_button()
		button_512.draw_button()
		button_256.draw_button()
		button_128.draw_button()
		pygame.display.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				# Returning new value (number of elements) which depends on the clicked button
				if button_1024.rect.collidepoint(pygame.mouse.get_pos()):
					return 1024
				elif button_512.rect.collidepoint(pygame.mouse.get_pos()):
					return 512
				elif button_256.rect.collidepoint(pygame.mouse.get_pos()):
					return 256
				elif button_128.rect.collidepoint(pygame.mouse.get_pos()):
					return 128


# Made function to display three quotes string
def blit_text(surface, text, x, y, font_size, spacing = 25):
	font = pygame.font.Font(FONT_PATH_INFO, font_size)
	for line in text.splitlines():
		note = font.render(line, True, (220, 220, 220))
		noteRect = note.get_rect()
		noteRect.midtop = (x, y)
		surface.blit(note, noteRect)
		y += spacing

def info_page(surface, logo):
	# Creating text and button
	info_text = """Sort Visualization is a program that
	visualize how work chosen sorting algorithm.
	This program is used only for visualization and
	should never be used for time comparison, because
	most of the time is spend for drawing every frame of sorting
	process, not sorting our array.

	Algorithms:
	Selection sort, Bubble sort, Insertion sort,
	Merge sort, Quick sort, Heap sort, Comb sort"""

	back_button = Button(surface, "Back", 150, 610, 50, 300, FONT_PATH_TEXT, 40)

	while(True):
		# Drawing everything
		surface.fill((80, 180, 50))
		logo.draw_button()
		back_button.draw_button()
		blit_text(surface, info_text, 300, 230, 24)
		pygame.display.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			# Going back after clicking
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if back_button.rect.collidepoint(pygame.mouse.get_pos()):
					return