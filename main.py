import pygame
from src.constants import *

# Pygame Setup
pygame.init()
screen = pygame.display.set_mode(WIN_SIZE, pygame.SCALED)
clock = pygame.Clock()

# Player Setup
player_image = pygame.image.load("assets/player.png").convert_alpha()
player_rect = player_image.get_frect()
player_speed = 50

running = True
while running:
    dt = clock.tick(60) / 1000
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player_direction = pygame.Vector2(
        keys[pygame.K_d] - keys[pygame.K_a],  # Horizontal
        keys[pygame.K_s] - keys[pygame.K_w]   # Vertical
    )
    if player_direction:
        player_direction.normalize_ip()
    player_rect.center += player_direction * player_speed * dt

    screen.fill("black")
    screen.blit(player_image, player_rect)
    
    pygame.display.flip()
