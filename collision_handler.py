import pygame
from constants import *

class CollisionHandler:
    def detect_floor(self, megaman, floor):
        sprite = pygame.sprite.Sprite()
        sprite.rect = pygame.Rect(megaman.rect.left, megaman.rect.top, megaman.rect.width, megaman.rect.height + megaman.speed[1])             
        collide = False
        for tile in floor:
            if tile.rect.colliderect(sprite): 
                collide = True
                temp_tile = tile
                
        if collide:
            megaman.speed[1] = 0
            megaman.acceleration[1] = 0
            megaman.rect.bottom = temp_tile.rect.top
            megaman.in_air = False
        else:
            megaman.acceleration[1] = 1
