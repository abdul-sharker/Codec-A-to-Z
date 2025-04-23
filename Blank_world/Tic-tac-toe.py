import tkinter as tk
from tkinter import messagebox
import random

class TicTacToeAI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe vs AI")

        self.board = [""] * 9
        self.buttons = []

        self.create_board()

    def create_board(self):
        for i in range(9):
            button = tk.Button(self.root, text="", font=('Arial', 24), width=5, height=2,
                               command=lambda i=i: self.player_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def player_move(self, index):
        if self.board[index] == "":
            self.board[index] = "X"
            self.buttons[index].config(text="X")
            if self.check_game_over("X"):
                return
            self.root.after(500, self.ai_move)

    def ai_move(self):
        index = self.best_move()
        if index is not None:
            self.board[index] = "O"
            self.buttons[index].config(text="O")
            self.check_game_over("O")

    def best_move(self):
        # Try to win
        for i in self.available_moves():
            self.board[i] = "O"
            if self.check_winner("O"):
                self.board[i] = ""
                return i
            self.board[i] = ""

        # Try to block player
        for i in self.available_moves():
            self.board[i] = "X"
            if self.check_winner("X"):
                self.board[i] = ""
                return i
            self.board[i] = ""

        # Pick random
        return random.choice(self.available_moves()) if self.available_moves() else None

    def available_moves(self):
        return [i for i in range(9) if self.board[i] == ""]

    def check_winner(self, player):
        combos = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]
        return any(all(self.board[i] == player for i in combo) for combo in combos)

    def check_game_over(self, player):
        if self.check_winner(player):
            messagebox.showinfo("Game Over", f"{'You' if player == 'X' else 'AI'} win!")
            self.reset_board()
            return True
        elif "" not in self.board:
            messagebox.showinfo("Game Over", "It's a draw!")
            self.reset_board()
            return True
        return False

    def reset_board(self):
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeAI(root)
    root.mainloop()
