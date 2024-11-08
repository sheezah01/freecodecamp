import random
import re
from colorama import Fore, Style

class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        self.board = self.make_new_board()
        self.assign_values_to_board()
        self.dug = set()

    def make_new_board(self):
        board = [[' ' for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            row = random.randint(0, self.dim_size - 1)
            col = random.randint(0, self.dim_size - 1)
            if board[row][col] == '*':
                continue
            board[row][col] = '*'
            bombs_planted += 1
        return board

    def assign_values_to_board(self):
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if self.board[row][col] == '*':
                    continue
                self.board[row][col] = self.get_num_neighboring_bombs(row, col)

    def get_num_neighboring_bombs(self, row, col):
        num_bombs = 0
        for r in range(max(0, row - 1), min(self.dim_size, row + 2)):
            for c in range(max(0, col - 1), min(self.dim_size, col + 2)):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    num_bombs += 1
        return num_bombs

    def dig(self, row, col):
        self.dug.add((row, col))
        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        for r in range(max(0, row - 1), min(self.dim_size, row + 2)):
            for c in range(max(0, col - 1), min(self.dim_size, col + 2)):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)

        return True

    def __str__(self):
        visible_board = [[Fore.WHITE + Style.BRIGHT + '.' + Style.RESET_ALL for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    if self.board[row][col] == '*':
                        visible_board[row][col] = Fore.RED + Style.BRIGHT + '*' + Style.RESET_ALL
                    else:
                        visible_board[row][col] = Fore.BLUE + Style.BRIGHT + str(self.board[row][col]) + Style.RESET_ALL
        return '\n'.join([''.join(row) for row in visible_board])

class GameUI:
    def __init__(self, board):
        self.board = board

    def play(self):
        safe = True
        while len(self.board.dug) < self.board.dim_size ** 2 - self.board.num_bombs:
            print(self.board)
            try:
                row, col = map(int, input("Where would you like to dig? Input as row,col: ").split(','))
            except ValueError:
                print("Invalid input. Please try again.")
                continue

            if row < 0 or row >= self.board.dim_size or col < 0 or col >= self.board.dim_size:
                print("Invalid location. Try again.")
                continue

            safe = self.board.dig(row, col)
            if not safe:
                break

        if safe:
            print(Fore.GREEN + Style.BRIGHT + "Congratulations! You won!" + Style.RESET_ALL)
        else:
            print(Fore.RED + Style.BRIGHT + "Game over!" + Style.RESET_ALL)
            self.board.dug = [(r, c) for r in range(self.board.dim_size) for c in range(self.board.dim_size)]
            print(self.board)

def main():
    board = Board(10, 10)
    game_ui = GameUI(board)
    game_ui.play()

if __name__ == '__main__':
    main()