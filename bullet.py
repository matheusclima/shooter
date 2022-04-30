import pygame
from pygame import Vector2
from constants import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = direction * Vector2(10, 0)
        self.image = self.load_sprite(2.8)
        self.pos = Vector2(x, y)
        self.rect = self.image.get_rect(center = self.pos)

    def load_sprite(self, scale):
        img = pygame.image.load(f'assets/img/bullet/0.png')
        img = pygame.transform.scale(img, (int(img.get_width()*scale), int(img.get_height()*scale)))
        return img

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.pos += self.speed
        self.rect = self.image.get_rect(center = self.pos)
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH: self.kill()