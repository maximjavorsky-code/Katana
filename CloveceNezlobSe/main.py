"""
ČLOVĚČE, NEZLOB SE (jednoduchá textová verze)

Popis:
- 2–4 hráči
- Každý má 4 figurky
- Cílem je dostat všechny figurky do cíle
- Pohyb podle hodu kostkou

Poznámka: Jednoduchá implementace pro školní projekt (CLI verze)
"""

import random

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.positions = [-1, -1, -1, -1]  # -1 = doma

    def all_finished(self):
        return all(pos == 40 for pos in self.positions)


class Game:
    def __init__(self, players):
        self.players = players
        self.current_player = 0

    def roll_dice(self):
        return random.randint(1, 6)

    def move_piece(self, player, piece_index, steps):
        pos = player.positions[piece_index]

        # figurka je doma
        if pos == -1:
            if steps == 6:
                player.positions[piece_index] = 0
                print("Figurka nasazena na start!")
            else:
                print("Potřebuješ 6 pro nasazení.")
            return

        # pohyb po herním plánu
        new_pos = pos + steps
        if new_pos > 40:
            print("Nelze táhnout, přesáhl bys cíl.")
            return

        player.positions[piece_index] = new_pos
        print(f"Figurka posunuta na {new_pos}")

    def play_turn(self, player):
        print(f"\nHraje: {player.name}")
        print("Pozice:", player.positions)

        dice = self.roll_dice()
        print(f"Hodil jsi: {dice}")

        try:
            piece = int(input("Vyber figurku (0-3): "))
            self.move_piece(player, piece, dice)
        except:
            print("Neplatný vstup.")

    def check_winner(self):
        for player in self.players:
            if player.all_finished():
                return player
        return None

    def start(self):
        while True:
            player = self.players[self.current_player]
            self.play_turn(player)

            winner = self.check_winner()
            if winner:
                print(f"Vyhrál hráč: {winner.name}")
                break

            self.current_player = (self.current_player + 1) % len(self.players)


# ===== SPUŠTĚNÍ HRY =====
if __name__ == "__main__":
    print("Člověče, nezlob se - textová verze")

    num_players = int(input("Počet hráčů (2-4): "))
    players = []

    for i in range(num_players):
        name = input(f"Jméno hráče {i+1}: ")
        players.append(Player(name, i))

    game = Game(players)
    game.start()
