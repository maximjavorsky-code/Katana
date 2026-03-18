"""
BLACKJACK (Poker 21) - Kompletní hra v jednom souboru
Interaktivní karetní hra, kde hráč hraje proti počítači (dealerovi).

Pravidla:
- Cíl: Dosáhnout hodnoty 21 nebo se jí co nejvíce přiblížit
- Figury (J, Q, K) = 10 bodů
- Eso (A) = 1 nebo 11 bodů (automatický výpočet)
- Dealer musí brát karty dokud nemá 17 nebo víc
- Překročení 21 = prohra
"""

import os
import random


class Card:
    """Reprezentuje jednu hrací kartu."""
    
    # Definice barev karet
    SUITS = ['♠', '♥', '♦', '♣']  # Piky, Srdce, Kára, Trefy
    
    # Definice hodnot karet
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    def __init__(self, suit, rank):
        """
        Inicializace karty.
        
        Args:
            suit (str): Barva karty (♠, ♥, ♦, ♣)
            rank (str): Hodnota karty (2-10, J, Q, K, A)
        """
        self.suit = suit
        self.rank = rank
    
    def get_value(self):
        """
        Vrací hodnotu karty pro hru.
        
        Returns:
            int: Hodnota karty (2-10, figury=10, Eso=11)
        """
        # Figury (J, Q, K) mají hodnotu 10
        if self.rank in ['J', 'Q', 'K']:
            return 10
        # Eso má aktuálně hodnotu 11 (bude se přepočítávat)
        elif self.rank == 'A':
            return 11
        # Číslické karty mají hodnotu podle sebe
        else:
            return int(self.rank)
    
    def __str__(self):
        """Vrací reprezentaci karty ve formátu 'rank♠' apod."""
        return f"{self.rank}{self.suit}"


class Deck:
    """Reprezentuje balíček 52 hracích karet."""
    
    def __init__(self):
        """Inicializace balíčku - vytvoří 52 karet a zamíchá je."""
        self.cards = []
        self._create_deck()
        self.shuffle()
    
    def _create_deck(self):
        """
        Vytvoří standardní balíček 52 karet.
        Pro každou barvu a hodnotu vytvoří kartu.
        """
        # Vnější smyčka: iteruje přes barvy
        for suit in Card.SUITS:
            # Vnitřní smyčka: iteruje přes hodnoty
            for rank in Card.RANKS:
                card = Card(suit, rank)
                self.cards.append(card)
    
    def shuffle(self):
        """Zamíchá karty v balíčku."""
        random.shuffle(self.cards)
    
    def draw_card(self):
        """
        Vybere a vrací kartu z balíčku.
        Pokud balíček skončí, vytvoří nový.
        
        Returns:
            Card: Následující karta z balíčku
        """
        if len(self.cards) == 0:
            # Pokud nám dojdou karty, vytvoříme nový balíček
            self._create_deck()
            self.shuffle()
        
        return self.cards.pop()
    
    def remaining_cards(self):
        """Vrací počet zbývajících karet v balíčku."""
        return len(self.cards)


class Player:
    """Reprezentuje hráče nebo dealera v hře."""
    
    def __init__(self, name, money=100):
        """
        Inicializace hráče.
        
        Args:
            name (str): Jméno hráče
            money (int): Počáteční peníze hráče
        """
        self.name = name
        self.hand = []  # Seznam karet v ruce
        self.money = money  # Dostupné peníze
        self.bet = 0  # Aktuální sázka
    
    def add_card(self, card):
        """
        Přidá kartu do ruky hráče.
        
        Args:
            card (Card): Karta k přidání
        """
        self.hand.append(card)
    
    def get_hand_value(self):
        """
        Vypočítá hodnotu kombinace karet.
        Automaticky přepočítá Esa (A) z 11 na 1 pokud je potřeba.
        
        Příklad: Pokud má hráč A + 5, hodnota je 16 (11 + 5)
                 Pokud má hráč A + K, hodnota je 21 (1 + 10, protože 11 + 10 > 21)
        
        Returns:
            int: Celková hodnota ruky
        """
        value = 0
        aces = 0
        
        # Sečte hodnoty všech karet a počítá Esa
        for card in self.hand:
            value += card.get_value()
            if card.rank == 'A':
                aces += 1
        
        # Pokud je hodnota > 21 a máme Esa, přepočítáme je na 1
        # Eso bylo počítáno jako 11, takže odečteme 10 (11 - 1 = 10)
        while value > 21 and aces > 0:
            value -= 10  # Eso se změní z 11 na 1
            aces -= 1
        
        return value
    
    def clear_hand(self):
        """Vyprázdní ruku hráče (příprava na nové kolo)."""
        self.hand = []
    
    def place_bet(self, amount):
        """
        Hráč vsadí peníze.
        
        Args:
            amount (int): Částka sázky
            
        Returns:
            bool: True pokud byla sázka přijata, False pokud nemá dost peněz
        """
        if amount <= self.money:
            self.bet = amount
            self.money -= amount
            return True
        return False
    
    def win_bet(self, multiplier=2):
        """
        Hráč vyhrál - přidá si výhru do peněz.
        
        Args:
            multiplier (float): Násobitel (2 = normální výhra, 2.5 = blackjack)
        """
        self.money += int(self.bet * multiplier)
    
    def display_hand(self):
        """Vrací textový výpis karet v ruce."""
        cards_str = ', '.join(str(card) for card in self.hand)
        return f"{cards_str} (Hodnota: {self.get_hand_value()})"
    
    def __str__(self):
        """Vrací informaci o hráči a jeho ruce."""
        return f"{self.name}: {self.display_hand()}"


