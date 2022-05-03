from entities.game import TicTacToe
from services.game_service import GameService
from services.player_service import PlayerService


if __name__ == "__main__":
    new_game = TicTacToe(3)
    player_service = PlayerService()
    game_service = GameService(player_service)
    print(new_game)
    game_service.play(new_game, new_game.board[0][0])
    print(new_game)
    game_service.play(new_game, new_game.board[0][0])
    print(new_game)
    game_service.play(new_game, new_game.board[1][1])
    print(new_game)
    game_service.play(new_game, new_game.board[1][0])
    game_service.play(new_game, new_game.board[2][0])
    game_service.play(new_game, new_game.board[0][1])
    print(new_game)
    game_service.play(new_game, new_game.board[0][2])
    print(game_service.active_tiles(new_game))
    print(new_game.player_x)
    print(new_game.player_o)
