from pages import *

def main():
	surface = pygame.display.set_mode((600, 700)) # Initializing surface
	algo_name = "Radix sort"
	N = 512 # Number of elements

	pygame.display.set_caption("Sort Visualization") # Set title

	# Creating logo and buttons
	logo = Button(surface, "Sort Visualization", 50, 30, 150, 500, FONT_PATH_SIGN, 80, True)
	visualize_button =  Button(surface, "Visualize", 150, 220, 50, 300, FONT_PATH_TEXT, 40)
	algo_button = Button(surface, "Algorithm: " + algo_name, 150, 290, 50, 300, FONT_PATH_TEXT, 40)
	elements_button = Button(surface, "Number of elements: " + str(N), 150, 360, 50, 300, FONT_PATH_TEXT, 40)
	info_button = Button(surface, "Information", 150, 430, 50, 300, FONT_PATH_TEXT, 40)
	quit_button = Button(surface, "QUIT", 150, 500, 50, 300, FONT_PATH_TEXT, 40)

	while(True):
		# Drawing everything
		surface.fill((80, 180, 50))
		logo.draw_button()
		visualize_button.draw_button()
		algo_button.draw_button()
		elements_button.draw_button()
		info_button.draw_button()
		quit_button.draw_button()
		pygame.display.update()

		# Event handler
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				# If button clicked, run the assigned function
				if quit_button.rect.collidepoint(pygame.mouse.get_pos()):
					pygame.quit()
					sys.exit()
				elif info_button.rect.collidepoint(pygame.mouse.get_pos()):
					info_page(surface, logo)
				elif algo_button.rect.collidepoint(pygame.mouse.get_pos()):
					algo_name = algorithm_page(surface, logo)
					# assigning new text for button after getting new value
					algo_button = Button(surface, "Algorithm: " + algo_name, 150, 290, 50, 300, FONT_PATH_TEXT, 40)
				elif elements_button.rect.collidepoint(pygame.mouse.get_pos()):
					N = number_page(surface, logo)
					# assigning new text for button after getting new value
					elements_button = Button(surface, "Number of elements: " + str(N), 150, 360, 50, 300, FONT_PATH_TEXT, 40)
				elif visualize_button.rect.collidepoint(pygame.mouse.get_pos()):
					visualize(N, algo_name)
					# Going back to normal display size and title
					surface = pygame.display.set_mode((600, 700))
					pygame.display.set_caption("Sort Visualization")

if __name__ == "__main__":
	main()