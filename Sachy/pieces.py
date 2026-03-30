# Definice figur a jejich pohybu

class Piece:
    def __init__(self, color, symbol):
        self.color = color  # "blue" nebo "red"
        self.symbol = symbol

    def enemy(self, other):
        return other is not None and other.color != self.color

    def valid_move(self, sr, sc, tr, tc, board):
        return False


class Pawn(Piece):
    def __init__(self, color):
        symbol = "♙" if color == "blue" else "♟"
        super().__init__(color, symbol)

    def valid_move(self, sr, sc, tr, tc, board):
        direction = -1 if self.color == "blue" else 1

        # pohyb dopředu
        if sc == tc and board[tr][tc] is None:
            if tr == sr + direction:
                return True

        # braní šikmo
        if abs(tc - sc) == 1 and tr == sr + direction:
            if self.enemy(board[tr][tc]):
                return True

        return False


class Rook(Piece):
    def __init__(self, color):
        symbol = "♖" if color == "blue" else "♜"
        super().__init__(color, symbol)

    def valid_move(self, sr, sc, tr, tc, board):
        if sr != tr and sc != tc:
            return False

        # kontrola cesty
        if sr == tr:
            step = 1 if tc > sc else -1
            for c in range(sc + step, tc, step):
                if board[sr][c] is not None:
                    return False
        else:
            step = 1 if tr > sr else -1
            for r in range(sr + step, tr, step):
                if board[r][sc] is not None:
                    return False

        return board[tr][tc] is None or self.enemy(board[tr][tc])


class Bishop(Piece):
    def __init__(self, color):
        symbol = "♗" if color == "blue" else "♝"
        super().__init__(color, symbol)

    def valid_move(self, sr, sc, tr, tc, board):
        if abs(sr - tr) != abs(sc - tc):
            return False

        step_r = 1 if tr > sr else -1
        step_c = 1 if tc > sc else -1

        r, c = sr + step_r, sc + step_c
        while r != tr:
            if board[r][c] is not None:
                return False
            r += step_r
            c += step_c

        return board[tr][tc] is None or self.enemy(board[tr][tc])


class Knight(Piece):
    def __init__(self, color):
        symbol = "♘" if color == "blue" else "♞"
        super().__init__(color, symbol)

    def valid_move(self, sr, sc, tr, tc, board):
        if (abs(sr - tr), abs(sc - tc)) in [(2, 1), (1, 2)]:
            return board[tr][tc] is None or self.enemy(board[tr][tc])
        return False


class Queen(Piece):
    def __init__(self, color):
        symbol = "♕" if color == "blue" else "♛"
        super().__init__(color, symbol)

    def valid_move(self, sr, sc, tr, tc, board):
        # kombinuje věž + střelec
        rook = Rook(self.color)
        bishop = Bishop(self.color)
        return rook.valid_move(sr, sc, tr, tc, board) or \
               bishop.valid_move(sr, sc, tr, tc, board)


class King(Piece):
    def __init__(self, color):
        symbol = "♔" if color == "blue" else "♚"
        super().__init__(color, symbol)

    def valid_move(self, sr, sc, tr, tc, board):
        if abs(sr - tr) <= 1 and abs(sc - tc) <= 1:
            return board[tr][tc] is None or self.enemy(board[tr][tc])
        return False


def create_pieces(board):
    # pěšci
    for i in range(8):
        board[1][i] = Pawn("red")
        board[6][i] = Pawn("blue")

    # věže
    board[0][0] = board[0][7] = Rook("red")
    board[7][0] = board[7][7] = Rook("blue")

    # koně
    board[0][1] = board[0][6] = Knight("red")
    board[7][1] = board[7][6] = Knight("blue")

    # střelci
    board[0][2] = board[0][5] = Bishop("red")
    board[7][2] = board[7][5] = Bishop("blue")

    # dáma
    board[0][3] = Queen("red")
    board[7][3] = Queen("blue")

    # král
    board[0][4] = King("red")
    board[7][4] = King("blue")