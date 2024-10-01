import pygame
from src.constants import *

pygame.init()
screen = pygame.display.set_mode(WIN_SIZE, pygame.SCALED)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
