# Space Invaders

## Popis a cíl projektu
Cílem projektu je vytvořit jednoduchou arkádovou hru Space Invaders v jazyce Python.
Hráč ovládá loď a snaží se sestřelit padající nepřátele.

Projekt je určen pro začátečníky jako ukázka práce s knihovnou Pygame.

## Funkcionalita programu
- pohyb hráče doleva a doprava
- střelba projektilů
- generování nepřátel
- pohyb nepřátel směrem dolů
- detekce kolizí mezi střelou a nepřítelem

## Technická část

### Použité knihovny
- pygame – vykreslování grafiky a zpracování vstupu

### Algoritmy
- detekce kolize pomocí porovnání vzdáleností objektů
- herní smyčka (game loop)

### Datové struktury
- seznam nepřátel (list)
- seznam střel (list)

### Struktura programu
- main.py obsahuje hlavní herní logiku
- funkce pro pohyb, kolize a generování objektů
