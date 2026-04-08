import pygame
import random

# Inicializace pygame
pygame.init()

# Nastavení okna
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man")

# Barvy
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# FPS
clock = pygame.time.Clock()

# Třída hráče (Pac-Man)
class Player:
    def __init__(self):
        self.rect = pygame.Rect(50, 50, 20, 20)
        self.speed = 5

    def move(self, keys):
        """
        Funkce pro pohyb hráče podle stisknutých kláves.
        """
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def draw(self):
        """
        Vykreslení hráče na obrazovku.
        """
        pygame.draw.circle(screen, YELLOW, self.rect.center, 10)

# Třída nepřítele (Ghost)
class Enemy:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, WIDTH), random.randint(0, HEIGHT), 20, 20)
        self.speed = 3

    def move(self):
        """
        Náhodný pohyb nepřítele.
        """
        self.rect.x += random.choice([-self.speed, self.speed])
        self.rect.y += random.choice([-self.speed, self.speed])

    def draw(self):
        pygame.draw.rect(screen, RED, self.rect)

# Třída bodu (pellet)
class Pellet:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, WIDTH), random.randint(0, HEIGHT), 5, 5)

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

# Vytvoření objektů
player = Player()
enemy = Enemy()
pellets = [Pellet() for _ in range(10)]

score = 0
font = pygame.font.SysFont(None, 30)

# Hlavní herní smyčka
running = True
while running:
    clock.tick(60)
    screen.fill(BLACK)

    # Zpracování událostí (např. zavření okna)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Ovládání hráče
    keys = pygame.key.get_pressed()
    player.move(keys)

    # Pohyb nepřítele
    enemy.move()

    # Kontrola kolizí s body
    for pellet in pellets[:]:
        if player.rect.colliderect(pellet.rect):
            pellets.remove(pellet)
            score += 1

    # Kontrola kolize s nepřítelem
    if player.rect.colliderect(enemy.rect):
        print("Game Over")
        running = False

    # Vykreslení objektů
    player.draw()
    enemy.draw()

    for pellet in pellets:
        pellet.draw()

    # Vykreslení skóre
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()