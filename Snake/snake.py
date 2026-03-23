import pygame
import random

# Inicializace pygame
pygame.init()

# Nastavení okna
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Barvy
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# FPS (rychlost hry)
clock = pygame.time.Clock()
FPS = 10


def draw_snake(snake):
    """Vykreslí hada na obrazovku"""
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))


def generate_food():
    """Vygeneruje jídlo na náhodné pozici"""
    x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
    y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
    return (x, y)


def main():
    # Počáteční pozice hada
    snake = [(100, 100), (80, 100), (60, 100)]
    direction = (20, 0)

    food = generate_food()

    running = True
    while running:
        screen.fill(BLACK)

        # Zpracování vstupu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Ovládání šipkami
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, 20):
                    direction = (0, -20)
                elif event.key == pygame.K_DOWN and direction != (0, -20):
                    direction = (0, 20)
                elif event.key == pygame.K_LEFT and direction != (20, 0):
                    direction = (-20, 0)
                elif event.key == pygame.K_RIGHT and direction != (-20, 0):
                    direction = (20, 0)

        # Pohyb hada
        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake.insert(0, head)

        # Kontrola snězení jídla
        if head == food:
            food = generate_food()
        else:
            snake.pop()

        # Kolize se stěnou
        if (
            head[0] < 0 or head[0] >= WIDTH or
            head[1] < 0 or head[1] >= HEIGHT
        ):
            running = False

        # Kolize se sebou samým
        if head in snake[1:]:
            running = False

        # Vykreslení jídla
        pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

        # Vykreslení hada
        draw_snake(snake)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()