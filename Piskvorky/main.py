"""
Jednoduchá konzolová hra Piškvorky (Tic-Tac-Toe)
Hrají dva hráči střídavě (X a O)
"""

def zobraz_pole(pole):
    """Vykreslí herní pole do konzole"""
    print("\n")
    for i in range(3):
        print(" | ".join(pole[i]))
        if i < 2:
            print("--+---+--")
    print("\n")


def kontrola_vyhry(pole, hrac):
    """Zkontroluje, zda hráč vyhrál"""

    # Kontrola řádků
    for radek in pole:
        if all(policko == hrac for policko in radek):
            return True

    # Kontrola sloupců
    for sloupec in range(3):
        if all(pole[radek][sloupec] == hrac for radek in range(3)):
            return True

    # Kontrola diagonál
    if all(pole[i][i] == hrac for i in range(3)):
        return True

    if all(pole[i][2 - i] == hrac for i in range(3)):
        return True

    return False


def kontrola_remizy(pole):
    """Zkontroluje, zda je hra remíza"""
    for radek in pole:
        if " " in radek:
            return False
    return True


def ziskej_tah(hrac):
    """Získá tah od hráče"""
    while True:
        try:
            radek = int(input(f"Hráč {hrac} - zadej řádek (0-2): "))
            sloupec = int(input(f"Hráč {hrac} - zadej sloupec (0-2): "))

            if radek not in range(3) or sloupec not in range(3):
                print("Neplatné souřadnice, zkus znovu.")
                continue

            return radek, sloupec

        except ValueError:
            print("Zadej číslo!")


def hra():
    """Hlavní funkce hry"""

    # Vytvoření prázdného pole
    pole = [[" " for _ in range(3)] for _ in range(3)]

    aktualni_hrac = "X"

    while True:
        zobraz_pole(pole)

        # Získání tahu
        radek, sloupec = ziskej_tah(aktualni_hrac)

        # Kontrola obsazenosti pole
        if pole[radek][sloupec] != " ":
            print("Toto pole je již obsazené!")
            continue

        # Zapsání tahu
        pole[radek][sloupec] = aktualni_hrac

        # Kontrola výhry
        if kontrola_vyhry(pole, aktualni_hrac):
            zobraz_pole(pole)
            print(f"Hráč {aktualni_hrac} vyhrál!")
            break

        # Kontrola remízy
        if kontrola_remizy(pole):
            zobraz_pole(pole)
            print("Remíza!")
            break

        # Střídání hráče
        aktualni_hrac = "O" if aktualni_hrac == "X" else "X"


# Spuštění hry
if __name__ == "__main__":
    hra()