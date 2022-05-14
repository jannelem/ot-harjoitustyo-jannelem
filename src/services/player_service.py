class PlayerService:

    def win(self, player_x, player_o, board_size):
        player_x.wins += board_size
        player_o.losses += board_size

    def tie(self, player_x, player_o, board_size):
        player_x.ties += board_size
        player_o.ties += board_size