import pygame
from tile import Tile

class Level(pygame.sprite.Sprite):
    def __init__(self, data, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.data = data
        self.map = pygame.Surface((width, height))
        self.floor = []

    def load_map(self, map):
        width = self.data["width"]
        t_width, t_height = self.data["tilewidth"], self.data["tileheight"]
        tileset = pygame.image.load(map)
        total_of_columns = tileset.get_width()/t_width

        for type, layer in enumerate(self.data["layers"]):
            for pos, tile in enumerate(layer["data"]):
                if tile > 0:
                    row = int((tile - 1)/total_of_columns)
                    column = (tile - 1) % total_of_columns
                    pos_y = int(pos/width)
                    pos_x = pos % width
                    sprite = tileset.subsurface((t_width * column, t_height * row), (t_width, t_height))
                    t = Tile(sprite, t_width * pos_x, t_height * pos_y)
                    if type == 1:
                        self.floor.append(t)
                    t.draw(self.map)
                    
    def draw_map(self, screen):
        screen.blit(self.map, (0, 0))

                    
