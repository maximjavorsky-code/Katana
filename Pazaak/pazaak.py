import pygame
import random
import os

pygame.init()

WIDTH, HEIGHT = 900, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pazaak - KOTOR Edition")

clock = pygame.time.Clock()

# --- STYLY PÍSMA ---
FONT = pygame.font.SysFont(["garamond", "georgia", "timesnewroman", "serif"], 22, bold=True)
BIG = pygame.font.SysFont(["garamond", "georgia", "timesnewroman", "serif"], 58, bold=True)

TARGET = 20

# --- NOVÁ PALETA BAREV ---
BG = (25, 20, 18)
TABLE = (35, 28, 25)
GLOW_AMBER = (212, 143, 56)
TEXT_IVORY = (235, 225, 200)
TEXT_GOLD = (230, 180, 90)
TEXT_TERRACOTTA = (180, 70, 50)  # Barva pro AI (Terracotta)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Check if asset exists before trying to load it to prevent crash
asset_path = os.path.join(BASE_DIR, "assets", "pozadi.png")
if os.path.exists(asset_path):
    bg = pygame.image.load(asset_path)
    bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
else:
    # Fallback to solid background color if asset is missing
    bg = pygame.Surface((WIDTH, HEIGHT))
    bg.fill(BG)

# ----------------------------
# ✨ GLOW
# ----------------------------
def glow(rect, color):
    surf = pygame.Surface((rect.w+20, rect.h+20), pygame.SRCALPHA)
    pygame.draw.rect(surf, (*color, 35), surf.get_rect(), border_radius=12)
    screen.blit(surf, (rect.x-10, rect.y-10))


# ----------------------------
# 🎴 CARD
# ----------------------------
class Card:
    def __init__(self, value, x, y, positive=True):
        self.value = value
        self.rect = pygame.Rect(x, y, 70, 90)
        self.positive = positive

    def draw(self):
        # Hráčovy karty jsou AMBER, AI karty jsou nyní TERRACOTTA (shodné s jménem)
        color = GLOW_AMBER if self.positive else TEXT_TERRACOTTA
        glow(self.rect, color)
        pygame.draw.rect(screen, (20, 16, 14), self.rect, border_radius=10)
        pygame.draw.rect(screen, color, self.rect, 2, border_radius=10)

        text = BIG.render(str(self.value), True, TEXT_IVORY)
        screen.blit(text, text.get_rect(center=self.rect.center))

        small = FONT.render(str(self.value), True, color)
        screen.blit(small, (self.rect.x + 6, self.rect.y + 4))


# ----------------------------
# 🌌 BACKGROUND
# ----------------------------
stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(100)]

def draw_background():
    screen.blit(bg, (0, 0))
    for s in stars:
        pygame.draw.circle(screen, (100, 90, 80), s, 1)

# ----------------------------
# 🎴 GAME LOGIC
# ----------------------------
def draw_card_value():
    return random.randint(1, 10)

SIDE_VALUES = [-4, -3, -2, -1, 1, 2, 3, 4]

player_total = 0
ai_total = 0
message = "DRAW A CARD"
game_over = False

player_cards = []
ai_cards = []  # List pro ukládání vizuálních karet AI


# ----------------------------
# 🤖 AI (Upraveno pro vizuální barvu a rozložení karet)
# ----------------------------
def ai_play():
    global ai_total
    while ai_total < 16:
        value = draw_card_value()
        ai_total += value
        
        # --- ZMĚNA 2: ROZLOŽENÍ KARET AI (Max. dvě vedle sebe, pak pod sebou) ---
        # Používáme modulo 3 a dělení 3 pro vytvoření mřížky 3xN v prostředním panelu.
        # Panel začíná na X=355, Y=100.
        col = len(ai_cards) % 3
        row = len(ai_cards) // 3
        card_x = 355 + col * 85  # Rozestup zůstává
        card_y = 100 + row * 130 # Rozestup zůstává
        
        # --- ZMĚNA 1: BARVA KARTY AI (Změna z True na False) ---
        # Změna z True na False. Třída Card nyní použije TERRACOTTA barvu pro AI karty.
        ai_cards.append(Card(value, card_x, card_y, False))
        
        if ai_total > TARGET:
            break


