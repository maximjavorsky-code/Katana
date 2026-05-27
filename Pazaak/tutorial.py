import pygame
import os

pygame.init()

# Nastavení okna (ponecháno 800x600, ale přizpůsobeno stylu)
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pazaak Tutorial - KOTOR Edition")

clock = pygame.time.Clock()

# --- STYLY PÍSMA (Shodné s pazaak.py) ---
FONT = pygame.font.SysFont(["garamond", "georgia", "timesnewroman", "serif"], 22, bold=True)
BIG = pygame.font.SysFont(["garamond", "georgia", "timesnewroman", "serif"], 48, bold=True)

# --- PALETA BAREV (Shodné s pazaak.py) ---
BG_COLOR = (25, 20, 18)
GLOW_AMBER = (212, 143, 56)      
TEXT_IVORY = (235, 225, 200)      
TEXT_GOLD = (230, 180, 90)        

# --- NAČTENÍ POZADÍ (Volitelné - pokud máš assets) ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
asset_path = os.path.join(BASE_DIR, "assets", "tutorial.png")
if os.path.exists(asset_path):
    bg = pygame.image.load(asset_path)
    bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
else:
    # Pokud pozadí neexistuje, vytvoří se tmavé herní plátno
    bg = pygame.Surface((WIDTH, HEIGHT))
    bg.fill(BG_COLOR)


# ----------------------------
# ✨ GLOW EFFECT (Světelná záře pod textem)
# ----------------------------
def text_glow(text_surface, x, y, color):
    # Vytvoří jemné rozmazané pozadí za textem pro KOTOR atmosféru
    glow_surf = pygame.Surface((text_surface.get_width() + 20, text_surface.get_height() + 20), pygame.SRCALPHA)
    pygame.draw.rect(glow_surf, (*color, 25), glow_surf.get_rect(), border_radius=8)
    screen.blit(glow_surf, (x - 10, y - 10))


# ----------------------------
# 🎨 DRAW FUNCTION
# ----------------------------
def draw():
    # Vykreslení pozadí
    screen.blit(bg, (0, 0))

    # --- NADPIS ---
    title = BIG.render("RULES", True, TEXT_GOLD)
    title_x = WIDTH // 3 - title.get_width() // 1
    title_y = 80
    text_glow(title, title_x, title_y, GLOW_AMBER)
    screen.blit(title, (title_x, title_y))

    # --- TEXTY PRAVIDEL ---
    text_lines = [
        "Cíl: dostat se co nejblíž k 20 bez překročení.",
        "Každé kolo taháš kartu 1-10.",
        "Můžeš použít side karty (+/- hodnoty).",
        "Side kartu můžeš použít max 4x.",
        "Když překročíš 20 = prohra.",
        "AI hraje automaticky."
    ]

    start_y = 200
    for line in text_lines:
        render = FONT.render(line, True, TEXT_IVORY)
        line_x = 90
        text_glow(render, line_x, start_y, GLOW_AMBER)
        screen.blit(render, (line_x, start_y))
        start_y += 45

    # --- SPODNÍ NÁPOVĚDA ---
    hint = FONT.render("Zavři okno pro návrat do lobby", True, GLOW_AMBER)
    hint_x = WIDTH // 2 - hint.get_width() // 2
    hint_y = 475
    screen.blit(hint, (hint_x, hint_y))


# ----------------------------
# 🎮 LOOP
# ----------------------------
running = True
while running:
    clock.tick(60)
    
    draw()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()