from entities.player import Player

def win(player, board_size):
    player.wins += board_size

def lose(player, board_size):
    player.losses += board_size

def tie(player, board_size):
    player.ties += board_size
