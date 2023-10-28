import random
import re


class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        self.board = self.make_new_board()
        self.assign_values_to_board()

        self.dug = set()

    def make_new_board(self):
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)

            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == "*":
                continue
            board[row][col] = "*"
            bombs_planted += 1
        return board

    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == "*":
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
        num_neighboring_bombs = 0

        for r in range(max(0, row - 1), min(self.dim_size - 1, (row + 1)) + 1):
            for c in range(max(0, col - 1), min(self.dim_size - 1, (col + 1)) + 1):
                if r == row and c == col:
                    continue  # me
                if self.board[r][c] == "*":
                    num_neighboring_bombs += 1
        return num_neighboring_bombs

    def dig(self, row, col):
        self.dug.add((row, col))

        if self.board[row][col] == "*":
            return False  # lose the game
        elif self.board[row][col] > 0:
            return True

        for r in range(max(0, row - 1), min(self.dim_size - 1, (row + 1)) + 1):
            for c in range(max(0, col - 1), min(self.dim_size - 1, (col + 1)) + 1):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)
        return True

    def __str__(self) -> str:
        visible_board = [
            [None for _ in range(self.dim_size)] for _ in range(self.dim_size)
        ]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = " "

        string_rep = ""
        widths = []

        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(len(max(columns, key=len)))

        indices = [i for i in range(self.dim_size)]
        indices_row = "   "
        cells = []
        for idx, col in enumerate(indices):
            format = "%-" + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += "  ".join(cells)
        indices_row += "  \n"

        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f"{i} |"
            cells = []
            for idx, col in enumerate(row):
                format = "%-" + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += " |".join(cells)
            string_rep += " |\n"

        str_len = len(string_rep) // self.dim_size
        string_rep = indices_row + "-" * str_len + "\n" + string_rep + "-" * str_len

        return string_rep


def play(dim_size=10, num_bombs=10):
    game = Board(dim_size, num_bombs)

    safe = True
    while len(game.dug) < game.dim_size**2 - num_bombs:
        print(game)

        user_input = re.split(
            ",(\\s)*", input("Onde voce deseja jogar? Insira a linha e coluna: ")
        )
        row, col = int(user_input[0]), int(user_input[-1])

        if row < 0 or row >= game.dim_size or col < 0 or col >= game.dim_size:
            print("Jogada Invalida")
            continue

        safe = game.dig(row, col)

        if not safe:
            return (False, game)

    return (True, game)


def main():
    options = re.split(
        ",(\\s)*", input("Defina o Tamanho do campo e o numero de bombas: ")
    )
    status, jogo = play(int(options[0]), int(options[-1]))
    if status:
        print("Voce ganhou parabens")
    else:
        print("Voce perdeu")
    print(jogo)


if __name__ == "__main__":
    print(
        """
          B E M  V I N D O
    AO  C A M P O  M I N A D O !
====================================
        """
    )
    main()
