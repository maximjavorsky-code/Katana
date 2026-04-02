import random

# =========================
# DEFINICE KARET
# =========================

colors = ["Red", "Green", "Blue", "Yellow"]
values = list(range(0, 10)) + ["Skip", "+2"]

def create_deck():
    """Vytvoří balíček UNO karet"""
    deck = []
    for color in colors:
        for value in values:
            deck.append((color, value))
    random.shuffle(deck)
    return deck

# =========================
# FUNKCE PRO HRU
# =========================

def draw_card(deck):
    """Lízne kartu z balíčku"""
    return deck.pop() if deck else None

def is_valid(card, top_card):
    """Kontrola, zda lze kartu zahrát"""
    return card[0] == top_card[0] or card[1] == top_card[1]

def print_hand(hand):
    """Vypíše karty hráče"""
    for i, card in enumerate(hand):
        print(f"{i}: {card[0]} {card[1]}")

# =========================
# HLAVNÍ HERNÍ SMYČKA
# =========================

def play_game():
    deck = create_deck()

    player_hand = [draw_card(deck) for _ in range(5)]
    ai_hand = [draw_card(deck) for _ in range(5)]

    top_card = draw_card(deck)

    print("Startovní karta:", top_card)

    while True:
        # ===== HRÁČ =====
        print("\nTvoje karty:")
        print_hand(player_hand)
        print("Horní karta:", top_card)

        move = input("Vyber index karty nebo 'd' pro líznutí: ")

        if move == "d":
            card = draw_card(deck)
            if card:
                player_hand.append(card)
                print("Líznul jsi:", card)
            continue

        try:
            move = int(move)
            chosen = player_hand[move]
        except:
            print("Neplatný vstup")
            continue

        if is_valid(chosen, top_card):
            top_card = chosen
            player_hand.remove(chosen)
        else:
            print("Tuto kartu nelze zahrát!")
            continue

        if len(player_hand) == 0:
            print("Vyhrál jsi!")
            break

        # ===== AI =====
        print("\nTah počítače...")

        valid_cards = [card for card in ai_hand if is_valid(card, top_card)]

        if valid_cards:
            chosen = random.choice(valid_cards)
            ai_hand.remove(chosen)
            top_card = chosen
            print("Počítač zahrál:", chosen)
        else:
            card = draw_card(deck)
            if card:
                ai_hand.append(card)
                print("Počítač lízne kartu")

        if len(ai_hand) == 0:
            print("Počítač vyhrál!")
            break


# =========================
# SPUŠTĚNÍ PROGRAMU
# =========================

if __name__ == "__main__":
    play_game()