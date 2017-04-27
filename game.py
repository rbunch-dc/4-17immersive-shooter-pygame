# The reason you have access to this moduel, is because you ran
# $ pip install pygame
# Pygame is NOT part of core (like math or random is)
import pygame
# Import the player class from Player
from player import Player
# Import check_events from the game_functions module
from game_functions import check_events

# The core game functionallity/loop
def run_game():
	# Init all the pygame stuff
	pygame.init()
	# Set up a tuple for the screensize, (horiz,vert)
	screen_size = (1000,800)
	# Set up a tuple for the bg color
	background_color = (82,111,53)

	# Create a pygame screen to use 
	screen = pygame.display.set_mode(screen_size)
	# Set a caption on the terminal window
	pygame.display.set_caption("A heroic 3rd person shooter")

	the_player = Player(screen)

	# Main game loop. Run forever... (or until break)
	while 1:
		screen.fill(background_color)

		check_events()

		# Draw the player
		the_player.draw_me()

		# Clear the screen for the next time through the loop
		pygame.display.flip()

# Start the game!
run_game()