import unittest
from unittest.mock import patch
from io import StringIO
from tic_tac_game import TicTacGame


game = TicTacGame()


class TestInput(unittest.TestCase):
    @patch('builtins.input', return_value='t')
    def test_letter(self, mock_input):
        with patch('sys.stdout', new=StringIO()):
            game.board = ['X', 'X', '3']
            res = game.validate_input()
            self.assertEqual(res, False)

    @patch('builtins.input', return_value='100')
    def test_large_number(self, mock_input):
        with patch('sys.stdout', new=StringIO()):
            res = game.validate_input()
            self.assertEqual(res, False)

    @patch('builtins.input', return_value='1')
    def test_occup_position(self, mock_input):
        with patch('sys.stdout', new=StringIO()):
            res = game.validate_input()
            self.assertEqual(res, False)

    @patch('builtins.input', return_value='3')
    def test_right_number(self, mock_input):
        with patch('sys.stdout', new=StringIO()):
            res = game.validate_input()
            self.assertEqual(res, 3)


class TestWinnerDraw(unittest.TestCase):
    def test_winner(self):
        with patch('sys.stdout', new=StringIO()):
            game.board = list('123456789')
            arr_res = self.check_win_player('X')
            arr_true = [True for _ in range(8)]
            self.assertListEqual(arr_res, arr_true)
            arr_res = self.check_win_player('0')
            self.assertListEqual(arr_res, arr_true)
            game.board = list(range(1, 10))
            self.assertFalse(game.check_winner())

    @staticmethod
    def check_win_player(player):
        arr_res = []
        for i in range(3):
            game.board[i] = player
        arr_res.append(game.check_winner())
        for i in range(3):
            game.board[i] = i
            game.board[i + 3] = player
        arr_res.append(game.check_winner())
        for i in range(3):
            game.board[i + 3] = i + 3
            game.board[i + 6] = player
        arr_res.append(game.check_winner())
        game.board = list('123456789')
        for i in range(0, 7, 3):
            game.board[i] = player
        arr_res.append(game.check_winner())
        for i in range(1, 8, 3):
            game.board[i - 1] = i - 1
            game.board[i] = player
        arr_res.append(game.check_winner())
        for i in range(2, 9, 3):
            game.board[i - 1] = i - 1
            game.board[i] = player
        arr_res.append(game.check_winner())
        game.board = list('123456789')
        for i in range(0, 9, 4):
            game.board[i] = player
        arr_res.append(game.check_winner())
        game.board = list('123456789')
        for i in range(2, 7, 2):
            game.board[i] = player
        arr_res.append(game.check_winner())
        return arr_res

    def test_drawn(self):
        with patch('sys.stdout', new=StringIO()):
            game.board = ['X', 'X', '0', '0', '0', 'X', 'X', 'X', '0']
            res = game.check_draw()
            self.assertTrue(res)
            game.board = list(range(1, 10))
            res = game.check_draw()
            self.assertFalse(res)


class TestMove(unittest.TestCase):
    def test_move(self):
        game.board = list('123456789')
        game.update_board(3, '0')
        self.assertIn('0', game.board)
        game.update_board(7, 'X')
        game.update_board(9, '0')
        game.update_board(1, 'X')
        self.assertListEqual(game.board, list('X20456X80'))


class TestAnswer(unittest.TestCase):
    @patch('builtins.input', return_value='nope')
    def test_incor_input(self, mock_input):
        with patch('sys.stdout', new=StringIO()):
            self.assertEqual(False, game.validate_answer(['0', 'X']))

    @patch('builtins.input', return_value='0')
    def test_move_0(self, mock_input):
        with patch('sys.stdout', new=StringIO()):
            self.assertEqual('0', game.validate_answer(['0', 'X']))

    @patch('builtins.input', return_value='X')
    def test_move_x(self, mock_input):
        with patch('sys.stdout', new=StringIO()):
            self.assertEqual('X', game.validate_answer(['0', 'X']))

    @patch('builtins.input', return_value='yes')
    def test_random(self, mock_input):
        with patch('sys.stdout', new=StringIO()):
            self.assertEqual('X', game.validate_answer(['X', 'X']))

    @patch('builtins.input', return_value='exit')
    def test_exit(self, mock_input):
        with patch('sys.stdout', new=StringIO()):
            self.assertEqual('exit', game.validate_answer(['0', 'X']))


class TestNewGame(unittest.TestCase):
    def test_restart_game(self):
        with patch('sys.stdout', new=StringIO()):
            self.assertEqual(None, game.restart_game('no'))
            self.assertRaises(ValueError, game.restart_game, 'ddfdd')
