import pygame


pygame.font.init()

try:
	font_path = "PressStart2P-Regular.ttf" # If this does not work paste the file path into this slot
	mode_select_font = pygame.font.Font(font_path, 30)
	game_title_font = pygame.font.Font(font_path, 45)
	game_over_font = pygame.font.Font(font_path, 90)
except:
	print("Error loading font pack")
	mode_select_font = pygame.font.Font(None, 60)
	game_title_font = pygame.font.Font(None, 65)
	game_over_font = pygame.font.Font(None, 150)

