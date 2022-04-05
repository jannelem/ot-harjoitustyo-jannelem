
from entities.game import TicTacToe

class Game_service:

    def play(game: TicTacToe, row: int, column: int):
            if game.board[row][column] == 0:
                game.board[row][column] = game.turn
                game.turn = -game.turn

    def check_winner(game: TicTacToe) -> int:
        board_size = len(game.board)
        diagonal1_sum = 0
        diagonal2_sum = 0
        for i in range(board_size):
            diagonal1_sum += game.board[i][i]
            diagonal2_sum += game.board[i][-1-i]
            row_sum = 0
            column_sum = 0
            for j in range(board_size):
                row_sum += game.board[i][j]
                column_sum += game.board[j][i]
            if abs(row_sum) == board_size:
                return row_sum
            if abs(column_sum) == board_size:
                return column_sum
        if abs(diagonal1_sum) == board_size:
            return diagonal1_sum
        if abs(diagonal2_sum) == board_size:
            return diagonal2_sum
        return 0


