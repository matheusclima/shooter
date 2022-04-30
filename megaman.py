import pygame, os
from pygame import Vector2
from constants import *

class Megaman(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.actions = {
            'idle': 0,
            'run': 1,
            'jump': 2,
            'idle_shoot': 3,
            'run_shoot': 4,
            'jump_shoot': 5,
            'dash': 6
        }
        self.action = 'idle'
        self.sprites = self.load_animation_sprites(2.8)
        self.index = 0
        self.pos = Vector2(100, 32)
        self.speed = Vector2(5, 0)
        self.acceleration = GRAVITY
        self.flip = False
        self.image = self.sprites[self.actions['idle']][0]
        self.rect = self.image.get_rect(bottomleft = self.pos)
        self.jumping = False
        self.in_air = False
        self.shooting = False
        self.bullets = pygame.sprite.Group()
        self.dashing = False

    def load_animation_sprites(self, scale):
        sprites = []
        for action in self.actions:
            temp_list = []
            path = f'assets/img/megaman/{action}'
            number_of_frames = len(os.listdir(path))
            for i in range(number_of_frames):
                img = pygame.image.load(f'{path}/{i}.png')
                img = pygame.transform.scale(img, (int(img.get_width()*scale), int(img.get_height()*scale)))
                temp_list.append(img)
            sprites.append(temp_list)
        
        return sprites
 
    def move(self, right, left):
        dx = 0
        dy = 0
        direction = 0

        if right:
            self.flip = False
            direction = 1
    
        if left:
            self.flip = True
            direction = -1

        dx += direction * self.speed[0]

        if self.dashing:
            dx += direction * self.speed[0]
        
        #Jump effect
        if self.jumping and not self.in_air:
            self.speed[1] = -20
            self.jumping = False
            self.in_air = True
        
        dy += self.speed[1]

        self.pos += Vector2(dx, dy)
        self.rect = self.image.get_rect(bottomleft = self.pos)

    def animation(self, action):
        if action != self.action:
            self.index = 0
            self.action = action

        if action == 'run' or action == 'run_shoot':
            self.run()
            
        elif action == 'jump' or action == 'jump_shoot':    
            self.jump()

        elif action == 'dash':
            self.dash()
            
        else:
            if self.shooting:
                self.idle_shoot()
            else:
                self.idle()

    def fall(self):
                # Gravity effect
        self.speed += self.acceleration
        if self.speed[1] > 10: self.speed[1] = 10

    def dash(self):
        dash = self.actions[self.action]
        self.image = self.sprites[dash][int(self.index)]
        
        if self.index < 1: 
            self.index += 0.25
        else:
            self.index += 0.05
        if self.index >= len(self.sprites[dash]): 
            self.index = 0
            self.dashing = False

    def run(self):
        run = self.actions[self.action]
        self.image = self.sprites[run][int(self.index)]
        self.index += 0.25
        if self.index >= len(self.sprites[run]): self.index = 1
            
    def idle(self):
        idle = self.actions['idle']
        self.image = self.sprites[idle][int(self.index)]
        
        if self.index < 1: 
            self.index += 0.01
        else:
            self.index += 0.25
        
        if self.index >= len(self.sprites[idle]): self.index = 0

    def jump(self):
        jump = self.actions[self.action]
        cooldown = 0.25
        if self.speed[1] < -17:
            self.image = self.sprites[jump][0]
        elif self.in_air:
            if self.speed[1] < 0:
                if self.index < 3:
                    self.image = self.sprites[jump][int(self.index + 1)]
            else:
                self.image = self.sprites[jump][3]
        else:
            self.image = self.sprites[jump][int(self.index)]

        self.index += cooldown
        if self.speed[1] == 0 and not self.in_air: self.index = 0

    def idle_shoot(self):
        action = self.actions['idle_shoot']
        self.image = self.sprites[action][int(self.index)]
        self.index += 0.15
        if self.index >= len(self.sprites[action]): self.index = 0

    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
        self.bullets.draw(screen)
        self.bullets.update()
    