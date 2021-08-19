import pygame
#Vai herdar de sprite

class MegamanRunningState(pygame.sprite.Sprite):

    def __init__(self, megaman):
        pygame.sprite.Sprite.__init__(self)
        self.megaman = megaman

        self.index = 0
        self.animation = []
        for i in range(11):
            img = pygame.image.load(f'assets/img/running/megaman{i}.png').convert_alpha()
            img = pygame.transform.scale2x(img)
            self.animation.append(img)
        
        self.image = self.animation[self.index]
        self.rect = self.image.get_rect(center = (100, 300))


    def update(self):
        self.image = self.animation[int(self.index)]
        speed = 5
        if self.megaman.direction == 'left':
            self.image = pygame.transform.flip(self.image, True, False)
            speed = -5

        self.index += 0.25
        if self.index >= len(self.animation): self.index = 1

        self.megaman.pos[0] += speed
        self.rect.center = self.megaman.pos

    # def jump(self):
    #     print('jumping')
    #     self.megaman.state = self.megaman.jump_state

    def stop(self):
        # print('stopped')
        self.index = 0
        self.megaman.state = self.megaman.idle_state

    
    def move(self):
        self.image = self.animation[int(self.index)]
        speed = 5
        if self.megaman.direction == 'left':
            self.image = pygame.transform.flip(self.image, True, False)
            speed = -5

        self.index += 0.25
        if self.index >= len(self.animation): self.index = 1

        self.megaman.pos[0] += speed
        self.rect.center = self.megaman.pos