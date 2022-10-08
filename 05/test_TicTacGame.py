import unittest

from TicTacGame import TicTacGame


game = TicTacGame()


class TestInput(unittest.TestCase):
    def setUp(self):
        game.board = ['X', 'X', '3']

    def test_number(self):
        res = game.validate_input('t')
        self.assertEqual(res, True)

        res = game.validate_input('3')
        self.assertEqual(res, False)

        res = game.validate_input('1')
        self.assertEqual(res, True)


class TestWinnerDraw(unittest.TestCase):
    def test_winner(self):
        game.board = list('123456789')
        arr_res = self.check_win_player('X')
        arr_true = [True for i in range(8)]
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
        game.board = ['X', 'X', '0', '0', '0', 'X', 'X', 'X', '0']
        res = game.check_draw()
        self.assertTrue(res)
        game.board = list(range(1, 10))
        res = game.check_draw()
        self.assertFalse(res)


class TestMove(unittest.TestCase):
    def setUp(self):
        game.board = list('123456789')

    def test_move(self):
        game.update_board(3, '0')
        self.assertIn('0', game.board)
        game.update_board(7, 'X')
        game.update_board(9, '0')
        game.update_board(1, 'X')
        self.assertListEqual(game.board, list('X20456X80'))


class TestAnswer(unittest.TestCase):
    def test_validate_answer(self):
        self.assertRaises(ValueError, game.validate_answer, 'nope', ['0', 'X'])
        self.assertEqual('0', game.validate_answer('0', ['0', 'X']))
        self.assertEqual('X', game.validate_answer('X', ['0', 'X']))
        self.assertEqual('X', game.validate_answer('yes', ['X', 'X']))
        self.assertEqual('-1', game.validate_answer('-1', ['0', 'X']))


class TestNewGame(unittest.TestCase):
    def test_restart_game(self):
        self.assertEqual(None, game.restart_game('no'))
        self.assertRaises(ValueError, game.restart_game, 'ddfdd')
