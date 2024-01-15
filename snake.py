import pygame

# Setup
pygame.init()
screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
running = True
dt = 0


player_position = [100, 50]

player_body = [ [100, 50],
                [90, 50],
                [80,50],
                [70,50],
            ]

while running:

    # Allow closing the app
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    rect_size = 16

    # Render game here
    pygame.draw.rect(screen, (255,0,0), (player_position[0], player_position[1], rect_size, rect_size))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_position[1] > 0:
        player_position[1] -= 300 * dt
    elif keys[pygame.K_s] and player_position[1] < 480 - rect_size:
        player_position[1] += 300 * dt
    elif keys[pygame.K_a] and player_position[0] > 0:
        player_position[0] -= 300 * dt
    elif keys[pygame.K_d] and player_position[0] < 720 - rect_size:
        player_position[0] += 300 * dt

    # Update display
    pygame.display.flip()

    # limiting FPS to 60
    fps = 60
    dt = clock.tick(fps) / 1000

pygame.quit()