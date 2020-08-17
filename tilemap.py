####################################################################
#
#
# Shards of Creation -- tilemap --
# A Fantasy Narrative RPG
# Liscense Here
#
#
####################################################################

try:
    # Standard Python Imports
    import os
    import pygame
    import pytmx
    import pyscroll

    # Non-Standard Imports
    from settings.settings import HEIGHT, WIDTH
except ImportError as err:
    print ('Couldn\'t load module. {}'.format(err))
    raise

def collide_hit_rect(one, two):
    return one.hit_rect.colliderect(two.rect)

def apply_rect(rect, x, y):
        return rect.move(x, y)

def apply(entity, x, y):
    return entity.rect.move(x, y)
