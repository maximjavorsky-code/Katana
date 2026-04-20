import pygame
import sys
import random
import math

# Constants
WIDTH = 800
HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MegaBonk")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 24)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 5
        self.life = 3
        self.score = 0
        self.level = 1
        self.xp = 0
        self.damage = 1
        self.weapon = "Basic"
        self.abilities = {}
        self.bullets = pygame.sprite.Group()
        self.turrets = pygame.sprite.Group()
        self.auto_fire = False
        self.fire_rate = 15
        self.last_shot = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        self.rect.clamp_ip(screen.get_rect())
        if self.auto_fire:
            self.last_shot += 1
            if self.last_shot >= self.fire_rate:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.shoot(mouse_x, mouse_y)
                self.last_shot = 0

    def shoot(self, mouse_x, mouse_y):
        dx = mouse_x - self.rect.centerx
        dy = mouse_y - self.rect.centery
        dist = math.sqrt(dx**2 + dy**2)
        if dist == 0:
            return
        dx /= dist
        dy /= dist
        if self.weapon == "Spread Shot":
            angles = [-0.3, 0, 0.3]
            for angle in angles:
                cos_a = math.cos(angle)
                sin_a = math.sin(angle)
                ndx = dx * cos_a - dy * sin_a
                ndy = dx * sin_a + dy * cos_a
                bullet = Bullet(self.rect.centerx, self.rect.centery, ndx, ndy, self.damage)
                self.bullets.add(bullet)
        else:
            bullet = Bullet(self.rect.centerx, self.rect.centery, dx, dy, self.damage)
            self.bullets.add(bullet)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 20)
        self.rect.y = random.randint(0, HEIGHT - 20)
        self.speed = 2
        self.life = 1
        self.bullets = pygame.sprite.Group()
        self.last_shot = 0

    def update(self, player):
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery
        dist = math.sqrt(dx**2 + dy**2)
        if dist > 0:
            self.rect.x += (dx / dist) * self.speed
            self.rect.y += (dy / dist) * self.speed
        self.last_shot += 1
        if self.last_shot >= 30:
            self.shoot(player.rect.centerx, player.rect.centery)
            self.last_shot = 0

    def shoot(self, target_x, target_y):
        dx = target_x - self.rect.centerx
        dy = target_y - self.rect.centery
        dist = math.sqrt(dx**2 + dy**2)
        if dist == 0:
            return
        dx /= dist
        dy /= dist
        bullet = Bullet(self.rect.centerx, self.rect.centery, dx, dy, 1)
        self.bullets.add(bullet)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, dx, dy, damage):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.dx = dx * 10
        self.dy = dy * 10
        self.damage = damage

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        if not screen.get_rect().colliderect(self.rect):
            self.kill()

class AutoTurret(pygame.sprite.Sprite):
    def __init__(self, x, y, damage):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.damage = damage
        self.last_shot = 0

    def update(self, player, bullets):
        self.last_shot += 1
        if self.last_shot >= 20:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            dx = mouse_x - self.rect.centerx
            dy = mouse_y - self.rect.centery
            dist = math.sqrt(dx**2 + dy**2)
            if dist > 0:
                dx /= dist
                dy /= dist
                bullet = Bullet(self.rect.centerx, self.rect.centery, dx, dy, self.damage)
                bullets.add(bullet)
            self.last_shot = 0

class DirectionalTurret(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, damage):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction
        self.damage = damage
        self.last_shot = 0

    def update(self, bullets):
        self.last_shot += 1
        if self.last_shot >= 25:
            bullet = Bullet(self.rect.centerx, self.rect.centery, self.direction[0], self.direction[1], self.damage)
            bullets.add(bullet)
            self.last_shot = 0

