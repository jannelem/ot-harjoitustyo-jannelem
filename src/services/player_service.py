class PlayerService:

    def win(self, player_X, player_O, board_size):
        player_X.wins += board_size
        player_O.losses += board_size


    def tie(self, player_X, player_O, board_size):
        player_X.ties += board_size
        player_O.ties += board_size
