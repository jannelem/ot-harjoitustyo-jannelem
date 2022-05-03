class GameService:
    def __init__(self, player_service):
        self.player_service = player_service

    def play(self, game, tile):
        if tile.value == 0 and tile.active:
            tile.value = game.turn
            game.turn = -game.turn
            tile.active = False
        if self.check_winner(game) != 0 or not self.active_tiles(game):
            self.game_over(game)
            if self.check_winner(game) > 0:
                self.player_service.win(
                    game.player_x, game.player_o, game.board_size)
            elif self.check_winner(game) < 0:
                self.player_service.win(
                    game.player_o, game.player_x, game.board_size)

    def check_winner(self, game):
        diagonal1_sum = 0
        diagonal2_sum = 0
        for i in range(game.board_size):
            diagonal1_sum += game.board[i][i].value
            diagonal2_sum += game.board[i][-1-i].value
            row_sum = 0
            column_sum = 0
            for j in range(game.board_size):
                row_sum += game.board[i][j].value
                column_sum += game.board[j][i].value
            if abs(row_sum) == game.board_size:
                return row_sum
            if abs(column_sum) == game.board_size:
                return column_sum
        if abs(diagonal1_sum) == game.board_size:
            return diagonal1_sum
        if abs(diagonal2_sum) == game.board_size:
            return diagonal2_sum
        return 0

    def game_over(self, game):
        for _ in range(game.board_size):
            for __ in range(game.board_size):
                game.board[_][__].active = False
        game.in_progress = False

    def active_tiles(self, game):
        for _ in range(game.board_size):
            for __ in range(game.board_size):
                if game.board[_][__].active:
                    return True
        return False
