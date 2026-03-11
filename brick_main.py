import pygame
import sys
import math
import constants
import game_scenes


pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

game_state = "start"  # start | game | pause | game_over | won_game
main_rect = None      # Paddle does not exist yet
paddle_y = constants.height - 60

ball_x = constants.width // 2
ball_y = constants.height // 2 + 100
ball_radius = 10

ball_vx = 5
ball_vy = -5
base_speed = 5
hard_speed = 10

bottom_wall = pygame.Rect(0, constants.height - constants.wall_thickness // 2, constants.width, 10)

top_space = True

# Place Holer Values
start_rect = pygame.Rect(0, 0, 0, 0)
paused_rect = pygame.Rect(0, 0, 0, 0)
cheat_rect = pygame.Rect(0, 0, 0, 0)
exit_rect = pygame.Rect(0, 0, 0, 0)
play_rect = pygame.Rect(0, 0, 0, 0)
exit_over_rect = pygame.Rect(0, 0, 0, 0)
main_menu_rect = pygame.Rect(0, 0, 0, 0)
won_menu_rect = pygame.Rect(0, 0, 0, 0)
won_exit_rect = pygame.Rect(0, 0, 0, 0)

# main_rect = pygame.Rect(constants.width // 2 - 102, paddle_y, 175, 30)
dummy_rect = pygame.Rect(constants.width // 2 - 102, paddle_y, 175, 30)
dummy_bricks = game_scenes.generate_bricks()
bricks = game_scenes.generate_bricks()

# x1 y1, x2 y2, x3 y3
triangle_pos_1 = [
	(constants.width // 2 - 95, constants.height // 2 + 65), # Top Left
	(constants.width // 2 - 95, constants.height // 2 + 95), # Botton Left
	(constants.width // 2 - 75, constants.height // 2 + 80) # Bottom Right
]

# x1 y1, x2 y2, x3 y3
triangle_pos_2 = [
	(constants.width // 2 - 95, constants.height // 2 + 135), # Top Left
	(constants.width // 2 - 95, constants.height // 2 + 165), # Bottom Left
	(constants.width // 2 - 75, constants.height // 2 + 150) # Bottom Right
]

top_space = True
    
while True:
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()

				if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
					if game_state == "start":
						game_state = "game"
						main_rect = pygame.Rect(constants.width // 2 - 102, paddle_y, 175, 30)
						bricks = game_scenes.generate_bricks()
						ball_x = constants.width - constants.width // 2
						ball_y = constants.height // 2 + 100
						# If top space is true then easy is selected
						if top_space:
							mode = "easy"
							ball_vx, ball_vy = base_speed, -base_speed
						else:
							mode = "hard"
							ball_vx, ball_vy = hard_speed, -hard_speed

					elif game_state == "game_over":
						game_state = "game"
						main_rect = pygame.Rect(constants.width // 2 - 102, paddle_y, 175, 30)
						bricks = game_scenes.generate_bricks()
						ball_x = constants.width - constants.width // 2
						ball_y = constants.height // 2 + 100
					
				if event.key == pygame.K_DOWN or event.key == pygame.K_s:
					if game_state == "start":
						if top_space == True:
							top_space = False
						elif top_space == False:
							top_space = True

				if event.key == pygame.K_UP or event.key == pygame.K_w:
					if game_state == "start":
						if top_space == True:
							top_space = False
						elif top_space == False:
							top_space = True

				if event.type == pygame.K_RETURN or event.type == pygame.K_KP_ENTER:
					if game_state == "start":
						main_rect = pygame.Rect(constants.width // 2 - 102, paddle_y, 175, 30)
						bricks = game_scenes.generate_bricks()
						ball_x = constants.width - constants.width // 2
						ball_y = constants.height // 2 + 100

				if game_state == "game" and event.key == pygame.K_p:
					game_state = "pause"

				elif game_state == "pause" and (event.key == pygame.K_p or event.key == pygame.K_SPACE):
					game_state = "game"
				
				if game_state == "game_over" and event.key == pygame.K_p:
					game_state = "game"
					main_rect = pygame.Rect(constants.width//2 - 102, paddle_y, 175, 30)
					bricks = game_scenes.generate_bricks()
					ball_x = constants.width - constants.width // 2
					ball_y = constants.height // 2 + 100
			
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = event.pos
				if game_state == "pause":
				
					if paused_rect.collidepoint(mouse_pos):
						game_state = "game"
					
					if exit_rect.collidepoint(mouse_pos):
						pygame.quit()
						sys.exit()
					
					if cheat_rect.collidepoint(mouse_pos):
						game_state = "won_game"
						"""print("Cheat menu clicked")"""

				if game_state == "game_over":

					if play_rect.collidepoint(mouse_pos):
						game_state = "game"
						bricks = game_scenes.generate_bricks()
						main_rect = pygame.Rect(constants.width//2 - 102, paddle_y, 175, 30)
						ball_x = constants.width - constants.width // 2
						ball_y = constants.height // 2 + 100
						if top_space:
							mode = "easy"
							ball_vx, ball_vy = base_speed, -base_speed
						else:
							mode = "hard"
							ball_vx, ball_vy = hard_speed, -hard_speed

					
					if exit_over_rect.collidepoint(mouse_pos):
						print(f"{constants.TERMINAL_RED}Exiting...{constants.TERMINAL_RESET}")
						pygame.quit()
						sys.exit()
					
					if main_menu_rect.collidepoint(mouse_pos):
						game_state = "start"

				if game_state == "start":

					if start_rect.collidepoint(mouse_pos):
						game_state = "game"
						main_rect = pygame.Rect(constants.width//2 - 102, paddle_y, 175, 30)
						bricks = game_scenes.generate_bricks()
						ball_x = constants.width - constants.width // 2
						ball_y = constants.height // 2 + 100
				
				if game_state == "won_game":

					if won_exit_rect.collidepoint(mouse_pos):
						print(f"{constants.TERMINAL_RED}Exiting...{constants.TERMINAL_RESET}")
						pygame.quit()
						sys.exit()
					
					if won_menu_rect.collidepoint(mouse_pos):
						game_state = "start"
					
	keys = pygame.key.get_pressed()

	if game_state == "start":
		start_rect = game_scenes.start_screen(dummy_rect, top_space, triangle_pos_1, triangle_pos_2, dummy_bricks)
	if game_state == "game" and main_rect is not None:
		game_scenes.main_game(main_rect, ball_x, ball_y, ball_radius, bottom_wall, bricks)

		prev_paddle_x = main_rect.x

		if keys[pygame.K_LEFT] or keys[pygame.K_a]:
			if mode == "easy":
				main_rect.move_ip(-9, 0)
			else:
				main_rect.move_ip(-13, 0)
		if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
			if mode == "easy":
				main_rect.move_ip(9, 0)
			else:
				main_rect.move_ip(13, 0)
		
		paddle_vx = main_rect.x - prev_paddle_x
		
		if main_rect.left < constants.wall_thickness:
			main_rect.left = constants.wall_thickness
		if main_rect.right > constants.width - constants.wall_thickness:
			main_rect.right = constants.width - constants.wall_thickness

		ball_x += ball_vx
		ball_y += ball_vy

		ball_rect = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)
		ball_center_x = ball_rect.left + ball_rect.width / 2
		ball_center_y = ball_rect.top + ball_rect.height / 2

		prev_paddle_x = main_rect.x
		paddle_vx = main_rect.x - prev_paddle_x

		for brick in bricks[:]:
			brick_rect, color = brick

			if ball_rect.colliderect(brick_rect):
				dx = ball_rect.centerx - brick_rect.centerx
				dy = ball_rect.centery - brick_rect.centery

				overlap_x = (brick_rect.width / 2 + ball_rect.width / 2) - abs(dx)
				overlap_y = (brick_rect.height / 2 + ball_rect.height / 2) - abs(dy)

				if overlap_x < overlap_y:
					# Horizontal Collision
					if dx > 0:
						ball_rect.left = brick_rect.right
						ball_vx = abs(ball_vx)
					else:
						ball_rect.right = brick_rect.left
						ball_vx = -abs(ball_vx)
				else:
					if dy > 0:
						ball_rect.top = brick_rect.bottom
						ball_vy = abs(ball_vy)
					else:
						ball_rect.bottom = brick_rect.top
						ball_vy = -abs(ball_vy)
					
				# Sync actual ball position to resolved rect
				ball_x = ball_rect.centerx
				ball_y = ball_rect.centery

				bricks.remove(brick)
				break

		if ball_rect.colliderect(main_rect):
			# Ball goes up to prevent sticking
			ball_rect.bottom = main_rect.top
			ball_y = ball_rect.centery

			# -1 is far left side and 1 is far right side
			ball_center = ball_rect.centerx
			paddle_center = main_rect.centerx
			paddle_half_width = main_rect.width / 2

			hit_offset = ball_center - paddle_center
			hit_pos = hit_offset / paddle_half_width

			# Clamp to prevent the ball from going slightly outside the rectangel edge
			if hit_pos > 1:
				hit_pos = 1
			if hit_pos < -1:
				hit_pos = -1
			
			max_bounce_angle = 75
			bounce_angle_degrees = hit_pos * max_bounce_angle
			bounce_angle_radians = math.radians(bounce_angle_degrees)

			# Preserve speed
			current_speed = math.sqrt(ball_vx ** 2 + ball_vy ** 2)

			# Convert angle to correct components, SOH-CAH-TOA
			ball_vx = current_speed * math.sin(bounce_angle_radians)
			ball_vy = -current_speed * math.cos(bounce_angle_radians)

		# Left wall
		if ball_x - ball_radius <= constants.wall_thickness:
			ball_vx = abs(ball_vx)
		
		# Right wall
		if ball_x + ball_radius >= constants.width - constants.wall_thickness:
			ball_vx = -abs(ball_vx)
		
		# Top wall
		if ball_rect.top <= 10:
			ball_rect.top = 10
			ball_vy = abs(ball_vy)
			ball_y = ball_rect.centery

		# Collide with the bottom
		if ball_y + ball_radius >= bottom_wall.top:
			game_state = "game_over"

		if not bricks:
			game_state = "won_game"

	if game_state == "pause":
		paused_rect, cheat_rect, exit_rect = game_scenes.pause_menu()
	if game_state == "game_over":
		play_rect, exit_over_rect, main_menu_rect = game_scenes.game_over()
	if game_state == "won_game":
		won_menu_rect, won_exit_rect = game_scenes.won_game()

	pygame.display.flip()
	clock.tick(60)

