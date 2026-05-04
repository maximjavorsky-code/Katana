import random

# Konstanty pro velikost hrací plochy
BOARD_SIZE = 5
SHIP_COUNT = 3

def create_board():
    """
    Vytvoří prázdné herní pole.
    Každé pole je reprezentováno znakem '~'.
    """
    return [["~" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


def print_board(board, hide_ships=True):
    """
    Vykreslí herní pole do konzole.
    hide_ships = True znamená, že lodě nejsou viditelné.
    """
    for row in board:
        for cell in row:
            if hide_ships and cell == "S":
                print("~", end=" ")
            else:
                print(cell, end=" ")
        print()
    print()


def place_ships(board):
    """
    Náhodně rozmístí lodě na herní pole.
    Lodě jsou reprezentovány znakem 'S'.
    """
    ships = 0

    while ships < SHIP_COUNT:
        x = random.randint(0, BOARD_SIZE - 1)
        y = random.randint(0, BOARD_SIZE - 1)

        # Kontrola, zda už na pozici není loď
        if board[x][y] != "S":
            board[x][y] = "S"
            ships += 1


def get_player_input():
    """
    Získá vstup od hráče a ověří jeho platnost.
    """
    while True:
        try:
            x = int(input("Zadej řádek (0-4): "))
            y = int(input("Zadej sloupec (0-4): "))

            if 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE:
                return x, y
            else:
                print("Souřadnice mimo hrací pole!")
        except ValueError:
            print("Zadej čísla!")


def check_hit(board, x, y):
    """
    Vyhodnotí zásah hráče.
    Vrací True pokud byl zásah, jinak False.
    """
    if board[x][y] == "S":
        board[x][y] = "X"
        print("Zásah!")
        return True
    elif board[x][y] == "~":
        board[x][y] = "O"
        print("Vedle.")
        return False
    else:
        print("Už jsi sem střílel.")
        return False


def check_win(board):
    """
    Zkontroluje, zda byly všechny lodě potopeny.
    """
    for row in board:
        if "S" in row:
            return False
    return True


def main():
    """
    Hlavní funkce hry.
    """
    board = create_board()
    place_ships(board)

    print("=== HRA LODĚ ===")

    while True:
        print_board(board)
        x, y = get_player_input()
        check_hit(board, x, y)

        # Kontrola výhry
        if check_win(board):
            print("Vyhrál jsi! Všechny lodě potopeny.")
            print_board(board, hide_ships=False)
            break
while True:
    if input() == "konec":
        break