# GUI Kalkulačka

## Popis a cíl projektu

Cílem projektu je vytvořit jednoduchou kalkulačku s grafickým uživatelským rozhraním.
Uživatel bude moci provádět základní matematické operace pomocí tlačítek v okně aplikace.

Program je určen pro běžné uživatele, kteří potřebují provádět základní výpočty.

## Funkcionalita programu

Program obsahuje:

* grafické okno aplikace
* displej pro zobrazení čísla a výsledku
* tlačítka pro čísla 0–9
* tlačítka pro matematické operace (+ − × ÷)
* tlačítko pro výpočet výsledku
* tlačítko pro vymazání displeje

Uživatel klikáním na tlačítka vytváří matematický výraz, který se po stisknutí "=" vypočítá.

## Technická část

Program je napsán v jazyce Python.

Použité technologie:

* knihovna Tkinter pro grafické rozhraní
* widgety Button a Entry
* funkce pro práci s tlačítky
* metoda eval() pro výpočet matematického výrazu

Algoritmus programu:

1. Program vytvoří grafické okno.
2. Vytvoří displej pro zobrazení výpočtu.
3. Přidá tlačítka pro čísla a operace.
4. Po stisknutí tlačítka se hodnota zapíše do displeje.
5. Po stisknutí "=" se výraz vypočítá a zobrazí výsledek.
6. Program běží, dokud uživatel okno nezavře.
