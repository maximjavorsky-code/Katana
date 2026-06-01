import subprocess
from git import Repo
from datetime import datetime

repo = Repo(".")

# 1. zjisti změny
diff = repo.git.diff("--staged")

if not diff:
    print("Žádné změny k commitnutí")
    exit()

# 2. auto-staging (pro jistotu)
repo.git.add(A=True)
staged_diff = repo.git.diff("--staged").lower()

# 3. kontrola kvality commit message
BAD_WORDS = ["update", "stuff", "changes", "misc", "project"]

def is_bad_commit(text):
    return any(word in text.lower() for word in BAD_WORDS)

# 4. analýza změn
def analyze(diff_text):
    commits = []

    if "readme" in diff_text or "_projekt" in diff_text:
        commits.append("Doplněna nebo upravena dokumentace projektu")

    if "def " in diff_text:
        commits.append("Přidána nebo upravena funkcionalita")

    if "class" in diff_text:
        commits.append("Upravena struktura objektů")

    if "fix" in diff_text or "bug" in diff_text:
        commits.append("Opravena chyba v kódu")

    if not commits:
        commits.append("Upraven kód projektu")

    # filtr špatných commitů
    commits = [c for c in commits if not is_bad_commit(c)]

    return commits


commits = analyze(staged_diff)

print("\nNAVRŽENÉ COMMITY:")
for i, c in enumerate(commits, 1):
    print(f"{i}. {c}")

# 5. školní kontrola
print("\nKONTROLA PRAVIDEL:")

print("- min. 3 commity týdně (kontroluj přes git log)")
print("- rozestup 12 hodin mezi commity (manuální kontrola)")
print("- commit musí být konkrétní")

# 6. potvrzení
confirm = input("\nNapiš YES pro commit + push: ")

if confirm != "YES":
    print("Zrušeno")
    exit()

# 7. commit + push
for msg in commits:
    repo.git.add(A=True)
    repo.index.commit(msg)

repo.remote().push()

print("\nHotovo: commity vytvořeny a pushnuty")