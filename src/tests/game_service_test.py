import unittest
from entities.game import TicTacToe
from services.game_service import *


class TestGame_service(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToe(4)
        self.game_diagonals = TicTacToe(4)
        self.game_column_and_row = TicTacToe(4)

        play(self.game_diagonals, self.game_diagonals.board[0][0])
        play(self.game_diagonals, self.game_diagonals.board[0][3])
        play(self.game_diagonals, self.game_diagonals.board[1][1])
        play(self.game_diagonals, self.game_diagonals.board[1][2])
        play(self.game_diagonals, self.game_diagonals.board[2][2])
        play(self.game_diagonals, self.game_diagonals.board[2][1])

        play(self.game_column_and_row, self.game_column_and_row.board[2][0])
        play(self.game_column_and_row, self.game_column_and_row.board[0][3])
        play(self.game_column_and_row, self.game_column_and_row.board[2][1])
        play(self.game_column_and_row, self.game_column_and_row.board[1][3])
        play(self.game_column_and_row, self.game_column_and_row.board[2][2])
        play(self.game_column_and_row, self.game_column_and_row.board[3][3])

    def test_board_is_initially_blank(self):
        for tile in self.game.tiles:
            self.assertEqual(tile.sign, 0)

    def test_first_move_changes_board(self):
        play(self.game, self.game.board[0][0])
        self.assertEqual(self.game.board[0][0].sign, 1)

    def test_same_tile_cannot_be_played_again(self):
        play(self.game, self.game.board[0][0])
        play(self.game, self.game.board[0][0])
        self.assertEqual(self.game.board[0][0].sign, 1)

    def test_tiles_are_deactivated(self):
        self.game.deactivate_tiles()
        for tile in self.game.tiles:
            self.assertEqual(tile.active, False)

    def test_no_winner(self):
        self.assertEqual(check_winner(self.game_diagonals), 0)

    def test_diagonal1_winner_is_detected(self):
        play(self.game_diagonals, self.game_diagonals.board[3][3])
        self.assertEqual(check_winner(self.game_diagonals), 4)

    def test_diagonal2_winner_is_detected(self):
        play(self.game_diagonals, self.game_diagonals.board[0][2])
        play(self.game_diagonals, self.game_diagonals.board[3][0])
        self.assertEqual(check_winner(self.game_diagonals), -4)

    def test_row_is_detected(self):
        play(self.game_column_and_row, self.game_column_and_row.board[2][3])
        self.assertEqual(check_winner(self.game_column_and_row), 4)

    def test_column_is_detected(self):
        play(self.game_column_and_row, self.game_column_and_row.board[0][1])
        play(self.game_column_and_row, self.game_column_and_row.board[2][3])
        self.assertEqual(check_winner(self.game_column_and_row), -4)
