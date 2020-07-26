####################################################################
#
#
# Shards of Creation -- sprites --
# A Fantasy Narrative RPG
# Liscense Here
#
#
####################################################################

try:
    # Standard Python Imports
    import os
    import pygame
    import sys

    # Non-Standard Imports
    from settings import *
    from tilemap import collide_hit_rect
except ImportError as err:
    print ('Couldn\'t load module. {}'.format(err))
    raise

vector = pygame.math.Vector2

# Set up assests folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

class Player(pygame.sprite.Sprite):
    """
    Sprite for the player character
    """
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.velocity = vector(0, 0)
        self.position = vector(x, y) * TILESIZE
        self.rotation = 0

    def get_keys(self):
        self.rotation_speed = 0
        self.velocity = vector(0, 0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rotation_speed = PLAYER_ROTATION_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rotation_speed = -PLAYER_ROTATION_SPEED
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.velocity = vector(PLAYER_SPEED, 0).rotate(-self.rotation)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.velocity = vector(-PLAYER_SPEED / 2, 0).rotate(-self.rotation)

    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False, collide_hit_rect)
            if hits:
                if self.velocity.x > 0:
                    self.position.x = hits[0].rect.left - self.hit_rect.width / 2
                if self.velocity.x < 0:
                    self.position.x = hits[0].rect.right + self.hit_rect.width / 2
                self.velocity.x = 0
                self.hit_rect.centerx = self.position.x
        if dir == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False, collide_hit_rect)
            if hits:
                if self.velocity.y > 0:
                    self.position.y = hits[0].rect.top - self.hit_rect.height / 2
                if self.velocity.y < 0:
                    self.position.y = hits[0].rect.bottom + self.hit_rect.height / 2
                self.velocity.y = 0
                self.hit_rect.centery = self.position.y

    def update(self):
        self.get_keys()
        self.rotation = (self.rotation + self.rotation_speed * self.game.dt) % 360
        self.image = pygame.transform.rotate(self.game.player_img, self.rotation)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.position += self.velocity * self.game.dt
        self.hit_rect.centerx = self.position.x
        self.collide_with_walls('x')
        self.hit_rect.centery = self.position.y
        self.collide_with_walls('y')
        self.rect.center = self.hit_rect.center


class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE