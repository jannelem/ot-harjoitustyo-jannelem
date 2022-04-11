import pygame


class TicTacToe:
    def __init__(self, board_size):
        self.turn = 1 # "Cross has the first turn"
        self.board_size = board_size
        self.tile_size = 300//board_size
        self.tiles = pygame.sprite.Group()
        x = 300
        y = 50
        self.board = []
        for i in range (self.board_size):
            row = []
            for j in range(self.board_size):
                tile = Tile(self.tile_size,x,y)
                row.append(tile)
                self.tiles.add(tile)
                x += self.tile_size + 1
            self.board.append(row)
            x = 300
            y += self.tile_size + 1
    
    def deactivate_tiles(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                self.board[i][j].deactivate()
                

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

class Tile(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__()
        self.size = size
        self.x = x
        self.y = y
        self.sign = 0
        self.active = True
        self.rect = pygame.Rect(x,y,size,size)
    
    def deactivate(self):
        self.active = False