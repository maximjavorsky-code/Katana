import pygame
import random

pygame.init()

WIDTH, HEIGHT = 900, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pazaak - 2P KOTOR Style")

FONT = pygame.font.SysFont("consolas", 22)
BIG = pygame.font.SysFont("consolas", 48)

TARGET = 20


# ----------------------------
# CORE
# ----------------------------
def draw_card():
    return random.randint(1, 10)


SIDE_VALUES = [-4, -3, -2, -1, 1, 2, 3, 4]


# ----------------------------
# STATE
# ----------------------------
p1_total = 0
p2_total = 0

turn = 1
message = "PLAYER 1 TURN"

game_over = False

# KOTOR SIDE DECK (hidden)
p1_side = random.sample(SIDE_VALUES, 4)
p2_side = random.sample(SIDE_VALUES, 4)


# SIDE MODE
side_mode = False


# ----------------------------
# TURN
# ----------------------------
def draw():
    global p1_total, p2_total, turn, message, game_over

    value = draw_card()

    if turn == 1:
        p1_total += value
        message = f"P1 +{value}"
        turn = 2
    else:
        p2_total += value
        message = f"P2 +{value}"
        turn = 1

    if p1_total > TARGET or p2_total > TARGET:
        game_over = True
        message = "GAME OVER"


def use_side(player):
    global p1_total, p2_total

    if player == 1:
        value = random.choice(p1_side)
        if value is not None:
            p1_total += value
            p1_side.remove(value)

    else:
        value = random.choice(p2_side)
        if value is not None:
            p2_total += value
            p2_side.remove(value)


def reset():
    global p1_total, p2_total, turn, game_over, message, p1_side, p2_side, side_mode

    p1_total = 0
    p2_total = 0
    turn = 1
    game_over = False
    side_mode = False
    message = "PLAYER 1 TURN"

    p1_side = random.sample(SIDE_VALUES, 4)
    p2_side = random.sample(SIDE_VALUES, 4)


# ----------------------------
# UI
# ----------------------------
def button(text, x, y, w, h, active=True):
    rect = pygame.Rect(x, y, w, h)

    color = (40, 60, 120) if active else (20, 20, 30)

    pygame.draw.rect(screen, color, rect, border_radius=10)
    pygame.draw.rect(screen, (120, 180, 255), rect, 2, border_radius=10)

    label = FONT.render(text, True, (255, 255, 255))
    screen.blit(label, label.get_rect(center=rect.center))

    return rect


# ----------------------------
# LOOP
# ----------------------------
running = True

while running:
    screen.fill((10, 10, 30))

    # ----------------------------
# ACTIVE PLAYER INDICATOR
# ----------------------------
if turn == 1:
    # P1 ACTIVE (LEFT SIDE GLOW)
    pygame.draw.rect(screen, (30, 80, 200), (0, 0, WIDTH//2, HEIGHT), 0)
    overlay = pygame.Surface((WIDTH//2, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 120, 255, 40))
    screen.blit(overlay, (0, 0))

else:
    # P2 ACTIVE (RIGHT SIDE GLOW)
    pygame.draw.rect(screen, (120, 30, 30), (WIDTH//2, 0, WIDTH//2, HEIGHT), 0)
    overlay = pygame.Surface((WIDTH//2, HEIGHT), pygame.SRCALPHA)
    overlay.fill((255, 80, 80, 40))
    screen.blit(overlay, (WIDTH//2, 0))
    
    title = BIG.render("PAZAAK 2P", True, (200, 220, 255))
    screen.blit(title, (320, 50))

    p1 = FONT.render(f"P1: {p1_total}", True, (100, 200, 255))
    p2 = FONT.render(f"P2: {p2_total}", True, (255, 100, 100))

    screen.blit(p1, (80, 120))
    screen.blit(p2, (80, 150))

    screen.blit(FONT.render(message, True, (255, 255, 255)), (80, 560))

    # ----------------------------
    # BUTTONS (KOTOR STYLE)
    # ----------------------------
    draw_btn = button("DRAW", 80, 250, 150, 60, not game_over)
    stand_btn = button("STAND", 260, 250, 150, 60, not game_over)
    side_btn = button("SIDE", 440, 250, 150, 60, not game_over)
    reset_btn = button("RESET", 620, 250, 150, 60, True)

    pygame.display.update()

    # ----------------------------
    # EVENTS
    # ----------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            if reset_btn.collidepoint(event.pos):
                reset()

            if game_over:
                continue

            # DRAW
            if draw_btn.collidepoint(event.pos):
                draw()

            # STAND
            if stand_btn.collidepoint(event.pos):
                if turn == 1:
                    turn = 2
                else:
                    turn = 1

                message = "TURN SWITCH"

            # SIDE (KOTOR STYLE: immediate use)
            if side_btn.collidepoint(event.pos):

                if turn == 1 and p1_side:
                    use_side(1)
                    message = "P1 used SIDE"

                elif turn == 2 and p2_side:
                    use_side(2)
                    message = "P2 used SIDE"

pygame.quit()