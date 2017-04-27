# Duh
import pygame
# we need sys for quit
import sys

def check_events():
	# The escape hatch (from while)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			# The user clicked the red x. Get out of teh loop and kill the game
			sys.exit()