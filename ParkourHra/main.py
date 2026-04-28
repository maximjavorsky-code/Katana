import pygame
import sys

# Inicializace pygame
pygame.init()

# Nastavení okna
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Parkour hra")

# Barvy
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 200, 0)

clock = pygame.time.Clock()

# Třída hráče
class Player:
    def __init__(self):
        self.rect = pygame.Rect(100, 400, 40, 50)
        self.vel_y = 0
        self.on_ground = False

    def move(self, keys):
        dx = 0

        if keys[pygame.K_LEFT]:
            dx = -5
        if keys[pygame.K_RIGHT]:
            dx = 5

        # skok
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = -15

        # gravitace
        self.vel_y += 1
        dy = self.vel_y

        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        pygame.draw.rect(screen, BLUE, self.rect)

# Třída platformy
class Platform:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)

    def draw(self):
        pygame.draw.rect(screen, GREEN, self.rect)

# vytvoření objektů
player = Player()

platforms = [
    Platform(0, 550, 800, 50),
    Platform(200, 450, 150, 20),
    Platform(400, 350, 150, 20),
    Platform(600, 250, 150, 20),
]

# herní smyčka
while True:
    clock.tick(60)
    screen.fill(WHITE)

    # eventy
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    player.move(keys)

    # kolize
    player.on_ground = False
    for platform in platforms:
        if player.rect.colliderect(platform.rect):
            if player.vel_y > 0:
                player.rect.bottom = platform.rect.top
                player.vel_y = 0
                player.on_ground = True

    # pád = restart
    if player.rect.y > HEIGHT:
        player = Player()

    # vykreslení
    player.draw()
    for platform in platforms:
        platform.draw()

    pygame.display.update()