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
    from random import uniform
    import sys

    # Non-Standard Imports
    from settings import *
    from tilemap import collide_hit_rect
except ImportError as err:
    print ('Couldn\'t load module. {}'.format(err))
    raise

vector = pygame.math.Vector2

def collide_with_walls(sprite, group, dir):
    if dir == 'x':
        hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centerx > sprite.hit_rect.centerx:
                sprite.position.x = hits[0].rect.left - sprite.hit_rect.width / 2
            if hits[0].rect.centerx < sprite.hit_rect.centerx:
                sprite.position.x = hits[0].rect.right + sprite.hit_rect.width / 2
            sprite.velocity.x = 0
            sprite.hit_rect.centerx = sprite.position.x
    if dir == 'y':
        hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centery > sprite.hit_rect.centery:
                sprite.position.y = hits[0].rect.top - sprite.hit_rect.height / 2
            if hits[0].rect.centery < sprite.hit_rect.centery:
                sprite.position.y = hits[0].rect.bottom + sprite.hit_rect.height / 2
            sprite.velocity.y = 0
            sprite.hit_rect.centery = sprite.position.y

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
        self.position = vector(x, y)
        self.rotation = 0
        self.last_shot = 0
        self.health = PLAYER_HEALTH

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
        if keys[pygame.K_SPACE]:
            now = pygame.time.get_ticks()
            if now - self.last_shot > PROJECTILE_RATE:
                self.last_shot = now
                direction = vector(1, 0).rotate(-self.rotation)
                position = self.position + PROJECTILE_LAUNCH_OFFSET.rotate(-self.rotation)
                Projectile(self.game, self.rotation, position, direction)
                self.velocity += vector(-PROJECTILE_OOMF, 0).rotate(-self.rotation)


    def update(self):
        self.get_keys()
        self.rotation = (self.rotation + self.rotation_speed * self.game.dt) % 360
        self.image = pygame.transform.rotate(self.game.player_img, self.rotation)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.position += self.velocity * self.game.dt
        self.hit_rect.centerx = self.position.x
        collide_with_walls(self, self.game.walls, 'x')
        self.hit_rect.centery = self.position.y
        collide_with_walls(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center


class Mob(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.mob_img
        self.rect = self.image.get_rect()
        self.hit_rect = MOB_HIT_RECT.copy()
        self.hit_rect.center = self.rect.center
        self.position = vector(x, y)
        self.velocity = vector(0, 0)
        self.acceleration = vector(0, 0)
        self.rect.center = self.position
        self.rotation = 0
        self.health = MOB_HEALTH

    def update(self):
        self.rotation = (self.game.player.position - self.position).angle_to(vector(1, 0))
        self.image = pygame.transform.rotate(self.game.mob_img, self.rotation)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.acceleration = vector(MOB_SPEED, 0).rotate(-self.rotation)
        self.acceleration += self.velocity * -1
        self.velocity += self.acceleration * self.game.dt
        self.position += self.velocity * self.game.dt * 0.5 + self.acceleration * self.game.dt ** 2
        self.hit_rect.centerx = self.position.x
        collide_with_walls(self, self.game.walls, 'x')
        self.hit_rect.centery = self.position.y
        collide_with_walls(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center
        if self.health <= 0:
            self.kill()

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


class Projectile(pygame.sprite.Sprite):
    def __init__(self, game, rotation, position, direction):
        self.groups = game.all_sprites, game.projectiles
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rotation = rotation
        self.image = game.projectile_img
        self.image = pygame.transform.rotate(self.game.projectile_img, self.rotation)
        self.rect = self.image.get_rect()
        self.hit_rect = self.rect
        self.position = vector(position)
        self.rect.center = position
        spread = uniform(-PROJECTILE_SPREAD, PROJECTILE_SPREAD)
        self.velocity = direction.rotate(spread) * PROJECTILE_SPEED
        self.spawn_time = pygame.time.get_ticks()

    def update(self):
        self.position += self.velocity * self.game.dt
        self.rect.center = self.position
        if pygame.sprite.spritecollideany(self, self.game.walls):
            self.kill()
        if pygame.time.get_ticks() - self.spawn_time > PROJECTILE_LIFETIME:
            self.kill()


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, game, x, y, width, height):
        self.groups = game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y