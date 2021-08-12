from pygame.constants import KEYDOWN
from megaman import Megaman
import pygame, sys

size = width, height = 720, 540
running = 1

idle = 1

pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
megaman = Megaman()

while running:
    keys = pygame.key.get_pressed()
    
    idle = 1

    if keys[pygame.K_RIGHT]:
        idle = 0
        megaman.running()
    elif keys[pygame.K_LEFT]:
        idle = 0
        megaman.running()
        megaman.image = pygame.transform.flip(megaman.image, True, False)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    if idle:
        megaman.index = 0
        megaman.idle()

    screen.fill((255, 255, 255))
    screen.blit(megaman.image, megaman.rect)

    pygame.display.flip()
    clock.tick(60)