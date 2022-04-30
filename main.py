from pygame.math import Vector2
from game import Game
from level import Level
from bullet import Bullet
from collision_handler import CollisionHandler
import pygame, sys

running = 1

idle = 1

game = Game()
game.start( )
screen = game.screen
megaman = game.megaman
clock = game.clock
collision = CollisionHandler()
flip = False
right = False
left = False
action = None
shooting_cooldown = 0

while game.running:

    if (right or left) and not megaman.in_air and not megaman.dashing:
        action = 'run'
        if megaman.shooting:
            shooting_cooldown += 1
            action = 'run_shoot'
        
    elif megaman.dashing and not megaman.in_air:
        action = 'dash'

    elif megaman.in_air:
        action = 'jump'
        if megaman.shooting:
            shooting_cooldown +=1
            action = 'jump_shoot'
    else:
        action = 'idle'
        if megaman.shooting:
            shooting_cooldown += 1
            action = 'idle_shoot'

    megaman.fall()
    megaman.move(right, left)
    megaman.animation(action)
    collision.detect_floor(megaman, game.level.floor)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                right = True
                left = False

            if event.key == pygame.K_LEFT:
                left = True
                right = False
    
            if event.key == pygame.K_x:
                megaman.jumping = True

            if event.key == pygame.K_z:
                megaman.shooting = True
                shooting_cooldown = 0
                bulletx, bullety, direction = megaman.rect.right, 0.99 * megaman.rect.centery, 1
                if megaman.flip:
                    bulletx, direction = megaman.rect.left, -1
                
                bullet = Bullet(bulletx, bullety, direction)
                megaman.bullets.add(bullet)

            if event.key == pygame.K_c:
                megaman.dashing = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                right = False
                megaman.dashing = False

            if event.key == pygame.K_LEFT:
                left = False
                megaman.dashing = False

            if event.key == pygame.K_x:
                megaman.jumping = False

    if shooting_cooldown > 25:
        megaman.shooting = False
        shooting_cooldown = 0

    game.draw()

    pygame.display.flip()
    clock.tick(60)