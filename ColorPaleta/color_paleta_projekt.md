# Color Palette Engine

## Popis a cíl projektu

Projekt Color Palette Engine slouží jako generátor a vyhledávač barevných odstínů v jazyce Python.

Program umožňuje:
- generovat HEX kódy barev,
- vyhledávat odstíny podle názvu,
- zobrazovat světlejší a tmavší varianty barev,
- organizovat barvy do kategorií.

Projekt je určen pro:
- začínající programátory,
- grafiky,
- tvorbu UI designů,
- práci s barevnými paletami.

---

## Funkcionalita programu

Program obsahuje několik hlavních částí:

### Generování HEX barev
Každá barva je automaticky převedena na HEX kód pomocí hashovací funkce MD5.

### Převod barev
Program umí převádět:
- HEX → RGB
- RGB → HEX

### Úprava jasu barev
Program dokáže:
- zesvětlit barvu,
- ztmavit barvu.

### Databáze barev
Barvy jsou ukládány do textového seznamu a následně zpracovány do slovníku.

### Vyhledávání
Uživatel může:
- hledat konkrétní odstíny,
- hledat celé skupiny barev,
- filtrovat výsledky podle názvu.

---

# Technická dokumentace

## Použité knihovny

### hashlib
Knihovna slouží pro:
- generování MD5 hashů,
- tvorbu deterministických HEX barev.

---

## Datové struktury

Program využívá:

### Slovník (dictionary)
```python
palette = {}