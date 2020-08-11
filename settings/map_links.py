####################################################################
#
#
# Shards of Creation -- settings.map_links.py --
# A Fantasy Narrative RPG
# Liscense Here
#
#
####################################################################

try:
    # Standard Python Imports
    import pygame

    # Non-Standard Imports
    from settings.settings import TILESIZE
except ImportError as err:
    print ('Couldn\'t load module. {}'.format(err))
    raise

vector = pygame.math.Vector2

class Link():
    def __init__(self, next_map, position_x, position_y, rotation=None):
        self.next_map = next_map
        self.position = vector(position_x * TILESIZE, position_y * TILESIZE)
        self.rotation = rotation

    def __repr__(self):
        return '<Link to {} at ({},{})>'.format(self.next_map, self.position.x, self.position.y)


MAP_PORTALS = {
    'monestary': {
        'front_door': Link('world_000001', 25, 25),
        'garden_door': Link('world_000001', 40, 40)
    },
    'world_000001': {
        'monestary_front_door': Link('monestary', 262.5, 818.5),  # Assuming rect.center
        'monestary_garden_door': Link('monestary', 293.5, 792.5)  # Assuming rect.center
    }
}