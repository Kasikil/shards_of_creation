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
except ImportError as err:
    print ('Couldn\'t load module. {}'.format(err))
    raise

vector = pygame.math.Vector2

class Link():
    def __init__(self, next_map, spawn_object, rotation=None):
        self.next_map = next_map
        self.spawn_object = spawn_object
        self.rotation = rotation

    def __repr__(self):
        return '<Link to map: {} \nat spawn location{}>'.format(self.next_map, self.spawn_object)


MAP_PORTALS = {
    'monestary': {
        'front_door': Link('world_000001', 'monestary_front_door'),
        'garden_door': Link('world_000001', 'monestary_garden_door')
    },
    'tinterbeck_home': {
        'front_door': Link('world_000001', 'taize_village_tinterbeck_home')
    },
    'sovik_home': {
        'front_door': Link('world_000001', 'taize_village_sovik_home')
    },
    'corris_home': {
        'front_door': Link('world_000001', 'taize_village_corris_home')
    },
    'elsk_home': {
        'front_door': Link('world_000001', 'taize_village_elsk_home')
    },
    'morad_home': {
        'front_door': Link('world_000001', 'taize_village_morad_home')
    },
    'world_000001': {
        'monestary_front_door': Link('monestary', 'front_door'),
        'monestary_garden_door': Link('monestary', 'garden_door'),
        'taize_village_tinterbeck_home': Link('tinterbeck_home', 'front_door'),
        'taize_village_sovik_home': Link('sovik_home', 'front_door'),
        'taize_village_corris_home': Link('corris_home', 'front_door'),
        'taize_village_elsk_home': Link('elsk_home', 'front_door'),
        'taize_village_morad_home': Link('morad_home', 'front_door')
    }
}