# Duh
import pygame
# we need sys for quit
import sys

def check_events(the_player):
	# The escape hatch (from while)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			# The user clicked the red x. Get out of teh loop and kill the game
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == 273:
				the_player.should_move("up", True)
			elif event.key == 274:
				the_player.should_move("down", True)
			elif event.key == 276:
				# print "User pressed left!"
				the_player.should_move("left", True)
			elif event.key == 275:
				# print "User pressed right!"
				the_player.should_move("right", True)
			# elif event.key == 121:
			# 	# userpushed "y"
			# 	hero['x'] = 100
			# 	hero['y'] = 100
			# elif event.key == 32:
			# 	# user pushed space!
			# 	game_paused = not game_paused
		elif event.type == pygame.KEYUP:
			# print "The user let go of a key"
			if event.key == 273:
				# the user let go of a key... and that key was the up arrow
				the_player.should_move("up", False)
			if event.key == 274:
				the_player.should_move("down", False)
			if event.key == 276:
				the_player.should_move("left", False)
			if event.key == 275:
				the_player.should_move("right", False)