class Game:
    def __init__(self):
        self.player = Player()
        self.enemies = pygame.sprite.Group()

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        self.spawn_initial_wave()

        self.level_xp = 50
        self.wave_number = 1

        self.choices = [
            ("Auto Fire", "Automatic firing", "auto_fire"),
            ("Spread Shot", "Shoot in multiple directions", "spread"),
            ("Extra Life", "Increase life", "life"),
            ("Speed Boost", "Increase speed", "speed"),
            ("Damage Up", "Increase damage", "damage"),
            ("Auto Turret", "Add automatic turret", "auto_turret"),
            ("Directional Turret", "Add directional turret", "dir_turret"),
        ]

    def spawn_initial_wave(self):
        for _ in range(5):
            self.spawn_enemy()

    def spawn_enemy(self):
        enemy = Enemy()
        self.enemies.add(enemy)
        self.all_sprites.add(enemy)

    def spawn_enemy_wave(self):
        if len(self.enemies) == 0:
            self.wave_number += 1
            for _ in range(5 + self.wave_number * 2):
                self.spawn_enemy()

    def apply_choice(self, choice):
        name, desc, typ = choice

        level = self.player.abilities.get(typ, 0)
        if level >= 5:
            return

        self.player.abilities[typ] = level + 1

        if typ == "auto_fire":
            lvl = self.player.abilities[typ]
            self.player.auto_fire = True
            self.player.fire_rate = max(3, 15 - 2 * lvl)
            self.player.weapon = name

        elif typ == "spread":
            self.player.weapon = name

        elif typ == "life":
            self.player.life += 1

        elif typ == "speed":
            self.player.speed += 1

        elif typ == "damage":
            self.player.damage += 1

        elif typ == "auto_turret":
            self._add_turret(AutoTurret)

        elif typ == "dir_turret":
            self._add_turret(
                DirectionalTurret,
                direction=(1, 0)
            )

    def _add_turret(self, turret_class, direction=None):
        if direction:
            turret = turret_class(
                self.player.rect.centerx,
                self.player.rect.centery,
                direction=direction,
                damage=self.player.damage
            )
        else:
            turret = turret_class(
                self.player.rect.centerx,
                self.player.rect.centery,
                damage=self.player.damage
            )

        self.player.turrets.add(turret)
        self.all_sprites.add(turret)

    def handle_collisions(self):
        # Enemy bullets → player
        for enemy in self.enemies:
            for bullet in enemy.bullets:
                if bullet.rect.colliderect(self.player.rect):
                    self.player.life -= 1
                    bullet.kill()

        # Player bullets → enemies
        for bullet in list(self.player.bullets):
            for enemy in list(self.enemies):
                if bullet.rect.colliderect(enemy.rect):
                    enemy.life -= self.player.damage
                    bullet.kill()

                    if enemy.life <= 0:
                        enemy.kill()
                        self.player.score += 10
                        self.player.xp += 10

    def check_level_up(self):
        if self.player.xp >= self.level_xp:
            self.player.level += 1
            self.player.xp -= self.level_xp
            self.level_xp *= 1.3
            self.level_up_screen_loop()

    def level_up_screen_loop(self):
        screen.fill((0, 0, 0))
        font_big = pygame.font.Font(None, 48)
        screen.blit(font_big.render("Level Up!", True, (255, 255, 255)), (300, 50))
        y = 150
        for i, (name, desc, typ) in enumerate(self.choices):
            level = self.player.abilities.get(typ, 0)
            color = (0, 255, 0) if level < 5 else (255, 0, 0)
            text = f"{i+1}. {name}: {desc} (Lv {level})"
            screen.blit(font.render(text, True, color), (50, y))
            y += 40
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    y = 150
                    for i, (name, desc, typ) in enumerate(self.choices):
                        if 50 <= mouse_x <= 650 and y <= mouse_y <= y + 30:
                            if self.player.abilities.get(typ, 0) < 5:
                                self.apply_choice((name, desc, typ))
                                waiting = False
                            break
                        y += 40

    def update_turrets(self):
        for turret in self.player.turrets:
            if isinstance(turret, AutoTurret):
                turret.update(self.player, self.player.bullets)
            elif isinstance(turret, DirectionalTurret):
                turret.update(self.player.bullets)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            mouse_x, mouse_y = pygame.mouse.get_pos()

            if pygame.mouse.get_pressed()[0]:
                self.player.shoot(mouse_x, mouse_y)

            # UPDATE
            self.player.update()
            self.player.bullets.update()
            self.enemies.update(self.player)

            for enemy in self.enemies:
                enemy.bullets.update()

            self.update_turrets()
            self.handle_collisions()

            self.check_level_up()
            self.spawn_enemy_wave()

            # DRAW
            screen.fill(WHITE)

            self.all_sprites.draw(screen)
            self.player.bullets.draw(screen)

            for enemy in self.enemies:
                enemy.bullets.draw(screen)

            pygame.draw.line(
                screen, BLACK,
                self.player.rect.center,
                (mouse_x, mouse_y), 2
            )

            self.draw_hud()

            pygame.display.flip()
            clock.tick(FPS)

    def draw_hud(self):
        screen.blit(font.render(f"Score: {int(self.player.score)}", True, BLACK), (10, 10))
        screen.blit(font.render(f"Level: {self.player.level}", True, BLACK), (10, 50))
        screen.blit(font.render(f"Life: {self.player.life}", True, RED), (10, 90))
        screen.blit(font.render(f"Weapon: {self.player.weapon}", True, BLACK), (10, 130))

        y = 170
        for typ, lvl in self.player.abilities.items():
            screen.blit(font.render(f"{typ}: Lv {lvl}", True, GREEN), (10, y))
            y += 30

if __name__ == "__main__":
    game = Game()
    game.run()