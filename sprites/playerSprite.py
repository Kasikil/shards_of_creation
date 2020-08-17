####################################################################
#
#
# Shards of Creation -- sprites.playerSprite --
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
    from sprites.castingFlashSprite import CastingFlash
    from sprites.itemSprite import Potion, Spell
    from sprites.projectileSprite import Projectile
    from settings.settings import *
    from settings.npc_settings import *
    from tilemap import collide_hit_rect
    from utilities import collide_with_walls
except ImportError as err:
    print ('Couldn\'t load module. {}'.format(err))
    raise

vector = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    """
    Sprite for the player character
    """
    def __init__(self, game, x, y):
        self._layer = PLAYER_LAYER
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.velocity = vector(0, 0)
        self.position = vector(x, y)
        self.rotation = 0
        self.last_shot = 0
        self.health = PLAYER_HEALTH
        self.weapon = 'vampirism'
        self.damaged = False
        self.busy = False
        self.conversation_partner = None
        self.player_inventory = [Potion(self.game, HIDDEN_ITEM_POSITION, 'health_potion_01', False),
                                 Spell(self.game, HIDDEN_ITEM_POSITION, 'fire_blast_01', False)]
        self.inventory_idx = 0

    def __repr__(self):
        return '<Player Current Weapon {}>'.format(self.weapon)

    def get_keys(self):
        self.rotation_speed = 0
        self.velocity = vector(0, 0)
        keys = pygame.key.get_pressed()
        if not self.busy and not self.game.inventory:
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.rotation_speed = PLAYER_ROTATION_SPEED
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.rotation_speed = -PLAYER_ROTATION_SPEED
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                self.velocity = vector(PLAYER_SPEED, 0).rotate(-self.rotation)
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.velocity = vector(-PLAYER_SPEED / 2, 0).rotate(-self.rotation)
            if keys[pygame.K_SPACE]:
                self.shoot()
            if keys[pygame.K_t]:
                self.talk()
            if keys[pygame.K_e]:
                self.game.inventory = True
        if self.game.inventory:
            self.get_keys_inventory(keys)
        if self.busy and keys[pygame.K_x]:
            self.busy = False
            self.conversation_partner.busy = False
            self.conversation_partner = None

    def get_keys_inventory(self, keys):
        if not self.game.wait_for_up:
            return
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]):
            # Deselect 'examine' view in inventory
            self.game.wait_for_up = False
        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d] or keys[pygame.K_RETURN]):
            # Select 'examine' view in inventory
            self.game.wait_for_up = False
        elif (keys[pygame.K_UP] or keys[pygame.K_w]):
            # Scroll up in the inventory
            if len(self.player_inventory) > 0 and self.inventory_idx > 0:
                self.inventory_idx -= 1
            elif len(self.player_inventory) > 0 and self.inventory_idx == 0:
                self.inventory_idx = len(self.player_inventory) - 1
            else:
                self.inventory_idx = 0
            self.game.wait_for_up = False
        elif (keys[pygame.K_DOWN] or keys[pygame.K_s]):
            # Scroll down in the inventory
            if len(self.player_inventory) > 0 and self.inventory_idx < (len(self.player_inventory) - 1):
                self.inventory_idx += 1
            elif len(self.player_inventory) > 0 and self.inventory_idx == (len(self.player_inventory) - 1):
                self.inventory_idx = 0
            else:
                self.inventory_idx = 0
            self.game.wait_for_up = False
        elif keys[pygame.K_r]:
            self.player_inventory.pop(self.inventory_idx).drop()
            self.game.wait_for_up = False
        elif keys[pygame.K_u]:
            self.player_inventory[self.inventory_idx].use()
            self.game.wait_for_up = False
        elif keys[pygame.K_x]:
            self.game.inventory = False
            self.game.wait_for_up = False

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > WEAPONS[self.weapon]['rate']:
            self.last_shot = now
            direction = vector(1, 0).rotate(-self.rotation)
            position = self.position + PROJECTILE_LAUNCH_OFFSET.rotate(-self.rotation)
            self.velocity += vector(-WEAPONS[self.weapon]['oomf'], 0).rotate(-self.rotation)
            for trashy_coding in range(WEAPONS[self.weapon]['projectile_count']):
                spread = uniform(-WEAPONS[self.weapon]['spread'], WEAPONS[self.weapon]['spread'])
                Projectile(self.game, self.rotation, position, direction.rotate(spread), WEAPONS[self.weapon]['damage'])
                sound = choice(self.game.weapon_sounds[self.weapon])
                if sound.get_num_channels() > 2:
                    sound.stop()
                sound.play()
            CastingFlash(self.game, position)
        
    def talk(self):
        hits = pygame.sprite.spritecollide(self, self.game.npcs, False, collide_hit_rect)
        if hits:
            hits[0].busy = True
            self.busy = True
            self.conversation_partner = hits[0]

    def hit(self):
        self.damaged = True
        self.damage_alpha = chain(DAMAGE_ALPHA * 2)

    def update(self):
        self.get_keys()
        if not self.game.inventory:
            self.rotation = (self.rotation + self.rotation_speed * self.game.dt) % 360
            self.image = pygame.transform.rotate(self.game.player_img, self.rotation)
            if self.damaged:
                try:
                    self.image.fill((255, 0, 0, next(self.damage_alpha)), special_flags=pygame.BLEND_RGBA_MULT)
                except StopIteration:
                    self.damaged = False
            self.rect = self.image.get_rect()
            self.rect.center = self.position
            self.position += self.velocity * self.game.dt
            self.hit_rect.centerx = self.position.x
            collide_with_walls(self, self.game.walls, 'x')
            self.hit_rect.centery = self.position.y
            collide_with_walls(self, self.game.walls, 'y')
            self.rect.center = self.hit_rect.center

    def add_health(self, amount):
        self.health += amount
        if self.health > PLAYER_HEALTH:
            self.health = PLAYER_HEALTH

    def new_map(self, spawn_key):
        """
        This method should only be called after a new map and its objects have been populated.
        """
        for spawn in self.game.spawns:
            if spawn.name == spawn_key:
                self.rect.center = (spawn.x, spawn.y)
                self.position = vector(spawn.x, spawn.y)
        self.hit_rect.center = self.rect.center
        self.velocity = vector(0, 0)




