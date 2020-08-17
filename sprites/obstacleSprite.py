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


class Spawn(pygame.sprite.Sprite):
    def __init__(self, game, x, y, width, height, name):
        self._layer = WALL_LAYER
        self.groups = game.spawns
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.name = name
        self.game = game
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, width, height)
        self.rect.center = (x, y)

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
        self.rect.center = (x, y)
        self.next_map = MAP_PORTALS[self.game.current_map][self.location].next_map
        self.spawn_object = MAP_PORTALS[self.game.current_map][self.location].spawn_object
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
        for spawn in self.game.spawns:
            spawn.kill()
        for portal in self.game.portals:
            if portal != self:
                portal.kill()
        for mob in self.game.mobs:
            mob.kill()
        for projectile in self.game.projectiles:
            projectile.kill()
        for npc in self.game.npcs:
            npc.kill()

        # Map Updates
        self.game.switch_map(self.next_map, False)

        # Player Updates
        if self.next_rotation:
            self.game.player.rotation = self.next_rotation
        self.game.player.new_map(self.spawn_object)
        self.kill()
