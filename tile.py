import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = image.get_rect(topleft = (x, y))

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        color = (255, 0, 0)
        pygame.draw.rect(surface, color, pygame.Rect(self.rect), 2)