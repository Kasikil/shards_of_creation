####################################################################
#
#
# Shards of Creation -- sprites.itemSprite --
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


class Item(pygame.sprite.Sprite):
    def __init__(self, game, position, name, visible=True):
        self._layer = ITEMS_LAYER
        self.groups = game.all_sprites, game.items
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = self.game.item_images[name]
        self.rect = self.image.get_rect()
        self.hit_rect = self.rect
        self.type = name
        self.position = position
        self.rect.center = position
        self.tween = pytweening.easeInOutSine
        self.step = 0
        self.direction = 1
        self.visible = visible

    def update(self):
        # bobbing motion
        if self.visible:
            offset = BOB_RANGE * (self.tween(self.step / BOB_RANGE) - 0.5) # -0.5 since we are starting in middle
            self.rect.centery = self.position.y + offset * self.direction
            self.step += BOB_SPEED
            if self.step > BOB_RANGE:
                self.step = 0
                self.direction *= -1
    
    def pickup(self):
        self.game.player.player_inventory.append(self)
        self.visible = False
        self.position = HIDDEN_ITEM_POSITION
        self.hit_rect.center = HIDDEN_ITEM_POSITION

    def drop(self):
        self.visible = True
        self.position = self.game.player.position + vector(1, 0).rotate(-self.game.player.rotation) * TILESIZE * 2
        self.hit_rect.center = self.position

    def __repr__(self):
        return '<Item {} at ({},{})>'.format(self.type, self.position.x, self.position.y)


class Potion(Item):
    def __init__(self, game, position, name, visible=True):
        Item.__init__(self, game, position, name, visible)
    
    def use(self):
        if self.game.player.health < PLAYER_HEALTH:
            self.game.effect_sounds['health_up'].play()
            self.game.player.add_health(HEALTH_PACK_AMOUNT)
            self.game.player.player_inventory.pop(self.game.player.inventory_idx)
            self.kill()
    
    def __repr__(self):
        return '<Health Potion {} at ({},{})>'.format(self.type, self.position.x, self.position.y)


class Spell(Item):
    def __init__(self, game, position, name, visible=True):
        Item.__init__(self, game, position, name, visible)
    
    def use(self):
        if self.game.player.weapon != 'fire_blast':
            self.game.player.player_inventory.pop(self.game.player.inventory_idx)
            self.game.effect_sounds['spell_pickup'].play()
            self.game.player.weapon = 'fire_blast'
            self.kill()
    
    def __repr__(self):
        return '<Health Potion {} at ({},{})>'.format(self.type, self.position.x, self.position.y)