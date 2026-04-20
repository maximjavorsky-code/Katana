def get_direction(player):
    return -1 if player == "white" else 1


def is_valid_piece(piece, player):
    if player == "white":
        return piece == "w"
    return piece == "b"


def can_move(board, x1, y1, x2, y2, player):
    piece = board[y1][x1]
    target = board[y2][x2]

    if target != " ":
        return False

    dx = x2 - x1
    dy = y2 - y1
    direction = get_direction(player)

    # normální krok
    if abs(dx) == 1 and dy == direction:
        return True

    # skok (braní)
    if abs(dx) == 2 and dy == 2 * direction:
        mid_x = (x1 + x2) // 2
        mid_y = (y1 + y2) // 2
        mid_piece = board[mid_y][mid_x]

        if mid_piece != " " and mid_piece.lower() != piece.lower():
            return True

    return False


def move_piece(board, x1, y1, x2, y2):
    piece = board[y1][x1]
    board[y1][x1] = " "
    board[y2][x2] = piece

    # odstranění při skoku
    if abs(x2 - x1) == 2:
        mid_x = (x1 + x2) // 2
        mid_y = (y1 + y2) // 2
        board[mid_y][mid_x] = " "