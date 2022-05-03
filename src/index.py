from entities.game import *
from entities.player import Player
from services.game_service import *
from services.player_service import *


if __name__ == "__main__":
    new_game = TicTacToe(6)
    game_service = GameService()
    print(new_game)
    print(game_service.check_winner(new_game))
