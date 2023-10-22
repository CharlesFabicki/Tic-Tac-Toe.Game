import tkinter as tk


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


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row, col = map(int, input(
            f"Player {current_player}, choose row (0-2) and column (0-2) separated by a space: ").split())

        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
            print("Invalid move. Try again.")
            continue

        board[row][col] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"


class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(root, text=" ", font=("normal", 24), width=5, height=2,
                                               command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if check_win(self.board, self.current_player):
                self.show_winner()
            elif is_full(self.board):
                self.show_tie()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def show_winner(self):
        winner_label = tk.Label(self.root, text=f"Player {self.current_player} wins!", font=("normal", 16))
        winner_label.grid(row=3, column=0, columnspan=3)
        self.disable_buttons()

    def show_tie(self):
        tie_label = tk.Label(self.root, text="It's a tie!", font=("normal", 16))
        tie_label.grid(row=3, column=0, columnspan=3)
        self.disable_buttons()

    def disable_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()
