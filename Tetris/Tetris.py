import pygame
import random

# Inicializace pygame
pygame.init()

# Velikost okna
WIDTH, HEIGHT = 300, 600
BLOCK_SIZE = 30

# Vytvoření okna
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

# Barvy
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [
    (0, 255, 255),   # Cyan - I
    (255, 255, 0),   # Yellow - O
    (128, 0, 128),   # Purple - T
    (0, 255, 0),     # Green - S
    (255, 0, 0),     # Red - Z
    (0, 0, 255),     # Blue - J
    (255, 165, 0)    # Orange - L
]

# Tetromino tvary
SHAPES = [
    [[1, 1, 1, 1]],           # I
    [[1, 1], [1, 1]],         # O
    [[0, 1, 0], [1, 1, 1]],   # T
    [[0, 1, 1], [1, 1, 0]],   # S
    [[1, 1, 0], [0, 1, 1]],   # Z
    [[1, 0, 0], [1, 1, 1]],   # J
    [[0, 0, 1], [1, 1, 1]],   # L
    [[1, 1, 1], [0, 1, 0]],   # T variant
    [[1, 0], [1, 1], [1, 0]]  # Plus variant
]

def create_grid():
    return [[0 for _ in range(WIDTH // BLOCK_SIZE)] for _ in range(HEIGHT // BLOCK_SIZE)]

def draw_grid(grid):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, cell,
                                 (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(screen, BLACK,
                                 (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

class Piece:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = random.choice(COLORS)
        self.x = WIDTH // BLOCK_SIZE // 2 - len(self.shape[0]) // 2
        self.y = 0

    def draw(self):
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, self.color,
                                     ((self.x + x) * BLOCK_SIZE,
                                      (self.y + y) * BLOCK_SIZE,
                                      BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(screen, BLACK,
                                     ((self.x + x) * BLOCK_SIZE,
                                      (self.y + y) * BLOCK_SIZE,
                                      BLOCK_SIZE, BLOCK_SIZE), 1)

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

def collision(piece, grid):
    for y, row in enumerate(piece.shape):
        for x, cell in enumerate(row):
            if cell:
                new_x = piece.x + x
                new_y = piece.y + y
                if new_x < 0 or new_x >= len(grid[0]) or new_y >= len(grid):
                    return True
                if new_y >= 0 and grid[new_y][new_x]:
                    return True
    return False

def merge(piece, grid):
    for y, row in enumerate(piece.shape):
        for x, cell in enumerate(row):
            if cell:
                grid[piece.y + y][piece.x + x] = piece.color

def clear_rows(grid):
    cleared = 0
    new_grid = []
    for row in grid:
        if all(row):
            cleared += 1
        else:
            new_grid.append(row)
    while len(new_grid) < len(grid):
        new_grid.insert(0, [0 for _ in range(len(grid[0]))])
    return new_grid, cleared

def main():
    grid = create_grid()
    piece = Piece()
    score = 0
    fall_speed = 500  # počáteční rychlost pádu (ms)
    level_up_interval = 5000  # zrychlení každých 5 sekund
    last_level_up = pygame.time.get_ticks()

    clock = pygame.time.Clock()
    fall_time = 0

    font = pygame.font.SysFont("Arial", 24)
    running = True
    while running:
        current_time = pygame.time.get_ticks()
        # postupné zrychlování
        if current_time - last_level_up > level_up_interval and fall_speed > 100:
            fall_speed -= 50
            last_level_up = current_time

        screen.fill(BLACK)
        fall_time += clock.get_rawtime()
        clock.tick()

        # Rychlejší pád při držení šipky dolů
        keys = pygame.key.get_pressed()
        current_speed = fall_speed // 10 if keys[pygame.K_DOWN] else fall_speed

        if fall_time > current_speed:
            piece.y += 1
            if collision(piece, grid):
                piece.y -= 1
                merge(piece, grid)
                grid, cleared = clear_rows(grid)
                if cleared > 0:
                    score += cleared * 100
                piece = Piece()
                if collision(piece, grid):
                    print("Game Over")
                    running = False
            fall_time = 0

        # Ovládání
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    piece.x -= 1
                    if collision(piece, grid):
                        piece.x += 1
                if event.key == pygame.K_RIGHT:
                    piece.x += 1
                    if collision(piece, grid):
                        piece.x -= 1
                if event.key == pygame.K_UP:
                    piece.rotate()
                    if collision(piece, grid):
                        for _ in range(3):
                            piece.rotate()
                if event.key == pygame.K_SPACE:  # hard drop
                    while not collision(piece, grid):
                        piece.y += 1
                    piece.y -= 1
                    merge(piece, grid)
                    grid, cleared = clear_rows(grid)
                    if cleared > 0:
                        score += cleared * 100
                    piece = Piece()
                    if collision(piece, grid):
                        print("Game Over")
                        running = False

        # Skóre
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (5, 5))
        # Ovládání
        control_text = font.render("Rotate: Up, Drop: Space", True, WHITE)
        screen.blit(control_text, (WIDTH - 200, 5))

        draw_grid(grid)
        piece.draw()
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()