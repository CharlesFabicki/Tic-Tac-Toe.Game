import tkinter as tk
import random


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True


class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe AI Game")
        self.initialize_game()

    def initialize_game(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text=" ", font=("normal", 24), width=5, height=2,
                                               command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)

        self.play_again_button = tk.Button(self.root, text="Play Again", command=self.play_again)
        self.play_again_button.grid(row=3, column=0, columnspan=3)
        self.winner_label = tk.Label(self.root, text="", font=("normal", 16))
        self.winner_label.grid(row=4, column=0, columnspan=3)

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if check_win(self.board, self.current_player):
                self.show_winner()
            elif is_full(self.board):
                self.show_tie()
            else:
                self.current_player = "O"
                self.make_ai_move()

    def make_ai_move(self):
        if self.current_player == "O":
            available_moves = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == " "]
            row, col = random.choice(available_moves)
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if check_win(self.board, self.current_player):
                self.show_winner()
            elif is_full(self.board):
                self.show_tie()
            else:
                self.current_player = "X"

    def show_winner(self):
        if self.current_player == "X":
            self.winner_label.config(text="You won!")
        else:
            self.winner_label.config(text=f"Player {self.current_player} wins!")
        self.winner_label.grid(row=4, column=0, columnspan=3)
        self.disable_buttons()

    def show_tie(self):
        self.winner_label.config(text="It's a tie!")
        self.winner_label.grid(row=4, column=0, columnspan=3)
        self.disable_buttons()

    def disable_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state=tk.DISABLED)
        self.play_again_button.config(state=tk.NORMAL)

    def play_again(self):
        self.winner_label.config(text="")
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].destroy()
        self.play_again_button.destroy()
        self.initialize_game()


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()
