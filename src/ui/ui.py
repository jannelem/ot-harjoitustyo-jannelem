import pygame
from entities.game import *
from services.game_service import *

def play_game(board_size):
	game = TicTacToe(board_size)
	pygame.init()
	display = pygame.display.set_mode((640,480))
	font = pygame.font.SysFont("Arial", 24)
	clock = pygame.time.Clock()
	game_running = True
	
	while game_running:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				mouse_rect = pygame.Rect(mouse_pos[0], mouse_pos[1],1,1)
				mouse_sprite = pygame.sprite.Sprite()
				mouse_sprite.rect = mouse_rect
				for tile in game.tiles:
					if pygame.sprite.collide_rect(mouse_sprite, tile):
						play(game, tile)

				

		display.fill((255,255,255))

		if game.turn == 1:
			turn_information_string = "Vuorossa: X"
		else:
			turn_information_string = "Vuorossa: 0"
		turn_information_text = font.render(turn_information_string, True, (0,128,128))
		display.blit(turn_information_text,(50,50))

		for tile in game.tiles:
			pygame.draw.rect(display, (0,128,128), (tile.x, tile.y, tile.size, tile.size))
			if tile.sign == 1:
				pygame.draw.line(display, (128,128,0), (tile.x, tile.y),(tile.x+tile.size-1, tile.y+tile.size-1),3)
				pygame.draw.line(display, (128,128,0), (tile.x+tile.size-1, tile.y),(tile.x, tile.y+tile.size-1),3)
			elif tile.sign == -1:
				pygame.draw.circle(display, (128,128,0), (tile.x+tile.size//2, tile.y+tile.size//2), tile.size//2, 3)



		
		#if check_winner(game) != 0:
		#	if check_winner(game) > 0:
		#		winner_string = "Risti voitti!"
		#	if check_winner(game) < 0:
		#		winner_string = "Nolla voitti!"
		#	winner_information_text = font.render(winner_string, True, (0,128,128))
		#	display.blit(winner_information_text,(50,200))
		
				

		pygame.display.flip()
		
		clock.tick(60)