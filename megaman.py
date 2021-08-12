import pygame
import time

class Megaman:
    
    def __init__(self):
        self.running_sprites = []
        self.idle_sprites = []
        for i in range(11):
            img = pygame.image.load(f'assets/img/running/megaman{i}.png').convert_alpha()
            img = pygame.transform.scale2x(img)
            self.running_sprites.append(img)
        
        for i in range(3):
            img = pygame.image.load(f'assets/img/idle/idle.png').subsurface((34 * i, 0), (34, 35)).convert_alpha()
            img = pygame.transform.scale2x(img)
            self.idle_sprites.append(img)

        self.index = 0
        self.image = self.idle_sprites[self.index]
        self.rect = self.image.get_rect(center = (100, 300))

    def running(self):
        self.image = self.running_sprites[int(self.index)]
        self.index += 0.3
        if self.index >= len(self.running_sprites): self.index = 0

    def idle(self):
        self.image = self.idle_sprites[int(self.index)]
        self.index += 0.01
        if self.index >= len(self.idle_sprites): self.index = 0