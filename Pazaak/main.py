import pygame
import subprocess
import sys

pygame.init()

WIDTH, HEIGHT = 900, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PAZAAK")

clock = pygame.time.Clock()

# ----------------------------
# LOAD BACKGROUND
# ----------------------------
bg = pygame.image.load("Pazaak/assets/lobby_bg.png")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

# ----------------------------
# COLORS
# ----------------------------
GOLD = (210, 170, 90)
HOVER = (255, 210, 120)
TEXT = (240, 220, 170)

FONT = pygame.font.SysFont("timesnewroman", 34)
BIG = pygame.font.SysFont("timesnewroman", 92)

# ----------------------------
# BUTTON
# ----------------------------
def button(text, x, y, w, h):
    mouse = pygame.mouse.get_pos()

    rect = pygame.Rect(x, y, w, h)

    hovered = rect.collidepoint(mouse)

    # transparent surface
    surf = pygame.Surface((w, h), pygame.SRCALPHA)

    if hovered:
        pygame.draw.rect(
            surf,
            (255, 220, 140, 45),
            surf.get_rect(),
            border_radius=6
        )
        border = HOVER
    else:
        pygame.draw.rect(
            surf,
            (20, 10, 5, 160),
            surf.get_rect(),
            border_radius=6
        )
        border = GOLD

    screen.blit(surf, (x, y))

    pygame.draw.rect(screen, border, rect, 2, border_radius=6)

    label = FONT.render(text, True, border)

    screen.blit(label, label.get_rect(center=rect.center))

    return rect


# ----------------------------
# DRAW
# ----------------------------
def draw():
    screen.blit(bg, (0, 0))

    # dark cinematic overlay
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 40))
    screen.blit(overlay, (0, 0))

# ----------------------------
# LOOP
# ----------------------------
running = True

while running:
    clock.tick(60)

    draw()

    tut_btn = button("TUTORIAL", WIDTH//2 - 140, 360, 280, 60)

    start_btn = button("START", WIDTH//2 - 140, 440, 280, 60)

    exit_btn = button("EXIT", WIDTH//2 - 140, 520, 280, 60)

    pygame.display.update()

    # ----------------------------
    # EVENTS
    # ----------------------------
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            if start_btn.collidepoint(event.pos):
                subprocess.run([sys.executable, "Pazaak/pazaak.py"])

            if tut_btn.collidepoint(event.pos):
                subprocess.run([sys.executable, "Pazaak/tutorial.py"])

            if exit_btn.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

pygame.quit()