BOARD_SIZE = 8


def create_board():
    board = [[" " for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    # černé kameny
    for y in range(3):
        for x in range(BOARD_SIZE):
            if (x + y) % 2 == 1:
                board[y][x] = "b"

    # bílé kameny
    for y in range(5, 8):
        for x in range(BOARD_SIZE):
            if (x + y) % 2 == 1:
                board[y][x] = "w"

    return board


def print_board(board):
    print("\n  " + " ".join(map(str, range(BOARD_SIZE))))
    for i, row in enumerate(board):
        print(i, " ".join(row))
    print()


def is_inside(x, y):
    return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE