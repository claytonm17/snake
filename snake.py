import pygame
import random

# Setup
pygame.init()
screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
running = True
dt = 0

grid_size = 20
width, height = 720 // grid_size, 480 // grid_size


player_position = [0, 0]

player_body = [ [0, 0], 
                [20,0],
            ]

rect_size = 20

food_position = [random.randint(0, width - 1) * grid_size, random.randint(0, height - 1) * grid_size]

current_direction = (0, 0)

while running:

    # Allow closing the app
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    for i in range(len(player_body) - 1, 0, -1):
        player_body[i][0] = player_body[i - 1][0]
        player_body[i][1] = player_body[i - 1][1]

    # Render game here
    pygame.draw.rect(screen, (255,0,0), (player_position[0], player_position[1], rect_size, rect_size))

    for segment in player_body:
        pygame.draw.rect(screen, (0, 255, 0), (segment[0], segment[1], rect_size, rect_size))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        current_direction = (0, -1)
    elif keys[pygame.K_s]:
        current_direction = (0, 1)
    elif keys[pygame.K_a]:
        current_direction = (-1, 0)
    elif keys[pygame.K_d]:
        current_direction = (1, 0)

    player_position[0] += current_direction[0] * grid_size
    player_position[1] += current_direction[1] * grid_size

    if player_position[0] < 0:
        player_position[0] = 0
        current_direction = (0, 1)
    elif player_position[0] >= 720 - grid_size:
        player_position[0] = 720 - grid_size
        current_direction = (0, 1)

    if player_position[1] < 0:
        player_position[1] = 0
        current_direction = (1, 0)
    elif player_position[1] >= 480 - grid_size:
        player_position[1] = 480 - grid_size
        current_direction = (1, 0)

    player_body[0][0] = player_position[0]
    player_body[0][1] = player_position[1]

    # Check for collision with body
    

    # Rendering grid lines
    for x in range(0, 720, grid_size):
        pygame.draw.line(screen, (100, 100, 100), (x, 0), (x, 480))
    for y in range(0, 480, grid_size):
        pygame.draw.line(screen, (100, 100, 100), (0, y), (720, y))

    # Food
    pygame.draw.rect(screen, (0, 0, 255), (food_position[0], food_position[1], grid_size, grid_size))

    if (
        player_position[0] == food_position[0]
        and player_position[1] == food_position[1]
    ):
        food_position = [random.randint(0, width - 1) * grid_size, random.randint(0, height - 1) * grid_size]

        player_body.append(player_body[-1].copy())

    pygame.display.flip()

    fps = 10
    dt = clock.tick(fps) / 1000

pygame.quit()