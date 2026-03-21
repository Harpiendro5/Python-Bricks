import pygame
import sys
import constants


pygame.font.init()

try:
	font_path = "" # Must replace with your own path
	mode_select_font = pygame.font.Font(font_path, 30)
	game_title_font = pygame.font.Font(font_path, 45)
	game_over_font = pygame.font.Font(font_path, 90)
except:
	print("Error loading font pack")
	mode_select_font = pygame.font.Font(None, 60)
	game_title_font = pygame.font.Font(None, 65)
	game_over_font = pygame.font.Font(None, 150)

try:
	trophy_raw = pygame.image.load("").convert_alpha() #<- Must replace with your own path
	trophy = pygame.transform.scale(trophy_raw, (400, 400))
	trophy_rect = trophy.get_rect()

except pygame.error as e:
	print(f"{constants.TERMINAL_RED}Error loading image: {e}{constants.TERMINAL_RESET}")
	sys.exit()
