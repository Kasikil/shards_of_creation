####################################################################
#
#
# Shards of Creation -- sprites.projectileSprite --
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
except ImportError as err:
    print ('Couldn\'t load module. {}'.format(err))
    raise

vector = pygame.math.Vector2


class Projectile(pygame.sprite.Sprite):
    def __init__(self, game, rotation, position, direction, damage):
        self._layer = PROJECTILE_LAYER
        self.groups = game.all_sprites, game.projectiles
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rotation = rotation
        self.image = game.projectile_images[WEAPONS[self.game.player.weapon]['projectile_size']]
        self.image = pygame.transform.rotate(self.game.projectile_images[WEAPONS[self.game.player.weapon]['projectile_size']], self.rotation)
        self.rect = self.image.get_rect()
        self.hit_rect = self.rect
        self.position = vector(position)
        self.rect.center = position
        self.velocity = direction * WEAPONS[self.game.player.weapon]['projectile_speed'] * uniform(0.9, 1.1)
        self.spawn_time = pygame.time.get_ticks()
        self.damage = damage

    def __repr__(self):
        return '<Projectile {}>'.format(self.position)

    def update(self):
        self.position += self.velocity * self.game.dt
        self.rect.center = self.position
        if pygame.sprite.spritecollideany(self, self.game.walls):
            self.kill()
        if pygame.time.get_ticks() - self.spawn_time > WEAPONS[self.game.player.weapon]['projectile_lifetime']:
            self.kill()