import pygame
import sys
import constants
import game_scenes


pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

game_scenes.generate_bricks()

game_state = "start"  # start | game | pause | game_over
main_rect = None      # Paddle does not exist yet
paddle_y = constants.height - 60

ball_x = constants.width // 2
ball_y = constants.height // 2 + 100
ball_radius = 10

ball_vx = 5
ball_vy = -5

bottom_wall = pygame.Rect(0, constants.height - constants.wall_thickness // 2, constants.width, 10)

top_space = True

dummy_rect = pygame.Rect(0, constants.height - constants.wall_thickness // 2, constants.width, 10)


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
						game_scenes.generate_bricks()
						ball_x = constants.width - constants.width // 2
						ball_y = constants.height // 2 + 100

					elif game_state == "game_over":
						game_state = "game"
						main_rect = pygame.Rect(constants.width // 2 - 102, paddle_y, 175, 30)
						game_scenes.generate_bricks()
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
						game_scenes.generate_bricks()
						ball_x = constants.width - constants.width // 2
						ball_y = constants.height // 2 + 100

				if game_state == "game" and event.key == pygame.K_p:
					game_state = "pause"

				elif game_state == "pause" and (event.key == pygame.K_p or event.key == pygame.K_SPACE):
					game_state = "game"
				
				if game_state == "game_over" and event.key == pygame.K_p:
					game_state = "game"
					main_rect = pygame.Rect(constants.width//2 - 102, paddle_y, 175, 30)
					game_scenes.generate_bricks()
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
						print("Cheat menu clicked")

				if game_state == "game_over":

					if play_rect.collidepoint(mouse_pos):
						game_state = "game"
						game_scenes.generate_bricks()
						main_rect = pygame.Rect(constants.width//2 - 102, paddle_y, 175, 30)
						ball_x = constants.width - constants.width // 2
						ball_y = constants.height // 2 + 100
					
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
						game_scenes.generate_bricks()
						ball_x = constants.width - constants.width // 2
						ball_y = constants.height // 2 + 100	
					

	keys = pygame.key.get_pressed()

	if game_state == "start":
		start_rect = game_scenes.start_screen(dummy_rect, top_space, triangle_pos_1, triangle_pos_2)
	if game_state == "game" and main_rect is not None:
		game_scenes.main_game(main_rect, ball_x, ball_y, ball_radius, bottom_wall)

		prev_paddle_x = main_rect.x

		if keys[pygame.K_LEFT] or keys[pygame.K_a]:
			main_rect.move_ip(-9, 0)
		if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
			main_rect.move_ip(9, 0)
		
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

		for brick in game_scenes.bricks[:]:
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

				game_scenes.bricks.remove(brick)
				break

		if ball_rect.colliderect(main_rect):
			# Push ball above paddle to stop sticking
			ball_rect.bottom = main_rect.top
			ball_y = ball_rect.centery

			# Always bounce upward
			ball_vy = -abs(ball_vy)

			# Influence direction
			if paddle_vx < 0 and ball_vx > 0:
				ball_vx *= -1
			if paddle_vx > 0 and ball_vx < 0:
				ball_vx *= -1

		# Left wall
		if ball_x - ball_radius <= constants.wall_thickness:
			ball_vx = abs(ball_vx)
		
		# Right wall
		if ball_x + ball_radius >= constants.width - constants.wall_thickness:
			ball_vx = -abs(ball_vx)
		
		# Top wall
		if ball_y - ball_radius <= 10:
			ball_vy = -abs(ball_vy)

		# Collide with the bottom
		if ball_y + ball_radius >= bottom_wall.top:
			game_state = "game_over"

	if game_state == "pause":
		paused_rect, cheat_rect, exit_rect = game_scenes.pause_menu()
	if game_state == "game_over":
		play_rect, exit_over_rect, main_menu_rect = game_scenes.game_over()

	pygame.display.flip()
	clock.tick(60)