class Game:
    """Hra Blackjack - správa průběhu a pravidel."""
    
    def __init__(self):
        """Inicializace hry."""
        self.deck = Deck()
        self.player = Player("Hráč", money=100)
        self.dealer = Player("Dealer", money=1000)
    
    def clear_screen(self):
        """Vyčistí terminál."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_game_state(self, show_dealer_full=False):
        """
        Zobrazí aktuální stav hry.
        
        Args:
            show_dealer_full (bool): Má se zobrazit úplná ruka dealera?
                                    False = zobrazí jen první kartu (z důvodu napětí)
        """
        print("\n" + "="*50)
        print(f"💰 Peníze hráče: {self.player.money + self.player.bet}")
        print("="*50)
        
        # Zobrazení ruky dealera
        if show_dealer_full:
            # Konec hry - ukáže všechny karty dealera
            print(f"🃏 {self.dealer.display_hand()}")
        else:
            # Během hry - ukáže jen první kartu
            if len(self.dealer.hand) > 0:
                print(f"🃏 Dealer: {self.dealer.hand[0]} + ? (hodnota: ?)")
        
        print("-"*50)
        
        # Zobrazení ruky hráče
        print(f"👤 {self.player.display_hand()}")
        print("="*50)
    
    def initial_deal(self):
        """
        Rozdá počáteční 2 karty hráči a dealerovi.
        Toto je standardní Blackjack pravidlo.
        """
        # Hráč dostane 2 karty
        self.player.add_card(self.deck.draw_card())
        self.player.add_card(self.deck.draw_card())
        
        # Dealer dostane 2 karty
        self.dealer.add_card(self.deck.draw_card())
        self.dealer.add_card(self.deck.draw_card())
    
    def check_blackjack(self):
        """
        Zkontroluje, zda má někdo Blackjack (21 na 2 kartách).
        Blackjack je speciální případ - nejsilnější kombinace.
        
        Returns:
            str: 'player', 'dealer', 'both' nebo None
        """
        # Podmínka pro blackjack: přesně 2 karty A hodnota = 21
        player_blackjack = (len(self.player.hand) == 2 and 
                           self.player.get_hand_value() == 21)
        dealer_blackjack = (len(self.dealer.hand) == 2 and 
                           self.dealer.get_hand_value() == 21)
        
        if player_blackjack and dealer_blackjack:
            return 'both'
        elif player_blackjack:
            return 'player'
        elif dealer_blackjack:
            return 'dealer'
        
        return None
    
    def player_turn(self):
        """
        Hra hráče. Hráč si může vzít další kartu (Hit) nebo skončit (Stand).
        
        Returns:
            bool: True pokud hráč pokračuje, False pokud prohraje nebo chce skončit
        """
        while True:
            self.display_game_state()
            
            # Pokud hráč již překročil 21, automaticky prohraje
            if self.player.get_hand_value() > 21:
                print("\n❌ Překročili jste 21! Prohráli jste.")
                return False
            
            # Hráč volí akci
            action = input("\n(H)it, (S)tand, (Q)uit? ").upper()
            
            if action == 'H':
                # Hráč vezme další kartu
                card = self.deck.draw_card()
                self.player.add_card(card)
                print(f"\n✅ Dostali jste: {card}")
            
            elif action == 'S':
                # Hráč končí svůj tah
                print(f"\n✋ Stojíte s hodnotou: {self.player.get_hand_value()}")
                return True
            
            elif action == 'Q':
                # Hráč chce skončit hru
                print("\n👋 Hra ukončena.")
                return False
            
            else:
                print("❌ Neplatná volba!")
    
    def dealer_turn(self):
        """
        Dealer hraje podle standardních pravidel Blackjacku.
        Dealer musí brát karty dokud nemá hodnotu >= 17.
        
        Toto je deterministické chování - dealer nemá volbu, pouze následuje pravidla.
        """
        print("\n🤖 Dealer hraje...\n")
        
        # Dealer musí brát karty dokud nemá 17 nebo víc
        while self.dealer.get_hand_value() < 17:
            card = self.deck.draw_card()
            self.dealer.add_card(card)
            print(f"Dealer vzal: {card} (Hodnota: {self.dealer.get_hand_value()})")
        
        if self.dealer.get_hand_value() > 21:
            print(f"\n❌ Dealer překročil 21! (Hodnota: {self.dealer.get_hand_value()})")
        else:
            print(f"\n✋ Dealer stojí s hodnotou: {self.dealer.get_hand_value()}")
    
    def determine_winner(self):
        """
        Určí vítěze kola na základě hodnot obou hráčů.
        
        Logika:
        1. Pokud hráč překročil 21 -> dealer vítězí
        2. Pokud dealer překročil 21 -> hráč vítězí
        3. Pokud oba mají <= 21 -> ten s vyšší hodnotou vítězí
        4. Pokud mají stejnou hodnotu -> remíza
        
        Returns:
            str: 'player', 'dealer' nebo 'push' (remíza)
        """
        player_value = self.player.get_hand_value()
        dealer_value = self.dealer.get_hand_value()
        
        # Hráč překročil 21
        if player_value > 21:
            return 'dealer'
        
        # Dealer překročil 21
        if dealer_value > 21:
            return 'player'
        
        # Oba mají <= 21, porovnáme hodnoty
        if player_value > dealer_value:
            return 'player'
        elif dealer_value > player_value:
            return 'dealer'
        else:
            return 'push'
    
    def play_round(self):
        """
        Odeehraje jedno kolo Blackjacku.
        Zahrnuje: sázku, rozdání karet, hru hráče, hru dealera a určení vítěze.
        """
        print("\n" + "="*50)
        print("🎴 BLACKJACK - NOVÉ KOLO")
        print("="*50)
        
        # Hráč se vsadí - musí zadat validní částku
        while True:
            try:
                bet = int(input(f"\n💰 Vaše peníze: {self.player.money}\n"
                              f"Kolik chcete vsadit? "))
                if self.player.place_bet(bet):
                    break
                else:
                    print("❌ Nemáte dost peněz!")
            except ValueError:
                print("❌ Zadejte číslo!")
        
        # Počáteční rozdání karet
        self.initial_deal()
        
        # Kontrola Blackjacku na začátku
        blackjack = self.check_blackjack()
        
        if blackjack == 'both':
            # Oba mají Blackjack = remíza
            self.display_game_state(show_dealer_full=True)
            print("\n🤝 Oba máte Blackjack! Remíza!")
            self.player.win_bet(2)  # Peníze se vrátí
        
        elif blackjack == 'player':
            # Hráč má Blackjack = automatická výhra
            self.display_game_state(show_dealer_full=True)
            print("\n🎉 BLACKJACK! Vyhráli jste 1.5x vaší sázky!")
            self.player.win_bet(2.5)  # 1.5x výhra
        
        elif blackjack == 'dealer':
            # Dealer má Blackjack = hráč prohraje
            self.display_game_state(show_dealer_full=True)
            print("\n😔 Dealer má Blackjack. Prohráli jste.")
        
        else:
            # Standardní průběh hry
            if not self.player_turn():
                # Hráč chce skončit nebo již překročil 21
                return
            
            # Nyní hraje dealer
            self.dealer_turn()
            
            # Určení vítěze
            self.display_game_state(show_dealer_full=True)
            winner = self.determine_winner()
            
            if winner == 'player':
                print("\n🎉 Vyhráli jste! Získáváte 2x vaší sázky!")
                self.player.win_bet(2)
            
            elif winner == 'dealer':
                print("\n😔 Dealer vyhrál.")
            
            else:
                print("\n🤝 Remíza! Peníze se vracejí.")
                self.player.win_bet(2)
        
        # Příprava na další kolo
        self.player.clear_hand()
        self.dealer.clear_hand()
    
    def run(self):
        """
        Hlavní smyčka hry.
        Odeehrávájící jednotlivá kola dokud hráč nemá peníze nebo nechce pokračovat.
        """
        self.clear_screen()
        print("🎴 Vítejte v BLACKJACKU (Poker 21) 🎴")
        print("="*50)
        print("Cíl: Dosáhnout hodnoty 21 nebo se jí přiblížit")
        print("bez překročení, a porazit dealera!")
        print("="*50)
        
        # Hlavní herní smyčka
        while self.player.money > 0:
            self.play_round()
            
            # Kontrola, zda má ještě peníze
            if self.player.money <= 0:
                print("\n💔 Nemáte již žádné peníze. Hra skončila.")
                break
            
            # Zeptáme se, zda chce pokračovat
            again = input("\nChcete hrát další kolo? (A)no/(N)e? ").upper()
            
            if again != 'A':
                print(f"\n👋 Děkujeme za hru! Odcházíte s {self.player.money} peníze.")
                break
            
            self.clear_screen()
        
        print("\n🎮 Konec hry.")


def main():
    """Hlavní funkce - spustí hru."""
    game = Game()
    game.run()


if __name__ == "__main__":
    # Kontrola, aby se kód spustil pouze když se soubor spustí přímo
    main()