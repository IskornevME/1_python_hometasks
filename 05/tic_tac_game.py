'''
This file realizes tic tac game
'''

import random


class RangeValueError(Exception):
    pass


class IntValueError(RangeValueError):
    pass


class TicTacGame:
    '''
    This is class for Tic Tac Game.
    '''
    board = list(range(1, 10))

    def check_draw(self):
        for i in list(range(1, 10)):
            if i in self.board:
                return False
        print("Oops, seems like we have a draw! What a tense game!")
        return True

    def show_board(self):
        print('-------------')
        print("| %s | %s | %s |\n -----------" % (self.board[0], self.board[1], self.board[2]))
        print("| %s | %s | %s |\n -----------" % (self.board[3], self.board[4], self.board[5]))
        print("| %s | %s | %s |" % (self.board[6], self.board[7], self.board[8]))
        print('-------------')

    def update_board(self, number, player):
        self.board[number - 1] = player

    def validate_input(self):
        try:
            number = input()
            if number == 'exit':
                return number
            if not number.isdigit():
                raise IntValueError
            if int(number) > 9 or int(number) < 1:
                raise RangeValueError
        except IntValueError:
            print("Please enter positive integer value or 'exit'")
            print(f"You entered {number}")
            return False
        except RangeValueError:
            print("Incorrect input. Please input integer number from 1 to 9")
            print(f"You entered {number}")
            return False
        number = int(number)
        if self.board[number - 1] in ["0", "X"]:
            print("Sorry, this position occupied. Enter another number")
            return False
        return number

    @staticmethod
    def validate_answer(players):
        ans = input()
        tmp = random.randint(0, 1)
        try:
            if ans == "yes":
                return players[tmp]
            if ans == players[0]:
                return '0'
            if ans == players[1]:
                return 'X'
            if ans == 'exit':
                print("Goodbye, see you next time")
                return ans
            raise ValueError
        except ValueError:
            print("Incorrect input.")
            print("Acceptable values 'yes', '0', 'X', 'exit'. Try again")
            return False

    def print_rules(self):
        print("Hello! This is a TicTac game!\n"
              "We think you now the rules, but we need to make some notices.\n"
              "Now you see our board with numbers. Each numbers denotes a position.\n"
              "All you need to do is type desired number and then your symbol will replace "
              "the number.\nSo, you should input integer number from 1 to 9.\n")
        self.show_board()
        print("And here is one more thing:\n"
              "If you want random choice of move type 'yes', otherwise type 'X' or '0'.")
        print("If you want to end the game just type 'exit'.")

    def start_game(self):
        self.print_rules()
        players = ['0', 'X']
        player = self.validate_answer(players)
        while not player:
            player = self.validate_answer(players)
        if player == 'exit':
            return
        while True:
            print(f"Player {player} please make your move.")
            number = self.validate_input()
            while not number:
                number = self.validate_input()
            if number == 'exit':
                print("Goodbye, see you next time")
                self.board = list(range(1, 10))
                return
            self.update_board(number, player)
            self.show_board()
            if self.check_winner():
                break
            if self.check_draw():
                self.board = list(range(1, 10))
                break
            player = players[int(not players.index(player))]
        print("\nDo you want to play one more time?\nEnter 'yes' or 'no'")
        ans = input()
        self.restart_game(ans)

    def restart_game(self, ans):
        if ans == 'yes':
            self.board = list(range(1, 10))
            print("")
            self.start_game()
        elif ans == 'no':
            self.board = list(range(1, 10))
            print("Goodbye, see you next time.")
            return
        else:
            raise ValueError("Incorrect input. Acceptable values 'yes', 'no'.")

    def check_winner(self):
        winner_comb = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                       [0, 3, 6], [1, 4, 7], [2, 5, 8],
                       [0, 4, 8], [6, 4, 2]]
        for comb in winner_comb:
            if self.board[comb[0]] == self.board[comb[1]] == self.board[comb[2]] == '0':
                print("Player 0 is on fire! Somebody stop him."
                      "We have new TicTac game champion!")
                return True
            if self.board[comb[0]] == self.board[comb[1]] == self.board[comb[2]] == 'X':
                print("Player X, what an amazing game! Pure class."
                      "We have new TicTac game champion!")
                return True
        return False


if __name__ == "__main__":
    game = TicTacGame()
    game.start_game()
