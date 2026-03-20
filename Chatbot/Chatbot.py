import random

# Předdefinované odpovědi
odpovedi = {
    "ahoj": ["Ahoj!", "Čau!", "Zdravím!"],
    "jak se máš": ["Mám se dobře!", "Jde to 🙂", "Jsem jen program, ale fungují mi bity 😄"],
    "co děláš": ["Povídám si s tebou.", "Čekám na tvůj dotaz.", "Jsem tu pro tebe."],
    "konec": ["Ahoj, měj se!", "Ukončuji program.", "Tak zase někdy!"]
}

# Funkce pro získání odpovědi
def ziskej_odpoved(vstup):
    vstup = vstup.lower()

    for klic in odpovedi:
        if klic in vstup:
            return random.choice(odpovedi[klic])

    return "Tomu nerozumím, zkus to jinak."


# Hlavní funkce
def main():
    print("🤖 Chatbot spuštěn (napiš 'konec' pro ukončení)")

    while True:
        uzivatel = input("Ty: ")

        odpoved = ziskej_odpoved(uzivatel)
        print("Bot:", odpoved)

        if "konec" in uzivatel.lower():
            break


# Spuštění programu
if __name__ == "__main__":
    main()