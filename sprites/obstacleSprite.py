####################################################################
#
#
# Shards of Creation -- sprites.obstacleSprite --
# A Fantasy Narrative RPG
# Liscense Here
#
#
####################################################################

try:
    # Standard Python Imports
    from itertools import chain, cycle
    import os
    import pygame
    import pytweening
    from random import choice, randint, random, uniform
    import sys

    # Non-Standard Imports
    from settings.settings import *
    from settings.map_links import *
    from settings.npc_settings import *
    from tilemap import collide_hit_rect
except ImportError as err:
    print ('Couldn\'t load module. {}'.format(err))
    raise

vector = pygame.math.Vector2


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, game, x, y, width, height):
        self._layer = WALL_LAYER
        self.groups = game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y


class Portal(pygame.sprite.Sprite):
    def __init__(self, game, x, y, width, height, key):
        self._layer = WALL_LAYER
        self.groups = game.portals
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.location = key
        self.game = game
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.next_map = MAP_PORTALS[self.game.current_map][self.location].next_map
        self.next_position = MAP_PORTALS[self.game.current_map][self.location].position
        self.next_rotation = MAP_PORTALS[self.game.current_map][self.location].rotation

    def update_map(self):
        # Load Screen
        self.game.draw_load_screen()

        # Cullling the previous map
        for item in self.game.items:
            if item not in self.game.player.player_inventory:
                item.kill()
        for wall in self.game.walls:
            wall.kill()
        for portal in self.game.portals:
            if portal != self:
                portal.kill()
        for mob in self.game.mobs:
            mob.kill()
        for projectile in self.game.projectiles:
            projectile.kill()
        for npc in self.game.npcs:
            npc.kill()
        self.game.camera = None

        # Player Updates
        if self.next_rotation:
            self.game.player.rotation = self.next_rotation
        self.game.player.new_map(self.next_position.x, self.next_position.y)

        # Map Updates
        self.game.switch_map(self.next_map, False)
        self.kill()
