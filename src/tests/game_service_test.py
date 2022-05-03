import unittest
from entities.game import TicTacToe
from services.game_service import GameService
from services.player_service import PlayerService


class TestGameService(unittest.TestCase):

    def setUp(self):
        self.player_service = PlayerService()
        self.game_service = GameService(self.player_service)
        self.game = TicTacToe(4)
        self.game_diagonals = TicTacToe(4)
        self.game_column_and_row = TicTacToe(4)

        self.game_service.play(self.game_diagonals, self.game_diagonals.board[0][0])
        self.game_service.play(self.game_diagonals, self.game_diagonals.board[0][3])
        self.game_service.play(self.game_diagonals, self.game_diagonals.board[1][1])
        self.game_service.play(self.game_diagonals, self.game_diagonals.board[1][2])
        self.game_service.play(self.game_diagonals, self.game_diagonals.board[2][2])
        self.game_service.play(self.game_diagonals, self.game_diagonals.board[2][1])

        self.game_service.play(self.game_column_and_row, self.game_column_and_row.board[2][0])
        self.game_service.play(self.game_column_and_row, self.game_column_and_row.board[0][3])
        self.game_service.play(self.game_column_and_row, self.game_column_and_row.board[2][1])
        self.game_service.play(self.game_column_and_row, self.game_column_and_row.board[1][3])
        self.game_service.play(self.game_column_and_row, self.game_column_and_row.board[2][2])
        self.game_service.play(self.game_column_and_row, self.game_column_and_row.board[3][3])

    def test_first_move_changes_board(self):
        self.game_service.play(self.game, self.game.board[0][0])
        self.assertEqual(self.game.board[0][0].value, 1)

    def test_same_tile_cannot_be_played_again(self):
        self.game_service.play(self.game, self.game.board[0][0])
        self.game_service.play(self.game, self.game.board[0][0])
        self.assertEqual(self.game.board[0][0].value, 1)

    def test_tiles_are_deactivated(self):
        self.game_service.game_over(self.game_diagonals)
        self.assertEqual(self.game_service.active_tiles(self.game_diagonals), False)

    def test_no_winner(self):
        self.assertEqual(self.game_service.check_winner(self.game_diagonals), 0)

    def test_diagonal1_winner_is_detected(self):
        self.game_service.play(self.game_diagonals, self.game_diagonals.board[3][3])
        self.assertEqual(self.game_service.check_winner(self.game_diagonals), 4)

    def test_diagonal2_winner_is_detected(self):
        self.game_service.play(self.game_diagonals, self.game_diagonals.board[0][2])
        self.game_service.play(self.game_diagonals, self.game_diagonals.board[3][0])
        self.assertEqual(self.game_service.check_winner(self.game_diagonals), -4)

    def test_row_is_detected(self):
        self.game_service.play(self.game_column_and_row, self.game_column_and_row.board[2][3])
        self.assertEqual(self.game_service.check_winner(self.game_column_and_row), 4)

    def test_column_is_detected(self):
        self.game_service.play(self.game_column_and_row, self.game_column_and_row.board[0][1])
        self.game_service.play(self.game_column_and_row, self.game_column_and_row.board[2][3])
        self.assertEqual(self.game_service.check_winner(self.game_column_and_row), -4)
