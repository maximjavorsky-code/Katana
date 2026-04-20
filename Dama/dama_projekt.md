# Dáma - konzolová hra

## Popis a cíl projektu
Projekt představuje jednoduchou konzolovou implementaci klasické deskové hry Dáma.

Cílem aplikace je umožnit dvěma hráčům hrát proti sobě na jednom zařízení v textovém rozhraní.
Hra slouží pro procvičení logiky, práce s poli a algoritmického myšlení.

---

## Funkcionalita programu
- vytvoření hrací desky 8x8
- střídání dvou hráčů (bílý a černý)
- pohyb kamenů po diagonále
- možnost skoku přes soupeřův kámen (brání)
- jednoduchá kontrola vítězství
- textové zobrazení herní desky v konzoli

---

## Technická část

### Použité technologie
- Python 3
- standardní knihovny (bez externích balíčků)

### Datové struktury
- 2D seznam (list of lists) pro hrací desku
- string hodnoty pro kameny:
  - "w" / "W" = bílý kámen / dáma
  - "b" / "B" = černý kámen / dáma

### Algoritmy
- validace tahu pomocí rozdílů souřadnic (dx, dy)
- kontrola braní přes střední pole
- kontrola výhry spočítáním zbývajících kamenů

### Logika hry
- střídání hráčů v hlavní smyčce
- kontrola vstupu uživatele
- validace pohybů
- aktualizace herní desky