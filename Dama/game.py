from board import create_board, print_board, is_inside
from pieces import can_move, move_piece, is_valid_piece


class Game:
    def __init__(self):
        self.board = create_board()
        self.player = "white"

    def switch_player(self):
        self.player = "black" if self.player == "white" else "white"

    def check_winner(self):
        white = sum(row.count("w") for row in self.board)
        black = sum(row.count("b") for row in self.board)

        if white == 0:
            return "black"
        if black == 0:
            return "white"
        return None

    def play_turn(self):
        print_board(self.board)
        print(f"Na tahu: {self.player}")

        try:
            x1, y1 = map(int, input("Start (x y): ").split())
            x2, y2 = map(int, input("Cíl (x y): ").split())
        except ValueError:
            print("❌ Špatný vstup!")
            return

        if not is_inside(x1, y1) or not is_inside(x2, y2):
            print("❌ Mimo desku")
            return

        piece = self.board[y1][x1]

        if piece == " ":
            print("❌ Na startu není kámen")
            return

        if not is_valid_piece(piece, self.player):
            print("❌ Nejsi na tahu tímto kamenem")
            return

        if can_move(self.board, x1, y1, x2, y2, self.player):
            move_piece(self.board, x1, y1, x2, y2)
            self.switch_player()
        else:
            print("❌ Neplatný tah")

    def run(self):
        while True:
            winner = self.check_winner()
            if winner:
                print(f"🏆 Vyhrál: {winner}")
                break

            self.play_turn()