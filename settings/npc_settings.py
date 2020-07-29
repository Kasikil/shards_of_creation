####################################################################
#
#
# Shards of Creation -- settings.npc_settings --
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

NPCS = {}
NPCS['Zuan'] = {'name': 'Zuan',
                'image': 'Zuan.png',
                'hit_rect': pygame.Rect(0, 0, 30, 30),
                'health': 500,
                'movement_method': 'waypoint',
                'speed': 100,
                'waypoint_system': 'relative', # relative or absolute
                'waypoints': [[0, 128], [128, 128], [128, 0], [0, 0]],
                'waysleep': [4000],
                'dialogue': ''}