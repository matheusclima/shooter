#Vai herdar de sprite
import pygame

class MegamanIdleState(pygame.sprite.Sprite):

    def __init__(self, megaman):
        pygame.sprite.Sprite.__init__(self)
        self.megaman = megaman

        self.index = 0
        self.animation = []
        for i in range(3):
            img = pygame.image.load(f'assets/img/idle/idle.png').subsurface((34 * i, 0), (34, 35)).convert_alpha()
            img = pygame.transform.scale2x(img)
            self.animation.append(img)
        self.image = self.animation[self.index]
        self.rect = self.image.get_rect(center = self.megaman.pos)

    def update(self):
        self.image = self.animation[int(self.index)]

        if self.megaman.direction == 'left':
            self.image = pygame.transform.flip(self.image, True, False)

        self.rect.center = self.megaman.pos
        if int(self.index) == 0:
            self.index += 0.01
        else:
            self.index += 0.2
        if self.index >= len(self.animation): self.index = 0


    # def jump(self):
    #     print('jumping')
    #     self.megaman.state = self.megaman.jumping_state

    def stop(self):
        self.image = self.animation[int(self.index)]

        if self.megaman.direction == 'left':
            self.image = pygame.transform.flip(self.image, True, False)

        self.rect.center = self.megaman.pos
        if int(self.index) == 0:
            self.index += 0.01
        else:
            self.index += 0.2
        if self.index >= len(self.animation): self.index = 0

    def move(self):
        self.index = 0
        self.megaman.state = self.megaman.running_state