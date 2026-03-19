# 🎲 Projekt: Hra Kostky

## 📌 Popis
Tento program simuluje jednoduchou hru „Kostky“ pro dva hráče.  
Hráči se střídají v tazích a snaží se získat co nejvíce bodů hodem kostkou.

## 🎮 Pravidla hry
- Každý hráč hází kostkou (1–6)
- Může se rozhodnout:
  - pokračovat v házení
  - nebo ukončit tah a přičíst body
- Pokud padne **1**, hráč ztrácí všechny body za dané kolo
- Vyhrává hráč, který jako první dosáhne **50 bodů**

## 🧠 Funkce programu

### `hod_kostkou()`
Vrací náhodné číslo od 1 do 6.

### `tah_hrace(jmeno)`
- Řídí tah hráče
- Umožňuje opakované házení
- Vrací počet bodů za kolo

### `main()`
- Hlavní logika hry
- Řídí střídání hráčů
- Kontroluje výhru

## ▶️ Spuštění programu
Program se spouští příkazem:

```bash
python Kostky_hra.py