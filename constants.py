import pygame

wall_thickness = 18
width = 950
height = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Bricks")

bricks = []
rows = 9
columns = 7
brick_width = 125
brick_height = 40
gap = 5

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
LIGHT_GREEN = (32, 168, 8)
LIGHT_GRAY = (164, 168, 163)

TERMINAL_RED = '\033[91m'
TERMINAL_YELLOW = '\u001b[33m'
TERMINAL_RESET = '\033[0m'

BRICK_RED = (145, 3, 3)
BRICK_GREEN = (10, 138, 3)
BRICK_ORANGE = (209, 86, 4)
BRICK_BLUE = (222, 222, 4)
BRICK_PURPLE = (104, 4, 138)
BRICK_LIGHT_BLUE = (9, 188, 224)

colors = [
	BRICK_RED,
	BRICK_GREEN,
	BRICK_ORANGE,
	BRICK_BLUE,
	BRICK_PURPLE,
	BRICK_LIGHT_BLUE
]
