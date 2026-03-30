import tkinter as tk
from board import Board

class ChessGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Zjednodušené šachy")

        self.board = Board(self.root)

    def run(self):
        self.root.mainloop()