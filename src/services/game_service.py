
from entities.game import TicTacToe

def play(game, row, column):
        if game.board[row][column] == 0:
            game.board[row][column] = game.turn
            game.turn = -game.turn

if __name__ == "__main__":
    testgame = TicTacToe()
    print(testgame)