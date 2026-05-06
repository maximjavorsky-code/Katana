def draw_card(x, y, value, positive=True):
    rect = pygame.Rect(x, y, 80, 120)

    color = (40, 60, 120) if positive else (120, 40, 40)

    pygame.draw.rect(screen, (15, 15, 30), rect, border_radius=10)
    pygame.draw.rect(screen, color, rect, 2, border_radius=10)

    text = FONT.render(str(value), True, (255, 255, 255))
    screen.blit(text, text.get_rect(center=rect.center))