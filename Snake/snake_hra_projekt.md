# Snake hra

## Popis a cíl projektu
Cílem projektu je vytvořit jednoduchou arkádovou hru Had (Snake).
Hráč ovládá hada pomocí klávesnice a snaží se sbírat jídlo.
Hra končí při nárazu do stěny nebo do vlastního těla.

## Funkcionalita programu
- Pohyb hada v mřížce
- Ovládání pomocí šipek
- Generování jídla na náhodné pozici
- Růst hada po sežrání jídla
- Detekce kolizí (stěna, vlastní tělo)

## Technická část
- Program je napsán v jazyce Python
- Použitá knihovna: pygame
- Herní smyčka zajišťuje běh aplikace
- Had je reprezentován jako seznam souřadnic
- Pohyb je realizován změnou pozice hlavy a posunem těla
- Kolize je kontrolována pomocí podmínek