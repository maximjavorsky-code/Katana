import random

# =========================
# VYTVOŘENÍ BALÍČKU KARET
# =========================
def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
              'J', 'Q', 'K', 'A']
    deck = [(value, suit) for value in values for suit in suits]
    return deck


# =========================
# MÍCHÁNÍ BALÍČKU
# =========================
def shuffle_deck(deck):
    random.shuffle(deck)


# =========================
# ROZDÁNÍ KARET
# =========================
def deal_cards(deck, num=2):
    hand = []
    for _ in range(num):
        hand.append(deck.pop())
    return hand


# =========================
# ZOBRAZENÍ KARET
# =========================
def show_hand(hand):
    return ", ".join([f"{value} of {suit}" for value, suit in hand])


# =========================
# VYHODNOCENÍ KARET (ZJEDNODUŠENÉ)
# =========================
def evaluate_hand(hand):
    """
    Vrací skóre kombinace.
    Čím vyšší číslo, tím lepší kombinace.
    (Zjednodušené – neobsahuje všechny poker kombinace)
    """
    values = [card[0] for card in hand]

    # převod hodnot na čísla
    order = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
             '7': 7, '8': 8, '9': 9, '10': 10,
             'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    numeric_values = sorted([order[v] for v in values])

    # kontrola dvojice
    if len(set(values)) < len(values):
        return 2  # pár

    # vysoká karta
    return 1


# =========================
# HLAVNÍ HRA
# =========================
def play_poker():
    deck = create_deck()
    shuffle_deck(deck)

    # hráč a AI
    player_hand = deal_cards(deck)
    ai_hand = deal_cards(deck)

    # společné karty
    table_cards = deal_cards(deck, 5)

    print("\n=== POKER ===")
    print("Tvoje karty:", show_hand(player_hand))
    print("Karty na stole:", show_hand(table_cards))

    input("\nStiskni ENTER pro odhalení soupeře...")

    print("\nSoupeř má:", show_hand(ai_hand))

    # kombinace
    player_score = evaluate_hand(player_hand + table_cards)
    ai_score = evaluate_hand(ai_hand + table_cards)

    print("\n=== VÝSLEDEK ===")
    if player_score > ai_score:
        print("Vyhrál jsi!")
    elif player_score < ai_score:
        print("Prohrál jsi.")
    else:
        print("Remíza.")


# =========================
# SPUŠTĚNÍ PROGRAMU
# =========================
if __name__ == "__main__":
    play_poker()