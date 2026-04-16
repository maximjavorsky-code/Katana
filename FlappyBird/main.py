import pygame
import random

# Inicializace pygame
pygame.init()

# Nastavení okna
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Barvy
WHITE = (255, 255, 255)

# FPS (rychlost hry)
clock = pygame.time.Clock()
FPS = 60

# Třída ptáka
class Bird:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT // 2
        self.velocity = 0
        self.gravity = 0.5
        self.jump = -10
        self.size = 20

    def move(self):
        # gravitace (pták padá dolů)
        self.velocity += self.gravity
        self.y += self.velocity

    def flap(self):
        # skok nahoru
        self.velocity = self.jump

    def draw(self):
        pygame.draw.rect(screen, (255, 255, 0), (self.x, self.y, self.size, self.size))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)


# Třída trubky
class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(100, 400)
        self.width = 50
        self.gap = 150  # mezera mezi trubkami

    def move(self):
        # pohyb doleva
        self.x -= 3

    def draw(self):
        # horní trubka
        pygame.draw.rect(screen, (0, 255, 0), (self.x, 0, self.width, self.height))
        # dolní trubka
        pygame.draw.rect(
            screen,
            (0, 255, 0),
            (self.x, self.height + self.gap, self.width, HEIGHT)
        )

    def collide(self, bird):
        bird_rect = bird.get_rect()

        top_rect = pygame.Rect(self.x, 0, self.width, self.height)
        bottom_rect = pygame.Rect(self.x, self.height + self.gap, self.width, HEIGHT)

        return bird_rect.colliderect(top_rect) or bird_rect.colliderect(bottom_rect)


# Inicializace hry
bird = Bird()
pipes = [Pipe(400)]
score = 0
font = pygame.font.SysFont(None, 36)

running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)

    # Ovládání
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.flap()

    # Pohyb ptáka
    bird.move()

    # Trubky
    for pipe in pipes:
        pipe.move()
        pipe.draw()

        # Kolize
        if pipe.collide(bird):
            running = False

    # Přidání nové trubky
    if pipes[-1].x < 250:
        pipes.append(Pipe(400))

    # Odstranění starých trubek
    if pipes[0].x < -50:
        pipes.pop(0)
        score += 1

    # Vykreslení ptáka
    bird.draw()

    # Skóre
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.update()

pygame.quit()