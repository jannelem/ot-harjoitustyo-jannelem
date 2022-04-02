class TicTacToe:
    def __init__(self):
        self.turn = 1 # "Cross has the first turn"
        self.board = [[0,0,0], [0,0,0],[0,0,0]]

    def __str__(self):
        string_to_return = "Turn: "
        if self.turn == 1:
            string_to_return += "X\n"
        else:
            string_to_return += "O\n"
        string_to_return += "Board:\n"
        for row in self.board:
            for element in row:
                if element == 1:
                    string_to_return += "X"
                elif element == -1:
                    string_to_return += "O"
                else:
                    string_to_return += "_"
            string_to_return += "\n"
        return string_to_return