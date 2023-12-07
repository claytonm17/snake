import pygame

# Setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0


player_position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:

    # Allow closing the app
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(("black"))

    # Render game here
    pygame.draw.rect(screen, 'green', (player_position.x, player_position.y, 50, 50))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_position.y -= 300 * dt
    elif keys[pygame.K_s]:
        player_position.y += 300 * dt
    elif keys[pygame.K_a]:
        player_position.x -= 300 * dt
    elif keys[pygame.K_d]:
        player_position.x += 300 * dt

    # Update display
    pygame.display.flip()

    # limiting FPS to 60
    dt = clock.tick(60) / 1000

pygame.quit()