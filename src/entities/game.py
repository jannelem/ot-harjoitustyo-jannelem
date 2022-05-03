from entities.player import *

class TicTacToe():

    def __init__(self, board_size):
        self.player_X = Player("Risti")
        self.player_O = Player("Nolla")
        self.turn = 1
        self.board_size = board_size
        self.in_progress = True
        self.board = []
        for _ in range(self.board_size):
            new_row = []
            for __ in range(self.board_size):
                new_row.append(Tile(_, __))
            self.board.append(new_row)

    def __str__(self):
        return_string = "Vuorossa: "
        if self.turn == 1:
            return_string += "X (" + self.player_X.name + ")"
        elif self.turn == -1:
            return_string += "O (" + self.player_O.name + ")"
        else:
            return_string += "ei kukaan!"
        return_string += "\nPelilauta:\n"
        for _ in range(self.board_size):
            for __ in range(self.board_size):
                if self.board[_][__].value == 1:
                    return_string += "X"
                elif self.board[_][__].value == -1:
                    return_string += "O"
                else:
                    return_string += "_"
            return_string += "\n"

        return return_string


class Tile:

    def __init__(self, row, column):
        self.value = 0
        self.active = True
        self.row = row
        self.column = column