# ----------------------------
# 🧍 ACTIONS (Hráčovy karty zůstávají 3 vedle sebe)
# ----------------------------
def add_player_card():
    global player_total
    value = draw_card_value()
    player_total += value
    
    # Výpočet pozice v levém (červeném) panelu: začátek na X=110, Y=160
    # Karty se skládají do mřížky 3xN, aby se jich do obdélníku vešlo víc.
    col = len(player_cards) % 3
    row = len(player_cards) // 3
    card_x = 87 + col * 85
    card_y = 100 + row * 130
    
    # Hráčovy karty zůstávají 'positive=True' (Amber)
    player_cards.append(Card(value, card_x, card_y, True))

def use_side_card():
    global player_total
    value = random.choice(SIDE_VALUES)
    player_total += value
    
    col = len(player_cards) % 3
    row = len(player_cards) // 3
    card_x = 87 + col * 85
    card_y = 100 + row * 130
    
    player_cards.append(Card(value, card_x, card_y, value > 0))


# ----------------------------
# 🔘 BUTTON
# ----------------------------
def button(text, x, y, w, h):
    rect = pygame.Rect(x, y, w, h)
    mouse = pygame.mouse.get_pos()

    hovered = rect.collidepoint(mouse)
    color = (65, 48, 38) if hovered else (40, 30, 24)

    if hovered:
        glow(rect, GLOW_AMBER)

    pygame.draw.rect(screen, color, rect, border_radius=10)
    pygame.draw.rect(screen, GLOW_AMBER, rect, 2, border_radius=10)

    label = FONT.render(text, True, TEXT_IVORY)
    screen.blit(label, label.get_rect(center=rect.center))

    return rect


# ----------------------------
# 🎮 LOOP
# ----------------------------
running = True

while running:
    clock.tick(60)
    draw_background()

    # SCORE (Vykresluje se v malém tmavém obdélníku vlevo dole)
    p = FONT.render(f"PLAYER: {player_total}", True, TEXT_GOLD)
    a = FONT.render(f"AI: {ai_total}", True, TEXT_TERRACOTTA) # Jméno AI je Terracotta

    screen.blit(p, (100, 475))
    screen.blit(a, (280, 475))

    msg = FONT.render(message, True, TEXT_IVORY)
    screen.blit(msg, (100, 550))

    # --- TLAČÍTKA V PRAVÉM PANELU ---
    BTN_X = 677
    BTN_W = 124
    BTN_H = 55

    draw_btn  = button("DRAW",  BTN_X, 130 + 0 * 95, BTN_W, BTN_H)
    side_btn  = button("SIDE",  BTN_X, 130 + 1 * 95, BTN_W, BTN_H)
    stand_btn = button("STAND", BTN_X, 130 + 2 * 95, BTN_W, BTN_H)
    reset_btn = button("RESET", BTN_X, 130 + 3 * 95, BTN_W, BTN_H)

    # DRAW CARDS (Hráčovy i AI karty)
    for c in player_cards:
        c.draw()
        
    for c in ai_cards:
        c.draw()

    pygame.display.update()

    # EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            if draw_btn.collidepoint(event.pos):
                add_player_card()
                message = "CARD DRAWN"

                if player_total > TARGET:
                    message = "💥 BUST!"
                    game_over = True

            if side_btn.collidepoint(event.pos):
                use_side_card()

            if stand_btn.collidepoint(event.pos):
                ai_play()

                if ai_total > TARGET:
                    message = "🎉 YOU WIN"
                elif player_total > ai_total:
                    message = "🎉 YOU WIN"
                elif player_total < ai_total:
                    message = "😢 YOU LOSE"
                else:
                    message = "DRAW"

                game_over = True

            if reset_btn.collidepoint(event.pos):
                player_total = 0
                ai_total = 0
                player_cards = []
                ai_cards = []
                message = "RESET"
                game_over = False

pygame.quit()