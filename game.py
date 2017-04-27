# The reason you have access to this moduel, is because you ran
# $ pip install pygame
# Pygame is NOT part of core (like math or random is)
import pygame
# Import the player class from Player
from player import Player
# Import check_events from the game_functions module
from game_functions import check_events
# Get the enemy class so we can make new enemies
from enemy import Enemy
# Get groupcollide and Group from the sprite module
from pygame.sprite import Group, groupcollide


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

	the_player = Player(screen,'./images/Hero.png',100,100)
	the_player_group = Group()
	the_player_group.add(the_player)
	bad_guy = Enemy(screen)
	enemies = Group()
	enemies.add(bad_guy)


	# Main game loop. Run forever... (or until break)
	while 1:
		screen.fill(background_color)

		check_events(the_player)

		# Draw the player
		for player in the_player_group:
			player.draw_me()

		# Update and Draw the bad guy
		bad_guy.update_me(the_player)
		bad_guy.draw_me()

		# Check for collisions...
		hero_died = groupcollide(the_player_group, enemies, True, False)
		print hero_died


		# Clear the screen for the next time through the loop
		pygame.display.flip()

# Start the game!
run_game()