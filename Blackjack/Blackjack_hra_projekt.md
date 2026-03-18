# Blackjack Hra

## Popis a cíl projektu

Projekt implementuje klasickou karetní hru **Blackjack (Poker 21)** v Pythonu. Hráč se snaží porazit dealera (počítač) tím, že dosáhne hodnoty 21 nebo ji překoná pouze částečně, aniž by ji překročil. Aplikace je určena pro jednoho hráče, který hraje proti počítači.

## Funkcionalita programu

Program se skládá z následujících technických prvků:

### Základní komponenty:
1. **Balíček karet (Deck)** - 52 standardních hracích karet
2. **Hráč a Dealer** - objekty pro sledování jejich stavu
3. **Herní logika** - pravidla Blackjacku
4. **Uživatelské rozhraní** - textové komunikace s hráčem

### Klíčové algoritmy:
- Výpočet hodnoty kombinace karet
- Logika dealera (dealer musí brát karty dokud nemá hodnotu ≥ 17)
- Určení vítěze (porovnání hodnot)
- Správa sázky a peněz hráče

### Datové struktury:
- Třída `Card` pro reprezentaci karty
- Třída `Deck` pro balíček karet
- Třída `Player` pro hráče/dealera
- Třída `Game` pro herní logiku

## Technické detaily

**Použité knihovny:** 
- `random` - pro shuffle balíčku
- `os` - pro čištění obrazovky

**Pravidla Blackjacku:**
- Cílová hodnota: 21
- Všechny figury (J, Q, K) = 10 bodů
- Eso (A) = 1 nebo 11 bodů (automatický výpočet)
- Dealer musí pokračovat až do hodnoty ≥ 17
- Hráč se snaží porazit dealera bez překročení 21