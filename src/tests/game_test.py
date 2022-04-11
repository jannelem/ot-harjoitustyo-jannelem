import unittest
from entities.game import *
from services.game_service import *


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToe(3)
        play(self.game, self.game.board[0][0])
        play(self.game, self.game.board[2][2])

    def test_str_works_after_two_moves(self):
        self.assertEqual(str(self.game), "Turn: X\nBoard:\nX__\n___\n__O\n")

    def test_str_works_after_three_moves(self):
        play(self.game, self.game.board[2][1])
        self.assertEqual(str(self.game), "Turn: O\nBoard:\nX__\n___\n_XO\n")
