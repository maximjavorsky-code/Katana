"""
Dáma - konzolová hra pro 2 hráče
Autor: student
Popis:
Jednoduchá implementace hry Dáma v terminálu.
Hráči se střídají v tazích a snaží se vyřadit soupeřovy kameny.
"""

BOARD_SIZE = 8


def create_board():
    """Vytvoří základní hrací desku."""
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
    """Vykreslení desky v konzoli."""
    print("\n  " + " ".join(map(str, range(BOARD_SIZE))))
    for i, row in enumerate(board):
        print(i, " ".join(row))
    print()


def is_inside(x, y):
    """Kontrola zda je pozice v rámci hrací plochy."""
    return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE


def get_player_pieces(player):
    """Vrátí kameny hráče."""
    return ("w", "W") if player == "white" else ("b", "B")


def move_direction(player):
    """Směr pohybu běžných kamenů."""
    return -1 if player == "white" else 1


def valid_move(board, x1, y1, x2, y2, player):
    """Základní validace tahu."""
    if not (is_inside(x2, y2)):
        return False

    piece = board[y1][x1]
    target = board[y2][x2]

    if target != " ":
        return False

    dx = x2 - x1
    dy = y2 - y1

    if piece.lower() == "w" or piece.lower() == "b":
        direction = move_direction(player)

        # normální pohyb
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


def make_move(board, x1, y1, x2, y2):
    """Provede tah a případné vyhození kamene."""
    piece = board[y1][x1]
    board[y1][x1] = " "
    board[y2][x2] = piece

    # pokud je to skok, smaž soupeře
    if abs(x2 - x1) == 2:
        mid_x = (x1 + x2) // 2
        mid_y = (y1 + y2) // 2
        board[mid_y][mid_x] = " "


def check_winner(board):
    """Kontrola výhry."""
    white = sum(row.count("w") + row.count("W") for row in board)
    black = sum(row.count("b") + row.count("B") for row in board)

    if white == 0:
        return "black"
    if black == 0:
        return "white"
    return None


def main():
    board = create_board()
    player = "white"

    while True:
        print_board(board)
        winner = check_winner(board)

        if winner:
            print(f"Vyhrál hráč: {winner}")
            break

        print(f"Na tahu: {player}")

        try:
            x1, y1 = map(int, input("Zadej start (x y): ").split())
            x2, y2 = map(int, input("Zadej cíl (x y): ").split())
        except ValueError:
            print("Neplatný vstup!")
            continue

        piece = board[y1][x1]

        if piece == " ":
            print("Na poli není kámen!")
            continue

        if player == "white" and piece.lower() != "w":
            print("To není tvůj kámen!")
            continue

        if player == "black" and piece.lower() != "b":
            print("To není tvůj kámen!")
            continue

        if valid_move(board, x1, y1, x2, y2, player):
            make_move(board, x1, y1, x2, y2)
            player = "black" if player == "white" else "white"
        else:
            print("Neplatný tah!")


if __name__ == "__main__":
    main()