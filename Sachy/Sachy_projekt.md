# Zjednodušené šachy

## Popis a cíl projektu
Cílem projektu je vytvořit jednoduchou verzi hry šachy pro dva hráče.
Hra bude mít grafické rozhraní a umožní hráčům hrát proti sobě na jednom počítači.

## Funkcionalita programu
- vykreslení šachovnice
- zobrazení figur
- klikání myší pro tahy
- kontrola základních pravidel pohybu
- střídání hráčů
- ukončení hry při sebrání krále

## Technická část
Program je napsán v jazyce Python s využitím knihovny Tkinter pro GUI.
Logika hry je rozdělena do několika souborů:
- main.py – spuštění aplikace
- board.py – vykreslení šachovnice
- pieces.py – definice figur a jejich pohybu
- game.py – hlavní herní logika

Použité principy:
- objektově orientované programování
- práce s 2D polem (šachovnice)
- event handling (kliknutí myší)