# --- Game class (úpravy) ---
class Game:
    def __init__(self):
        self.player = Player()
        self.enemies = pygame.sprite.Group()
        for _ in range(5):
            self.enemies.add(Enemy())
        # Hlavní sprite skupina
        self.all_sprites = pygame.sprite.Group(self.player, *self.enemies)
        self.level_xp = 50

    def apply_choice(self, choice):
        name, desc, typ = choice
        level = self.player.abilities.get(typ,0)
        if level < 5:
            self.player.abilities[typ] = level + 1

        if typ == "auto_fire":
            self.player.auto_fire = True
            self.player.fire_rate = max(3, 15 - 2*self.player.abilities[typ])
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
            turret = AutoTurret(self.player.rect.centerx, self.player.rect.centery, damage=self.player.damage)
            self.player.turrets.add(turret)
            self.all_sprites.add(turret)  # ← DŮLEŽITÉ: přidání do all_sprites
        elif typ == "dir_turret":
            turret = DirectionalTurret(self.player.rect.centerx, self.player.rect.centery, direction=(1,0), damage=self.player.damage)
            self.player.turrets.add(turret)
            self.all_sprites.add(turret)  # ← DŮLEŽITÉ: přidání do all_sprites

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            mouse_x, mouse_y = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0]:
                self.player.shoot(mouse_x, mouse_y)

            # Aktualizace hráče a projektilů
            self.player.update()
            self.player.bullets.update()
            for turret in self.player.turrets:
                if isinstance(turret, AutoTurret):
                    turret.update(self.player, self.player.bullets)
                elif isinstance(turret, DirectionalTurret):
                    turret.update(self.player.bullets)

            # Aktualizace nepřátel
            for enemy in self.enemies:
                enemy.update(self.player)
                enemy.bullets.update()

            # Kolize
            for enemy in self.enemies:
                for bullet in enemy.bullets:
                    if bullet.rect.colliderect(self.player.rect):
                        self.player.life -= 1
                        bullet.kill()
            for bullet in list(self.player.bullets):
                for enemy in list(self.enemies):
                    if bullet.rect.colliderect(enemy.rect):
                        enemy.life -= self.player.damage
                        bullet.kill()
                        if enemy.life <= 0:
                            enemy.kill()
                            self.player.score += 10
                            self.player.xp += 10

            # Level up
            if self.player.xp >= self.level_xp:
                self.player.level +=1
                self.level_xp *= 1.3
                self.level_up_screen_loop()

            self.spawn_enemy_wave()

            # --- Vykreslení ---
            screen.fill(WHITE)
            self.all_sprites.draw(screen)
            self.player.bullets.draw(screen)
            for enemy in self.enemies:
                enemy.bullets.draw(screen)

            # Linie směru myši
            pygame.draw.line(screen, BLACK, self.player.rect.center, (mouse_x, mouse_y), 2)

            # HUD
            screen.blit(font.render(f"Score: {int(self.player.score)}", True, BLACK), (10,10))
            screen.blit(font.render(f"Level: {self.player.level}", True, BLACK), (10,50))
            screen.blit(font.render(f"Life: {self.player.life}", True, RED), (10,90))
            screen.blit(font.render(f"Weapon: {self.player.weapon}", True, BLACK), (10,130))
            y_off = 170
            for typ, lvl in self.player.abilities.items():
                screen.blit(font.render(f"{typ}: Level {lvl}", True, GREEN), (10, y_off))
                y_off += 30

            pygame.display.flip()
            clock.tick(FPS)