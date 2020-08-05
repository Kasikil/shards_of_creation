####################################################################
#
#
# [Untitled Game] -- utilities --
# A Fantasy Narrative RPG
# Liscense Here
#
#
####################################################################

try:
    # Standard Python Imports
    import pygame

    # Non-Standard Imports
    from settings.settings import *
    from tilemap import collide_hit_rect
except ImportError as err:
    print ('Couldn\'t load module. {}'.format(err))
    raise

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

# HUD Functions
def draw_player_health(surface, x, y, percentage):
    if percentage < 0:
        percentage = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 20
    fill = percentage * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    if percentage > 0.6:
        color = GREEN
    elif percentage > 0.3:
        color = YELLOW
    else:
        color = RED
    pygame.draw.rect(surface, color, fill_rect)
    pygame.draw.rect(surface, WHITE, outline_rect, 2)