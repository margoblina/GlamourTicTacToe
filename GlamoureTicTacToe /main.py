#загружаем библиотеку и штуки, которые нам нужны из неё
import tkinter as tk
from pygame import mixer
from tkinter import messagebox

#загружаем музыку
mixer.init()
mixer.music.load('glamour.mp3')

class GlamourTicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Крестики-нолики")
        #делаем фон розовым
        self.master.configure(bg="#F81894") 
        #заменяем значок на цветок
        self.current_player = "🌺" 
        #строим доску
        self.board = [""] * 9 
 #делаем оформление кнопочек
        self.buttons = [tk.Button(master, text="", font=("Arial", 24), width=5, height=2, 
                                  #снова делаем оформление самих крестиков-ноликов
                                  command=lambda i=i: self.make_move(i), bg="#F81894", fg="white") for i in range(9)] 

        #нумеруем ячейки табличек
        for i, button in enumerate(self.buttons):
            button.grid(row=i // 3, column=i % 3) 

    #создаём правила игры и делаем проверку победы или ничьи
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

     #задаём, в каких ячейках должны быть знаки, чтобы случилась победа
    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6) 
        ]
        #прописываем условия победы
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "": 
                return True
        return False

    #делаем так, чтобы игра начиналась бесконечно
    def reset_game(self):
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")
        self.current_player = "🌺" 

#делаем запуск игры
if __name__ == "__main__":
    root = tk.Tk()
    game = GlamourTicTacToe(root)
    mixer.music.play(loops=-1)
    root.mainloop() 
