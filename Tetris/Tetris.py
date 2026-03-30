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

# Definice tetris tvarů (tetromino)
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
]

# Funkce pro vytvoření prázdné mřížky
def create_grid():
    return [[0 for _ in range(WIDTH // BLOCK_SIZE)] for _ in range(HEIGHT // BLOCK_SIZE)]

# Funkce pro vykreslení mřížky
def draw_grid(grid):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, WHITE,
                                 (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

# Třída pro padající blok
class Piece:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.x = WIDTH // BLOCK_SIZE // 2
        self.y = 0

    # vykreslení bloku
    def draw(self):
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, WHITE,
                                     ((self.x + x) * BLOCK_SIZE,
                                      (self.y + y) * BLOCK_SIZE,
                                      BLOCK_SIZE, BLOCK_SIZE))

# Kontrola kolize
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

# Zamknutí bloku do mřížky
def merge(piece, grid):
    for y, row in enumerate(piece.shape):
        for x, cell in enumerate(row):
            if cell:
                grid[piece.y + y][piece.x + x] = 1

# Mazání plných řádků
def clear_rows(grid):
    new_grid = [row for row in grid if any(cell == 0 for cell in row)]
    while len(new_grid) < len(grid):
        new_grid.insert(0, [0 for _ in range(len(grid[0]))])
    return new_grid

# Hlavní smyčka hry
def main():
    grid = create_grid()
    piece = Piece()

    clock = pygame.time.Clock()
    fall_time = 0

    running = True
    while running:
        screen.fill(BLACK)
        fall_time += clock.get_rawtime()
        clock.tick()

        # Pohyb dolů každých 500 ms
        if fall_time > 500:
            piece.y += 1
            if collision(piece, grid):
                piece.y -= 1
                merge(piece, grid)
                grid = clear_rows(grid)
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

                if event.key == pygame.K_DOWN:
                    piece.y += 1
                    if collision(piece, grid):
                        piece.y -= 1

        draw_grid(grid)
        piece.draw()

        pygame.display.update()

    pygame.quit()

# Spuštění programu
if __name__ == "__main__":
    main()