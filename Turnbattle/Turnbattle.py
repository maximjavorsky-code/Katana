import pygame
import sys

# Inicializace pygame
pygame.init()

# Nastavení okna
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 6
CELL_SIZE = WIDTH // GRID_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Tahová hra")

# Barvy
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 50, 50)
BLUE = (50, 50, 200)
GRAY = (200, 200, 200)

# Třída hráče
class Player:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        """Vykreslení hráče na obrazovku"""
        pygame.draw.rect(
            screen,
            self.color,
            (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
        )

    def move(self, dx, dy):
        """Pohyb hráče v rámci mřížky"""
        new_x = self.x + dx
        new_y = self.y + dy

        # Kontrola hranic
        if 0 <= new_x < GRID_SIZE and 0 <= new_y < GRID_SIZE:
            self.x = new_x
            self.y = new_y


# Vytvoření hráčů
player1 = Player(0, 0, RED)
player2 = Player(GRID_SIZE - 1, GRID_SIZE - 1, BLUE)

current_player = player1
game_over = False

def draw_grid():
    """Vykreslení herní mřížky"""
    for x in range(0, WIDTH, CELL_SIZE):
        for y in range(0, HEIGHT, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY, rect, 1)


def check_win():
    """Kontrola výhry"""
    if player1.x == player2.x and player1.y == player2.y:
        return True
    return False


def switch_turn():
    """Přepnutí hráče"""
    global current_player
    if current_player == player1:
        current_player = player2
    else:
        current_player = player1


# Herní smyčka
while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Ovládání pouze pokud hra běží
        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_UP:
                current_player.move(0, -1)
                switch_turn()
            elif event.key == pygame.K_DOWN:
                current_player.move(0, 1)
                switch_turn()
            elif event.key == pygame.K_LEFT:
                current_player.move(-1, 0)
                switch_turn()
            elif event.key == pygame.K_RIGHT:
                current_player.move(1, 0)
                switch_turn()

            # Kontrola výhry po tahu
            if check_win():
                game_over = True

    # Vykreslení
    draw_grid()
    player1.draw()
    player2.draw()

    # Text při konci hry
    if game_over:
        font = pygame.font.SysFont(None, 50)
        text = font.render("Konec hry!", True, BLACK)
        screen.blit(text, (200, 250))

    pygame.display.flip()