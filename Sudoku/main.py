# Sudoku hra v konzoli

# Vytvoření hracího pole (0 = prázdné pole)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],

    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],

    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Funkce pro vykreslení hracího pole
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

# Funkce pro kontrolu, zda je tah platný
def is_valid(board, num, pos):
    # kontrola řádku
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # kontrola sloupce
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # kontrola 3x3 bloku
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

# Funkce pro kontrolu dokončení hry
def is_complete(board):
    for row in board:
        if 0 in row:
            return False
    return True

# Hlavní herní smyčka
def game():
    while True:
        print_board(board)

        if is_complete(board):
            print("Gratulace! Sudoku je vyřešeno.")
            break

        try:
            user_input = input("Zadej řádek, sloupec a číslo (např. 0 1 5), nebo 'q' pro konec: ")

            if user_input.lower() == 'q':
                print("Hra ukončena.")
                break

            row, col, num = map(int, user_input.split())

            # kontrola rozsahu
            if row not in range(9) or col not in range(9) or num not in range(1, 10):
                print("Neplatný vstup!")
                continue

            # kontrola prázdného pole
            if board[row][col] != 0:
                print("Pole už je obsazené!")
                continue

            # kontrola pravidel Sudoku
            if is_valid(board, num, (row, col)):
                board[row][col] = num
            else:
                print("Tento tah porušuje pravidla Sudoku!")

        except:
            print("Chybný vstup!")

# Spuštění hry
game()