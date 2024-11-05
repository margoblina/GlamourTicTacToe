import tkinter as tk
from pygame import mixer
from tkinter import messagebox

mixer.init()
mixer.music.load('glamour.mp3')

class GlamourTicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Крестики-нолики")
        self.master.configure(bg="#F81894")
        self.current_player = "🌺"
        self.board = [""] * 9

        self.buttons = [tk.Button(master, text="", font=("Arial", 24), width=5, height=2,
                                  command=lambda i=i: self.make_move(i), bg="#F81894", fg="white") for i in range(9)]

        for i, button in enumerate(self.buttons):
            button.grid(row=i // 3, column=i % 3)

    def make_move(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Победа!", f"Игрок {self.current_player} выиграл!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Ничья!", "Игра завершилась вничью.")
                self.reset_game()
            else:
                self.current_player = "❤" if self.current_player == "🌺" else "🌺"

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False

    def reset_game(self):
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")
        self.current_player = "🌺"


if __name__ == "__main__":
    root = tk.Tk()
    game = GlamourTicTacToe(root)
    mixer.music.play(loops=-1)
    root.mainloop()