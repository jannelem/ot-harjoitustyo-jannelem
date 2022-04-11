import pygame


class TicTacToe:
    def __init__(self, board_size):
        self.turn = 1  # "Cross has the first turn"
        self.board_size = board_size
        self.tile_size = 300//board_size
        self.tiles = pygame.sprite.Group()
        x_coordinate = 300
        y_coordinate = 50
        self.board = []
        for _ in range(self.board_size):
            row = []
            for __ in range(self.board_size):
                tile = Tile(self.tile_size, x_coordinate, y_coordinate)
                row.append(tile)
                self.tiles.add(tile)
                x_coordinate += self.tile_size + 1
            self.board.append(row)
            x_coordinate = 300
            y_coordinate += self.tile_size + 1

    def deactivate_tiles(self):
        for tile in self.tiles:
            tile.deactivate()

    def __str__(self):
        string_to_return = "Turn: "
        if self.turn == 1:
            string_to_return += "X\n"
        else:
            string_to_return += "O\n"
        string_to_return += "Board:\n"
        for row in self.board:
            for element in row:
                if element.sign == 1:
                    string_to_return += "X"
                elif element.sign == -1:
                    string_to_return += "O"
                else:
                    string_to_return += "_"
            string_to_return += "\n"
        return string_to_return


class Tile(pygame.sprite.Sprite):
    def __init__(self, size, x_coordinate, y_coordinate):
        super().__init__()
        self.size = size
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.sign = 0
        self.active = True
        self.rect = pygame.Rect(x_coordinate, y_coordinate, size, size)

    def deactivate(self):
        self.active = False
