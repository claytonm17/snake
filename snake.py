import pygame

# Setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:

    # Allow closing the app
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Render game here

    # limiting FPS to 60
    clock.tick(60)

pygame.quit()