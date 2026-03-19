import random

# Funkce pro hod kostkou
def hod_kostkou():
    return random.randint(1, 6)

# Funkce pro tah hráče
def tah_hrace(jmeno):
    body = 0

    while True:
        print(f"\n{jmeno}, chceš házet? (a/n)")
        volba = input("> ")

        if volba.lower() != "a":
            break

        hod = hod_kostkou()
        print(f"Hodil jsi: {hod}")

        if hod == 1:
            print("Padla 1! Ztrácíš body za toto kolo.")
            return 0

        body += hod
        print(f"Aktuální body v kole: {body}")

    return body


# Hlavní část programu
def main():
    print("🎲 Vítej ve hře Kostky!")

    hrac1 = input("Zadej jméno hráče 1: ")
    hrac2 = input("Zadej jméno hráče 2: ")

    skore1 = 0
    skore2 = 0

    while skore1 < 50 and skore2 < 50:
        print("\n--- Nové kolo ---")

        skore1 += tah_hrace(hrac1)
        print(f"{hrac1} má celkem: {skore1}")

        if skore1 >= 50:
            break

        skore2 += tah_hrace(hrac2)
        print(f"{hrac2} má celkem: {skore2}")

    print("\n--- Konec hry ---")
    if skore1 >= 50:
        print(f"Vyhrál {hrac1}!")
    else:
        print(f"Vyhrál {hrac2}!")


# Spuštění programu
if __name__ == "__main__":
    main()