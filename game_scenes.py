import pygame
import random
import constants
import font_and_pic_connection

input_box_width = 350


def generate_bricks():
	bricks = []

	for row in range(constants.rows):
		for col in range(constants.columns):
			x = 22 + col * 130 # Start at correct x cordinates | width + gap
			y = 18 + row * 45 # Start at correct y cordinates | height + vertical gap
			color = random.choice(constants.colors)
			rect = pygame.Rect(x, y, constants.brick_width, constants.brick_height)
			bricks.append((rect, color))
	
	return bricks


def draw_bricks(bricks, alpha = 255):
	if not bricks:
		return
	
	# Alpha < 255 makes them transperant
	elif alpha < 255:
		# Generate surface that supports transperancy
		temp_surface = pygame.Surface((constants.width, constants.height), pygame.SRCALPHA)
		for rect, color in bricks:
			pygame.draw.rect(temp_surface, color + (alpha,), rect)
		constants.screen.blit(temp_surface, (0, 0))
	
	else:
		for rect, color in bricks:
			pygame.draw.rect(constants.screen, color, rect)


def game_over():
	constants.screen.fill(constants.BLACK)
	game_over = font_and_pic_connection.game_over_font.render("Game Over", True, constants.RED)
	over_rect = game_over.get_rect(center = (constants.width // 2, constants.height // 2 - 240))

	play_text = font_and_pic_connection.mode_select_font.render("Play Again", True, constants.WHITE)
	play_rect = play_text.get_rect(center = (constants.width // 2, constants.height // 2 - 40))

	main_menu_text = font_and_pic_connection.mode_select_font.render("Main Menu", True, constants.WHITE)
	main_menu_rect = main_menu_text.get_rect(center = (constants.width // 2, constants.height // 2 + 40))

	exit_text = font_and_pic_connection.mode_select_font.render("Exit", True, (255, 255, 255))
	exit_over_rect = exit_text.get_rect(center = (constants.width // 2, constants.height // 2 + 120))

	pygame.draw.rect(constants.screen, (40, 40, 60), over_rect.inflate(100, 100), border_radius = 10) # Game Over title

	pygame.draw.rect(constants.screen, (40, 40, 60), play_rect.inflate(30, 20), border_radius = 8)
	pygame.draw.rect(constants.screen, (40, 40, 60), main_menu_rect.inflate(30, 20), border_radius = 8)
	pygame.draw.rect(constants.screen, (40, 40, 60), exit_over_rect.inflate(30, 20), border_radius = 8)

	constants.screen.blit(game_over, over_rect)
	constants.screen.blit(play_text, play_rect)
	constants.screen.blit(main_menu_text, main_menu_rect)
	constants.screen.blit(exit_text, exit_over_rect)

	pygame.draw.rect(constants.screen, (40, 40, 60), (0, 0, constants.wall_thickness, constants.height))  # Left
	pygame.draw.rect(constants.screen, (40, 40, 60), (constants.width - constants.wall_thickness, 0, constants.wall_thickness, constants.height)) # Right
	pygame.draw.rect(constants.screen, (40, 40, 60), (0, 0, constants.width, 10)) # Top
	pygame.draw.rect(constants.screen, (40, 40, 60), (0, constants.height - constants.wall_thickness // 2, constants.width, 10)) # Bottom

	pygame.display.flip()

	return play_rect, exit_over_rect, main_menu_rect


def start_screen(dummy_rect, top_space, triangle_pos_1, triangle_pos_2, dummy_bricks):
	constants.screen.fill(constants.BLACK)

	draw_bricks(dummy_bricks, alpha = 80)

	# Temporary transparent paddle
	temp_paddle_surf = pygame.Surface((dummy_rect.width, dummy_rect.height), pygame.SRCALPHA)
	dummy_paddle_alpha = (173, 216, 230, 80)
	pygame.draw.rect(temp_paddle_surf, dummy_paddle_alpha, (0, 0, dummy_rect.width, dummy_rect.height))
	constants.screen.blit(temp_paddle_surf, (dummy_rect.x, dummy_rect.y))

	start_text = font_and_pic_connection.game_title_font.render("Mode Select", True, (255, 255, 255))
	start_rect = start_text.get_rect(center = (constants.width // 2, constants.height //2 - 160))

	play_text = font_and_pic_connection.game_over_font.render("START GAME", True, constants.LIGHT_GREEN)
	play_rect = play_text.get_rect(center = (constants.width // 2, constants.height // 2 - 300))

	easy_text = font_and_pic_connection.mode_select_font.render("EASY", True, constants.WHITE)
	easy_rect = easy_text.get_rect(center = (constants.width // 2, constants.height // 2 + 80))

	hard_text = font_and_pic_connection.mode_select_font.render("HARD", True, constants.WHITE)
	hard_rect = hard_text.get_rect(center = (constants.width // 2, constants.height // 2 + 150))

	constants.screen.blit(start_text, start_rect)
	constants.screen.blit(play_text, play_rect)
	constants.screen.blit(easy_text, easy_rect)
	constants.screen.blit(hard_text, hard_rect)

	if top_space == True:
		pygame.draw.polygon(constants.screen, constants.WHITE, triangle_pos_1)
	elif top_space == False:
		pygame.draw.polygon(constants.screen, constants.WHITE, triangle_pos_2)

	# Walls
	pygame.draw.rect(constants.screen, (40, 40, 60), (0, 0, constants.wall_thickness, constants.height))  # Left
	pygame.draw.rect(constants.screen, (40, 40, 60), (constants.width - constants.wall_thickness, 0, constants.wall_thickness, constants.height)) # Right
	pygame.draw.rect(constants.screen, (40, 40, 60), (0, 0, constants.width, 10)) # Top
	pygame.draw.rect(constants.screen, (40, 40, 60), (0, constants.height - constants.wall_thickness // 2, constants.width, 10))

	pygame.display.flip()

	return start_rect


def main_game(main_rect, ball_x, ball_y, ball_radius, bottom_wall, bricks):
	constants.screen.fill(constants.BLACK)
	if main_rect:
		pygame.draw.rect(constants.screen, (173, 216, 230), main_rect)
	pygame.draw.circle(constants.screen, constants.WHITE, (ball_x, ball_y), ball_radius)

	# Load the bricks on the page
	draw_bricks(bricks, alpha = 255)

	# Walls
	pygame.draw.rect(constants.screen, (40, 40, 60), (0, 0, constants.wall_thickness, constants.height))  # Left
	pygame.draw.rect(constants.screen, (40, 40, 60), (constants.width - constants.wall_thickness, 0, constants.wall_thickness, constants.height)) # Right
	pygame.draw.rect(constants.screen, (40, 40, 60), (0, 0, constants.width, 10)) # Top
	pygame.draw.rect(constants.screen, (40, 40, 60), bottom_wall) # Bottom

	pygame.display.flip()


def pause_menu():
	constants.screen.fill((10, 10, 10))

	paused_text = font_and_pic_connection.mode_select_font.render("Play", True, constants.WHITE)
	paused_rect = paused_text.get_rect(center=(constants.width//2, constants.height//2))

	cheat_text = font_and_pic_connection.mode_select_font.render("Cheat Menu", True, constants.WHITE)
	cheat_rect = cheat_text.get_rect(center = (constants.width//2, constants.height//2 + 80))

	exit_text = font_and_pic_connection.mode_select_font.render("Exit", True, constants.WHITE)
	exit_rect = exit_text.get_rect(center = (constants.width//2, constants.height//2 - 80))

	pygame.draw.rect(constants.screen, (40, 40, 60), paused_rect.inflate(30, 20), border_radius = 8)
	pygame.draw.rect(constants.screen, (40, 40, 60), cheat_rect.inflate(30, 20), border_radius = 8)
	pygame.draw.rect(constants.screen, (40, 40, 60), exit_rect.inflate(30, 20), border_radius = 8)

	constants.screen.blit(paused_text, paused_rect)
	constants.screen.blit(cheat_text, cheat_rect)
	constants.screen.blit(exit_text, exit_rect)

	# Walls
	pygame.draw.rect(constants.screen, (40, 40, 60), (0, 0, constants.wall_thickness, constants.height))  # Left
	pygame.draw.rect(constants.screen, (40, 40, 60), (constants.width - constants.wall_thickness, 0, constants.wall_thickness, constants.height)) # Right
	pygame.draw.rect(constants.screen, (40, 40, 60), (0, 0, constants.width, 10)) # Top
	pygame.draw.rect(constants.screen, (40, 40, 60), (0, constants.height - constants.wall_thickness // 2, constants.width, 10)) # Bottom
	pygame.display.flip()

	return paused_rect, cheat_rect, exit_rect


def won_game():
	constants.screen.fill(constants.BLACK)

	won_text = font_and_pic_connection.game_over_font.render("!YOU WIN!", True, constants.BRIGHT_GREEN)
	won_rect = won_text.get_rect(center = (constants.width // 2, constants.height // 2 - 300))

	menu_text = font_and_pic_connection.mode_select_font.render("MAIN MENU", True, constants.WHITE)
	won_menu_rect = menu_text.get_rect(center = (constants.width // 2, constants.height // 2 + 40))

	exit_text = font_and_pic_connection.mode_select_font.render("EXIT", True, constants.WHITE)
	won_exit_rect = exit_text.get_rect(center = (constants.width // 2, constants.height // 2 + 120))

	pygame.draw.rect(constants.screen, (40, 40, 60), won_menu_rect.inflate(30, 20), border_radius = 8)
	pygame.draw.rect(constants.screen, (40, 40, 60), won_exit_rect.inflate(30, 20), border_radius = 8)

	constants.screen.blit(won_text, won_rect)
	constants.screen.blit(menu_text, won_menu_rect)
	constants.screen.blit(exit_text, won_exit_rect)

	font_and_pic_connection.trophy_rect.center = (constants.width // 2, constants.height // 2 - 150)
	constants.screen.blit(font_and_pic_connection.trophy, font_and_pic_connection.trophy_rect)

	# Walls
	pygame.draw.rect(constants.screen, (40, 40, 60), (0, 0, constants.wall_thickness, constants.height))  # Left
	pygame.draw.rect(constants.screen, (40, 40, 60), (constants.width - constants.wall_thickness, 0, constants.wall_thickness, constants.height)) # Right
	pygame.draw.rect(constants.screen, (40, 40, 60), (0, 0, constants.width, 10)) # Top
	pygame.draw.rect(constants.screen, (40, 40, 60), (0, constants.height - constants.wall_thickness // 2, constants.width, 10)) # Bottom
	pygame.display.flip()

	return won_menu_rect, won_exit_rect


def cheat_menu(input_text, show_cursor):
	constants.screen.fill(constants.BLACK)

	# Title
	cheats_text = font_and_pic_connection.mode_select_font.render("CHEATS", True, constants.WHITE)
	cheats_rect = cheats_text.get_rect(center = (constants.width // 4 - 30, constants.height // 4 - 100))
	constants.screen.blit(cheats_text, cheats_rect)

	# Textbox Border/box
	input_box = pygame.Rect(constants.width // 2 + 30, constants.height // 4 - 125, input_box_width, 50)
	pygame.draw.rect(constants.screen, constants.WHITE, input_box, 2) # Textbox Border

	# Render the typed text
	content_surf = font_and_pic_connection.mode_select_font.render(input_text, True, constants.WHITE)
	text_x = input_box.x + 10
	text_y = input_box.y + 10
	constants.screen.blit(content_surf, (input_box.x + 10, input_box.y + 10))

	# Find the dynamic/moving cursor position
	text_width, _ = font_and_pic_connection.mode_select_font.size(input_text)

	# Blinking cursor
	if show_cursor:
		# Find x at 95% if the box width
		cursor_x = text_x + text_width + 2

		start_y = input_box.y + 10
		end_y = input_box.y + input_box.height - 10

		pygame.draw.line(constants.screen, constants.WHITE, (cursor_x, start_y), (cursor_x, end_y))
	
	# Walls
	pygame.draw.rect(constants.screen, (40, 40, 60), (0, 0, constants.wall_thickness, constants.height))  # Left
	pygame.draw.rect(constants.screen, (40, 40, 60), (constants.width - constants.wall_thickness, 0, constants.wall_thickness, constants.height)) # Right
	pygame.draw.rect(constants.screen, (40, 40, 60), (0, 0, constants.width, 10)) # Top
	pygame.draw.rect(constants.screen, (40, 40, 60), (0, constants.height - constants.wall_thickness // 2, constants.width, 10)) # Bottom
	pygame.display.flip()
	
