####################################################################
#
#
# Shards of Creation -- sprites.readableSprite --
# A Fantasy Narrative RPG
# Liscense Here
#
#
####################################################################

try:
    # Standard Python Imports
    import os
    import pygame
    import pytweening
    import sys

    # Non-Standard Imports
    from scripts.readable import READABLE
    from settings.settings import *
    from tilemap import collide_hit_rect
except ImportError as err:
    print ('Couldn\'t load module. {}'.format(err))
    raise

class Readable(pygame.sprite.Sprite):

    def __init__(self, game, x, y, width, height, key):
        self._layer = WALL_LAYER
        self.groups = game.readables
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.location = key
        self.game = game
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.text = READABLE[key]['text'].split('\n')
        self.name = READABLE[key]['title']
        self.color = READABLE[key]['color']
        self.colliding = False
        self.busy = False

    def draw_read(self):
        if self.colliding:
            x_y = self.game.map_layer.translate_point((self.rect.x, self.rect.y))
            self.game.draw_text('Read \'r\' {}'.format(self.name), 
                                self.game.dialogue_font, WHITE, 
                                x_y[0], x_y[1])
    
    def update(self):
        self.colliding = False
