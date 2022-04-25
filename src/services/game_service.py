
from entities.game import TicTacToe, Tile


def play(game: TicTacToe, tile: Tile):
    if tile.sign == 0 and tile.active is True:
        tile.sign = game.turn
        game.turn = -game.turn
        tile.deactivate()


def check_winner(game):
    diagonal1_sum = 0
    diagonal2_sum = 0
    for i in range(game.board_size):
        diagonal1_sum += game.board[i][i].sign
        diagonal2_sum += game.board[i][-1-i].sign
        row_sum = 0
        column_sum = 0
        for j in range(game.board_size):
            row_sum += game.board[i][j].sign
            column_sum += game.board[j][i].sign
        if abs(row_sum) == game.board_size:
            return row_sum
        if abs(column_sum) == game.board_size:
            return column_sum
    if abs(diagonal1_sum) == game.board_size:
        return diagonal1_sum
    if abs(diagonal2_sum) == game.board_size:
        return diagonal2_sum
    return 0
