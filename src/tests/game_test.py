import unittest
from entities.game import *
from services.game_service import *
from services.player_service import *


class TestGame(unittest.TestCase):

    def setUp(self):
        self.player_service = PlayerService()
        self.game_service = GameService(self.player_service)
        self.blank_game = TicTacToe(3)
        

    def test_board_initially_blank(self):
        for _ in range(self.blank_game.board_size):
            for __ in range(self.blank_game.board_size):
                self.assertEqual(self.blank_game.board[_][__].value, 0)