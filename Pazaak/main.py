import pygame
import subprocess
import sys

pygame.init()

WIDTH, HEIGHT = 900, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pazaak")

clock = pygame.time.Clock()

# COLORS
BG = (8, 10, 25)
PANEL = (20, 25, 60)
ACCENT = (120, 180, 255)
HOVER = (180, 220, 255)
TEXT = (230, 240, 255)

FONT = pygame.font.SysFont("consolas", 30)
BIG = pygame.font.SysFont("consolas", 64)


def draw_glow(rect, color):
    glow_surf = pygame.Surface((rect.w + 20, rect.h + 20), pygame.SRCALPHA)
    pygame.draw.rect(glow_surf, (*color, 40), glow_surf.get_rect(), border_radius=15)
    screen.blit(glow_surf, (rect.x - 10, rect.y - 10))


def button(text, x, y, w, h):
    mouse = pygame.mouse.get_pos()
    rect = pygame.Rect(x, y, w, h)

    hovered = rect.collidepoint(mouse)

    color = HOVER if hovered else PANEL

    if hovered:
        draw_glow(rect, ACCENT)

    pygame.draw.rect(screen, color, rect, border_radius=12)
    pygame.draw.rect(screen, ACCENT, rect, 2, border_radius=12)

    label = FONT.render(text, True, TEXT)
    label_rect = label.get_rect(center=rect.center)
    screen.blit(label, label_rect)

    return rect


def draw_bg():
    screen.fill(BG)

    # subtle gradient line
    pygame.draw.line(screen, ACCENT, (200, 140), (700, 140), 2)

    title = BIG.render("PAZAAK", True, ACCENT)
    subtitle = FONT.render("KOTOR STYLE LOBBY", True, TEXT)

    screen.blit(title, title.get_rect(center=(WIDTH // 2, 100)))
    screen.blit(subtitle, subtitle.get_rect(center=(WIDTH // 2, 150)))


running = True

while running:
    clock.tick(60)
    draw_bg()

    start_btn = button("START GAME", WIDTH//2 - 150, 240, 300, 65)
    tut_btn = button("TUTORIAL", WIDTH//2 - 150, 330, 300, 65)
    exit_btn = button("EXIT", WIDTH//2 - 150, 420, 300, 65)

    two_player_btn = button("2 PLAYER", WIDTH//2 - 150, 510, 300, 65)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_btn.collidepoint(event.pos):
                subprocess.run([sys.executable, "Pazaak/pazaak.py"])

            if two_player_btn.collidepoint(event.pos):
                subprocess.run([sys.executable, "Pazaak/pazaak_2p.py"])

            if tut_btn.collidepoint(event.pos):
                subprocess.run([sys.executable, "Pazaak/tutorial.py"])

            if exit_btn.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

pygame.quit()