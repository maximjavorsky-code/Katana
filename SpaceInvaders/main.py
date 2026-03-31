import pygame
import random
import sys

pygame.init()

# okno
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# hráč (rychlejší)
player = pygame.Rect(370, 500, 60, 40)
player_speed = 9

# střely
bullets = []

# nepřátelé
enemies = []
enemy_timer = 0

# skóre a životy
score = 0
lives = 3

# funkce pro vytvoření nepřítele
def spawn_enemy():
    x = random.randint(0, WIDTH - 40)
    return pygame.Rect(x, 0, 40, 30)

# vykreslení hráče (letadlo)
def draw_player(rect):
    pygame.draw.polygon(screen, (0, 255, 0), [
        (rect.centerx, rect.y),           # špička
        (rect.x, rect.y + rect.height),   # levý spodní
        (rect.right, rect.y + rect.height) # pravý spodní
    ])

# vykreslení nepřítele (červené letadlo)
def draw_enemy(rect):
    pygame.draw.polygon(screen, (255, 0, 0), [
        (rect.x, rect.y),
        (rect.right, rect.y),
        (rect.centerx, rect.bottom)
    ])

# game over text
def draw_game_over():
    text = font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(text, (WIDTH//2 - 100, HEIGHT//2))

# hlavní smyčka
while True:
    # události
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(pygame.Rect(player.centerx - 2, player.y, 5, 15))

    # pohyb hráče
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed

    # spawn nepřátel
    enemy_timer += 1
    if enemy_timer > 35:
        enemies.append(spawn_enemy())
        enemy_timer = 0

    # pohyb střel
    for bullet in bullets[:]:
        bullet.y -= 10
        if bullet.y < 0:
            bullets.remove(bullet)

    # pohyb nepřátel
    for enemy in enemies[:]:
        enemy.y += 4

        # když projde dolů → ztráta života
        if enemy.y > HEIGHT:
            enemies.remove(enemy)
            lives -= 1

    # kolize
    for enemy in enemies[:]:
        for bullet in bullets[:]:
            if enemy.colliderect(bullet):
                enemies.remove(enemy)
                bullets.remove(bullet)
                score += 1
                break

    # vykreslení
    screen.fill((0, 0, 0))

    draw_player(player)

    for bullet in bullets:
        pygame.draw.rect(screen, (255, 255, 0), bullet)

    for enemy in enemies:
        draw_enemy(enemy)

    # skóre a životy
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    lives_text = font.render(f"Lives: {lives}", True, (255, 100, 100))

    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (650, 10))

    # game over
    if lives <= 0:
        draw_game_over()

    pygame.display.flip()
    clock.tick(60)