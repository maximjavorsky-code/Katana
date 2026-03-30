import tkinter as tk
import tkinter.messagebox
from pieces import create_pieces

TILE_SIZE = 80


class Board:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=640, height=640)
        self.canvas.pack()

        self.selected = None
        self.turn = "blue"  # 🔵 začíná modrý hráč

        # vytvoření šachovnice (8x8 pole)
        self.grid = [[None for _ in range(8)] for _ in range(8)]

        create_pieces(self.grid)

        self.draw_board()
        self.canvas.bind("<Button-1>", self.click)

    def draw_board(self):
        self.canvas.delete("all")

        for row in range(8):
            for col in range(8):
                # barvy šachovnice
                tile_color = "#EEEED2" if (row + col) % 2 == 0 else "#769656"

                x1 = col * TILE_SIZE
                y1 = row * TILE_SIZE
                x2 = x1 + TILE_SIZE
                y2 = y1 + TILE_SIZE

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=tile_color)

                # zvýraznění vybrané figury
                if self.selected == (row, col):
                    self.canvas.create_rectangle(
                        x1, y1, x2, y2,
                        outline="yellow", width=3
                    )

                piece = self.grid[row][col]
                if piece:
                    color = "blue" if piece.color == "blue" else "red"

                    self.canvas.create_text(
                        x1 + 40, y1 + 40,
                        text=piece.symbol,
                        fill=color,
                        font=("Arial", 28)
                    )

    def click(self, event):
        col = event.x // TILE_SIZE
        row = event.y // TILE_SIZE

        piece = self.grid[row][col]

        if self.selected:
            sel_row, sel_col = self.selected
            sel_piece = self.grid[sel_row][sel_col]

            # pokus o tah
            if sel_piece and sel_piece.color == self.turn:
                if sel_piece.valid_move(sel_row, sel_col, row, col, self.grid):

                    target = self.grid[row][col]

                    # 🏆 kontrola konce hry (král)
                    if target and target.symbol in ["♔", "♚"]:
                        if self.turn == "blue":
                            winner = "modrý hráč"
                        else:
                            winner = "červený hráč"

                        tk.messagebox.showinfo(
                            "Konec hry",
                            f"Konec hry, vyhrál {winner}"
                        )

                        self.canvas.unbind("<Button-1>")
                        return

                    # provedení tahu
                    self.grid[row][col] = sel_piece
                    self.grid[sel_row][sel_col] = None

                    # střídání hráče
                    self.turn = "red" if self.turn == "blue" else "blue"

            self.selected = None
        else:
            if piece and piece.color == self.turn:
                self.selected = (row, col)

        self.draw_board()