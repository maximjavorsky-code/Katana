import pygame
import random

pygame.init()

WIDTH, HEIGHT = 900, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pazaak - KOTOR Edition")

clock = pygame.time.Clock()

FONT = pygame.font.SysFont("consolas", 22)
BIG = pygame.font.SysFont("consolas", 54)

TARGET = 20

# COLORS
BG = (6, 8, 20)
TABLE = (10, 20, 50)
GLOW_BLUE = (120, 180, 255)
TEXT = (220, 230, 255)


# ----------------------------
# ✨ GLOW
# ----------------------------
def glow(rect, color):
    surf = pygame.Surface((rect.w+20, rect.h+20), pygame.SRCALPHA)
    pygame.draw.rect(surf, (*color, 40), surf.get_rect(), border_radius=12)
    screen.blit(surf, (rect.x-10, rect.y-10))


# ----------------------------
# 🎴 CARD (UPGRADED)
# ----------------------------
class Card:
    def __init__(self, value, x, y, positive=True):
        self.value = value
        self.rect = pygame.Rect(x, y, 70, 110)
        self.positive = positive

    def draw(self):
        color = (80, 140, 255) if self.positive else (200, 80, 80)

        # glow
        glow(self.rect, color)

        # base
        pygame.draw.rect(screen, (15, 18, 35), self.rect, border_radius=10)

        # border
        pygame.draw.rect(screen, color, self.rect, 2, border_radius=10)

        # center number
        text = BIG.render(str(self.value), True, (255, 255, 255))
        screen.blit(text, text.get_rect(center=self.rect.center))

        # small corner number
        small = FONT.render(str(self.value), True, color)
        screen.blit(small, (self.rect.x + 5, self.rect.y + 5))


# ----------------------------
# 🌌 BACKGROUND
# ----------------------------
stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(100)]

def draw_background():
    screen.fill(BG)

    for s in stars:
        pygame.draw.circle(screen, (120, 120, 180), s, 1)

    table_rect = pygame.Rect(100, 150, 700, 350)
    glow(table_rect, GLOW_BLUE)
    pygame.draw.rect(screen, TABLE, table_rect, border_radius=15)
    pygame.draw.rect(screen, GLOW_BLUE, table_rect, 2, border_radius=15)


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


# ----------------------------
# 🤖 AI
# ----------------------------
def ai_play():
    global ai_total
    while ai_total < 16:
        ai_total += draw_card_value()
        if ai_total > TARGET:
            break


# ----------------------------
# 🧍 ACTIONS
# ----------------------------
def add_player_card():
    global player_total

    value = draw_card_value()
    player_total += value

    player_cards.append(Card(value, 200 + len(player_cards)*80, 420, True))


def use_side_card():
    global player_total

    value = random.choice(SIDE_VALUES)
    player_total += value

    player_cards.append(Card(value, 200 + len(player_cards)*80, 300, value > 0))


# ----------------------------
# 🔘 BUTTON (HOVER + GLOW)
# ----------------------------
def button(text, x, y, w, h):
    rect = pygame.Rect(x, y, w, h)
    mouse = pygame.mouse.get_pos()

    hovered = rect.collidepoint(mouse)
    color = (40, 60, 120) if hovered else (20, 30, 70)

    if hovered:
        glow(rect, GLOW_BLUE)

    pygame.draw.rect(screen, color, rect, border_radius=10)
    pygame.draw.rect(screen, GLOW_BLUE, rect, 2, border_radius=10)

    label = FONT.render(text, True, TEXT)
    screen.blit(label, label.get_rect(center=rect.center))

    return rect


# ----------------------------
# 🎮 LOOP
# ----------------------------
running = True

while running:
    clock.tick(60)
    draw_background()

    # TITLE
    title = BIG.render("PAZAAK", True, GLOW_BLUE)
    screen.blit(title, title.get_rect(center=(WIDTH//2, 80)))

    # SCORE
    p = FONT.render(f"PLAYER: {player_total}", True, GLOW_BLUE)
    a = FONT.render(f"AI: {ai_total}", True, (255, 100, 100))

    screen.blit(p, (60, 120))
    screen.blit(a, (60, 150))

    msg = FONT.render(message, True, TEXT)
    screen.blit(msg, (60, 600))

    # BUTTONS
    draw_btn = button("DRAW", 60, 220, 130, 50)
    side_btn = button("SIDE", 210, 220, 130, 50)
    stand_btn = button("STAND", 360, 220, 130, 50)
    reset_btn = button("RESET", 510, 220, 130, 50)

    # CARDS
    for c in player_cards:
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
                message = "RESET"
                game_over = False

pygame.quit()