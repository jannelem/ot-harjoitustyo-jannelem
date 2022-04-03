from re import X
import pygame
from entities.game import TicTacToe
from services.game_service import *

def play_game():
	game = TicTacToe()
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
				mouse_position = pygame.mouse.get_pos()
				if 300 <= mouse_position[0] <= 399 and 50 <= mouse_position[1] <= 149:
					play(game,0,0)
				if 410 <= mouse_position[0] <= 509 and 50 <= mouse_position[1] <= 149:
					play(game,0,1)
				if 520 <= mouse_position[0] <= 619 and 50 <= mouse_position[1] <= 149:
					play(game,0,2)
				if 300 <= mouse_position[0] <= 399 and 160 <= mouse_position[1] <= 259:
					play(game,1,0)
				if 410 <= mouse_position[0] <= 509 and 160 <= mouse_position[1] <= 259:
					play(game,1,1)
				if 520 <= mouse_position[0] <= 619 and 160 <= mouse_position[1] <= 259:
					play(game,1,2)
				if 300 <= mouse_position[0] <= 399 and 270 <= mouse_position[1] <= 369:
					play(game,2,0)
				if 410 <= mouse_position[0] <= 509 and 270 <= mouse_position[1] <= 369:
					play(game,2,1)
				if 520 <= mouse_position[0] <= 619 and 270 <= mouse_position[1] <= 369:
					play(game,2,2)
		

		
				

		display.fill((255,255,255))

		x = 300
		y = 50

		for i in range (len(game.board)):
			for j in range(len(game.board)):
				pygame.draw.rect(display, (0,0,255), (x,y,100,100))
				if game.board[i][j] == 1:
					pygame.draw.line(display, (255,0,255), (x,y),(x+100,y+100),5)
					pygame.draw.line(display, (255,0,255), (x+100,y),(x,y+100),5)
				if game.board[i][j] == -1:
					pygame.draw.circle(display, (255,0,255), (x+50,y+50),49)
					pygame.draw.circle(display, (0,0,255), (x+50,y+50),44)
				x += 110
			x = 300
			y += 110

		if game.turn == 1:
			turn_information_string = "Vuorossa: X"
		else:
			turn_information_string = "Vuorossa: 0"
		turn_information_text = font.render(turn_information_string, True, (0,128,128))
		display.blit(turn_information_text,(50,50))
		
		if check_winner(game) != 0:
			if check_winner(game) > 0:
				winner_string = "Risti voitti!"
			if check_winner(game) < 0:
				winner_string = "Nolla voitti!"
			winner_information_text = font.render(winner_string, True, (0,128,128))
			display.blit(winner_information_text,(50,200))
		
				

		pygame.display.flip()
		
		clock.tick(60)