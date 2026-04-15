import pygame
import random

# Inicializace pygame
pygame.init()

# Nastavení okna
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Frogger")

# Barvy
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# FPS
clock = pygame.time.Clock()

# Třída hráče
class Frog:
    def __init__(self):
        self.size = 40
        self.x = WIDTH // 2
        self.y = HEIGHT - self.size
        self.speed = 10

    def move(self, keys):
        # Pohyb hráče podle kláves
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, self.size, self.size))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)


# Třída auta
class Car:
    def __init__(self, y):
        self.width = 60
        self.height = 40
        self.x = random.randint(0, WIDTH)
        self.y = y
        self.speed = random.randint(3, 7)

    def move(self):
        self.x += self.speed
        # Pokud auto vyjede z obrazovky, vrátí se zpět
        if self.x > WIDTH:
            self.x = -self.width

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


# Vytvoření hráče
frog = Frog()

# Vytvoření aut
cars = []
for i in range(5):
    cars.append(Car(100 + i * 80))

# Herní smyčka
running = True
game_over = False

while running:
    clock.tick(60)
    screen.fill(WHITE)

    # Události
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if not game_over:
        frog.move(keys)

        # Pohyb aut
        for car in cars:
            car.move()

            # Kontrola kolize
            if frog.get_rect().colliderect(car.get_rect()):
                game_over = True

        # Výhra (dostane se nahoru)
        if frog.y <= 0:
            game_over = True

    # Vykreslení
    frog.draw()
    for car in cars:
        car.draw()

    # Game over text
    if game_over:
        font = pygame.font.SysFont(None, 50)
        text = font.render("GAME OVER - R pro restart", True, BLACK)
        screen.blit(text, (50, HEIGHT // 2))

        if keys[pygame.K_r]:
            frog = Frog()
            game_over = False

    pygame.display.flip()

pygame.quit()