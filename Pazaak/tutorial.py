import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pazaak Tutorial")

FONT = pygame.font.SysFont("arial", 22)
BIG = pygame.font.SysFont("arial", 40)

def draw():
    screen.fill((10, 10, 25))

    title = BIG.render("PAZAAK RULES", True, (200, 220, 255))
    screen.blit(title, (250, 50))

    text = [
        "Cíl: dostat se co nejblíž k 20 bez překročení.",
        "Každé kolo taháš kartu 1-10.",
        "Můžeš použít side karty (+/- hodnoty).",
        "Side kartu můžeš použít max 4x.",
        "Když překročíš 20 = prohra.",
        "AI hraje automaticky."
    ]

    y = 150
    for line in text:
        render = FONT.render(line, True, (255, 255, 255))
        screen.blit(render, (80, y))
        y += 40

    hint = FONT.render("Zavři okno pro návrat do lobby", True, (150, 150, 150))
    screen.blit(hint, (120, 520))

running = True
while running:
    draw()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()