import unittest
from entities.game import TicTacToe
from services.game_service import *

class TestGame_service(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToe()

    def test_board_is_initially_blank(self):
        for row in self.game.board:
            for element in row:
                self.assertEqual(element, 0)