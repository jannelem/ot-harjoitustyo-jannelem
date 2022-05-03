from entities.game import TicTacToe, Tile
from services.game_service import GameService
from entities.player import Player


if __name__ == "__main__":
    new_game = TicTacToe(6)
    game_service = GameService()
    print(new_game)
