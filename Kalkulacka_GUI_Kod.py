# Import knihovny Tkinter pro vytvoření grafického rozhraní
import tkinter as tk

# Vytvoření hlavního okna aplikace
okno = tk.Tk()
okno.title("Kalkulačka")
okno.geometry("300x400")

# Proměnná pro ukládání matematického výrazu
vyraz = ""

# Funkce pro přidání čísla nebo operace do displeje
def stisk(symbol):
    global vyraz
    vyraz = vyraz + str(symbol)
    displej_var.set(vyraz)

# Funkce pro výpočet výsledku
def vypocet():
    global vyraz
    try:
        vysledek = str(eval(vyraz))
        displej_var.set(vysledek)
        vyraz = vysledek
    except:
        displej_var.set("Chyba")
        vyraz = ""

# Funkce pro vymazání displeje
def vymazat():
    global vyraz
    vyraz = ""
    displej_var.set("")

# Proměnná pro text displeje
displej_var = tk.StringVar()

# Displej kalkulačky
displej = tk.Entry(okno, textvariable=displej_var, font=("Arial", 20), justify="right")
displej.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Rám pro tlačítka
tlacitka = tk.Frame(okno)
tlacitka.pack()

# Funkce pro vytvoření tlačítka
def vytvor_tlacitko(text, radek, sloupec):
    tl = tk.Button(
        tlacitka,
        text=text,
        width=5,
        height=2,
        font=("Arial", 14),
        command=lambda: stisk(text)
    )
    tl.grid(row=radek, column=sloupec, padx=5, pady=5)

# Čísla
vytvor_tlacitko("7",0,0)
vytvor_tlacitko("8",0,1)
vytvor_tlacitko("9",0,2)

vytvor_tlacitko("4",1,0)
vytvor_tlacitko("5",1,1)
vytvor_tlacitko("6",1,2)

vytvor_tlacitko("1",2,0)
vytvor_tlacitko("2",2,1)
vytvor_tlacitko("3",2,2)

vytvor_tlacitko("0",3,1)

# Operace
vytvor_tlacitko("+",0,3)
vytvor_tlacitko("-",1,3)
vytvor_tlacitko("*",2,3)
vytvor_tlacitko("/",3,3)

# Speciální tlačítka
tk.Button(tlacitka, text="=", width=5, height=2, font=("Arial",14), command=vypocet).grid(row=3,column=2)
tk.Button(tlacitka, text="C", width=5, height=2, font=("Arial",14), command=vymazat).grid(row=3,column=0)

# Spuštění programu
okno.mainloop()