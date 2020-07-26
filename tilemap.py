####################################################################
#
#
# Shards of Creation -- tilemap --
# A Fantasy Narrative RPG
# Liscense Here
#
#
####################################################################

try:
    # Standard Python Imports
    import os
    import pygame

    # Non-Standard Imports
    from settings import *
except ImportError as err:
    print ('Couldn\'t load module. {}'.format(err))
    raise

class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as map_file:
            for line in map_file:
                self.data.append(line.strip())

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE


class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(WIDTH/2)
        y = -target.rect.y + int(HEIGHT/2)

        # limit scrolling to one side
        x = min(0, x) # left
        y = min(0, y) # top
        x = max(-(self.width - WIDTH), x) # right
        y = max(-(self.height - HEIGHT), y) # bottom
        self.camera = pygame.Rect(x, y, self.width, self.height)