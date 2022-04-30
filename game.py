from megaman import Megaman
from level import Level
from bullet import Bullet
from constants import *
import pygame, json

class Game:
    def __init__(self):
        pygame.init()
        self.size = self.width, self.height = SCREEN_WIDTH, SCREEN_HEIGHT
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        self.running = True
        self.bullets = pygame.sprite.Group()

    def start(self):
        file = open('maps/introStage.json')
        data = json.load(file)
        file.close()
        self.level = Level(data, 800, 640)
        self.level.load_map('maps/introStage.png')
        self.megaman = Megaman()

    def draw(self):
        self.level.draw_map(self.screen)
        color = (0, 255, 0)
        self.megaman.draw(self.screen)
        pygame.draw.rect(self.screen, color, pygame.Rect(self.megaman.rect), 2)



