# Pazaak

## Popis a cíl projektu

Projekt Pazaak je karetní hra inspirovaná minihrou ze série Star Wars: Knights of the Old Republic (KOTOR).

Cílem projektu je vytvořit funkční desktopovou aplikaci v jazyce Python s grafickým rozhraním pomocí knihovny Pygame. Hráč soutěží proti počítači a snaží se dosáhnout co nejbližší hodnoty 20 bez jejího překročení.

Aplikace je určena pro fanoušky karetních her a světa Star Wars a zároveň slouží jako praktická ukázka tvorby herních aplikací v Pythonu.

---

## Funkcionalita programu

Program obsahuje několik samostatných částí:

### Hlavní menu (Lobby)

* spuštění hry
* zobrazení tutoriálu
* ukončení aplikace

### Herní režim

* dobírání karet (DRAW)
* použití vedlejších karet (SIDE)
* ukončení tahu (STAND)
* restart hry (RESET)
* opakované spuštění po skončení partie (PLAY AGAIN)

### Grafické rozhraní

* vlastní vykreslování karet
* animované zvýraznění aktivních prvků
* pozadí inspirované hrou KOTOR
* futuristické uživatelské rozhraní

### Tutorial

* vysvětlení pravidel hry
* popis ovládání
* vysvětlení systému vedlejších karet

---

## Technická část

### Použité knihovny

* pygame
* random
* subprocess
* sys

### Použité algoritmy

#### Generování karet

Hodnoty hlavních karet jsou generovány náhodně pomocí funkce:

```python
random.randint(1, 10)
```

#### Vedlejší karty

Vedlejší karty jsou vybírány z předdefinovaného seznamu:

```python
[-4, -3, -2, -1, 1, 2, 3, 4]
```

#### Vyhodnocení vítěze

Program průběžně kontroluje:

* překročení hodnoty 20
* rozdíl mezi hráčem a soupeřem
* remízu

### Datové struktury

Projekt využívá:

* seznamy (list) pro ukládání karet hráče
* třídu Card pro reprezentaci jednotlivých karet
* proměnné pro správu herního stavu

### Struktura projektu

```text
Pazaak/
│
├── assets/
│   └── lobby_bg.png
│
├── main.py
├── pazaak.py
├── tutorial.py
├── karty.py
└── Pazaak_projekt.md
```

### Budoucí rozšíření

* lokální multiplayer
* síťový multiplayer
* zvukové efekty
* hudební doprovod
* ukládání statistik
* pokročilejší umělá inteligence
* animace karet
* větší podobnost s originální hrou Pazaak z KOTOR
