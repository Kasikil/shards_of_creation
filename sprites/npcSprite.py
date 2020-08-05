####################################################################
#
#
# [Untitled Game] -- sprites.npcSprite --
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
    from settings.npc_settings import *
    from tilemap import collide_hit_rect
    from utilities import collide_with_walls
except ImportError as err:
    print ('Couldn\'t load module. {}'.format(err))
    raise

vector = pygame.math.Vector2


class Npc(pygame.sprite.Sprite):
    def __init__(self, game, x, y, identifier):
        self._layer = NPC_LAYER
        self.groups = game.all_sprites, game.npcs
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.name = NPCS[identifier]['name']
        self.image = self.game.npc_images[self.name].copy()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.hit_rect = NPCS[identifier]['hit_rect'].copy()
        self.hit_rect.center = self.rect.center
        self.position = vector(x, y)
        self.velocity = vector(0, 0)
        self.rect.center = self.position
        self.rotation = 0
        self.health = NPCS[identifier]['health']
        self.speed = NPCS[identifier]['speed']
        self.busy = False
        self.dialogue = NPCS[identifier]['dialogue']

        # Waypoint System Initialization
        self.waypoint = False
        self.wait_location_time = 0
        self.time_waiting = 0
        if NPCS[identifier]['movement_method'] == 'waypoint':
            self.waypoint = True
            if NPCS[identifier]['waypoint_system'] == 'relative':
                abs_ways = []
                for waypoint in NPCS[identifier]['waypoints']:
                    waypoint = [waypoint[0] + x, waypoint[1] + y]
                    abs_ways.append(vector(waypoint[0], waypoint[1]))
                self.waypoints = cycle(abs_ways)
            else:
                self.waypoints = cycle(NPCS[identifier]['waypoints'])
            self.waysleep = cycle(NPCS[identifier]['waysleep'])
            self.target = next(self.waypoints)
            self.waymode = 'find'
                    
    def __repr__(self):
        return '<NPC {} at ({},{})>'.format(self.name, self.position.x, self.position.y)

    def update(self):
        if self.waypoint and not self.busy:
            target_distance = (self.target - self.position)
            wait_time = pygame.time.get_ticks() - self.time_waiting
            if self.waymode == 'find' and target_distance.length_squared() != 0: # Not there yet, time to move
                self.rotation = target_distance.angle_to(vector(1, 0))
                self.rect = self.image.get_rect()
                self.velocity = vector(self.speed, 0).rotate(-self.rotation)
                if (self.velocity * self.game.dt).length_squared() < target_distance.length_squared():
                    self.position += self.velocity * self.game.dt
                else:
                    self.position = vector(self.target.x, self.target.y)
                self.hit_rect.centerx = self.position.x
                collide_with_walls(self, self.game.walls, 'x')
                self.hit_rect.centery = self.position.y
                collide_with_walls(self, self.game.walls, 'y')
                self.rect.center = self.hit_rect.center
                self.image = pygame.transform.rotate(self.game.npc_images[self.name], self.rotation)
                self.rect.center = self.position
            elif self.waymode == 'find' and target_distance.length_squared() == 0: # NPC is there, time to wait
                self.waymode = 'sleep'
                self.wait_location_time = next(self.waysleep)
                self.time_waiting = pygame.time.get_ticks()
            elif self.waymode == 'sleep' and wait_time < self.wait_location_time: # Waiting
                pass
            elif self.waymode == 'sleep' and wait_time >= self.wait_location_time: # Done waiting, onwards to the next point
                self.target = next(self.waypoints)
                self.waymode = 'find'
