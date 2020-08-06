####################################################################
#
#
# Shards of Creation -- sprites.mobSprite --
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


class Mob(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = MOB_LAYER
        self.groups = game.all_sprites, game.mobs
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.mob_img.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.hit_rect = MOB_HIT_RECT.copy()
        self.hit_rect.center = self.rect.center
        self.position = vector(x, y)
        self.velocity = vector(0, 0)
        self.acceleration = vector(0, 0)
        self.rect.center = self.position
        self.rotation = 0
        self.health = MOB_HEALTH
        self.speed = choice(MOB_SPEEDS)
        self.target = game.player

    def __repr__(self):
        return '<Mob Position {}>'.format(self.position)

    def avoid_mobs(self):
        for mob in self.game.mobs:
            if mob != self:
                distance = self.position - mob.position
                if 0 < distance.length() < AVOID_RADIUS:
                    self.acceleration += distance.normalize()

    def update(self):
        target_distance = (self.game.player.position - self.position)
        if target_distance.length_squared() < DETECT_RADIUS**2: # Squared to optimize. Sqrt is slow
            if random() < 0.002:
                choice(self.game.mob_standard_sounds).play()
            self.rotation = target_distance.angle_to(vector(1, 0))
            self.rect = self.image.get_rect()
            self.acceleration = vector(1, 0).rotate(-self.rotation)
            self.avoid_mobs()
            self.acceleration.scale_to_length(self.speed)
            self.acceleration += self.velocity * -1
            self.velocity += self.acceleration * self.game.dt
            self.position += self.velocity * self.game.dt * 0.5 + self.acceleration * self.game.dt ** 2
            self.hit_rect.centerx = self.position.x
            collide_with_walls(self, self.game.walls, 'x')
            self.hit_rect.centery = self.position.y
            collide_with_walls(self, self.game.walls, 'y')
            self.rect.center = self.hit_rect.center
        self.image = pygame.transform.rotate(self.game.mob_img, self.rotation)
        self.rect.center = self.position
        if self.health <= 0:
            choice(self.game.mob_hit_sounds).play()
            self.kill()
            self.game.map_img.blit(self.game.splat, self.position - vector(TILESIZE / 2, TILESIZE / 2))

    def draw_health(self):
        if self.health > MOB_HEALTH * 0.6:
            color = GREEN
        elif self.health > MOB_HEALTH * 0.3:
            color = YELLOW
        else:
            color = RED
        width = int(self.rect.width * self.health / MOB_HEALTH)
        self.health_bar = pygame.Rect(0, 0, width, 3)
        if self.health < MOB_HEALTH:
            pygame.draw.rect(self.image, color, self.health_bar)