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
                'waypoints': [[0, 128], [224, 128], [224, 0], [0, 0]], # in pixels
                'waysleep': [15], # in seconds
                'dialogue': 0}
NPCS['Corris'] = {'name': 'Corris',
                'image': 'villager001.png',
                'hit_rect': pygame.Rect(0, 0, 30, 30),
                'health': 500,
                'movement_method': 'waypoint',
                'speed': 100,
                'waypoint_system': 'relative', # relative or absolute
                'waypoints': [[96, 0], [96, -96], [160, -96], [64, -64], [0,0]], # in pixels
                'waysleep': [25, 50, 17, 23], # in seconds
                'dialogue': 100}
NPCS['Elsk'] = {'name': 'Elsk',
                'image': 'villager002.png',
                'hit_rect': pygame.Rect(0, 0, 30, 30),
                'health': 500,
                'movement_method': 'waypoint',
                'speed': 100,
                'waypoint_system': 'relative', # relative or absolute
                'waypoints': [[0, -96], [0, 64]], # in pixels
                'waysleep': [7], # in seconds
                'dialogue': 200}
NPCS['Morad'] = {'name': 'Morad',
                'image': 'villager003.png',
                'hit_rect': pygame.Rect(0, 0, 30, 30),
                'health': 500,
                'movement_method': 'waypoint',
                'speed': 100,
                'waypoint_system': 'relative', # relative or absolute
                'waypoints': [[0, -32], [0, 0]], # in pixels
                'waysleep': [2], # in seconds
                'dialogue': 300}
NPCS['Sovik'] = {'name': 'Sovik',
                'image': 'villager001.png',
                'hit_rect': pygame.Rect(0, 0, 30, 30),
                'health': 500,
                'movement_method': 'waypoint',
                'speed': 100,
                'waypoint_system': 'relative', # relative or absolute
                'waypoints': [[0, -32], [0, 0]], # in pixels
                'waysleep': [2], # in seconds
                'dialogue': 400}
NPCS['Tinterbeck'] = {'name': 'Tinterbeck',
                'image': 'villager001.png',
                'hit_rect': pygame.Rect(0, 0, 30, 30),
                'health': 500,
                'movement_method': 'waypoint',
                'speed': 100,
                'waypoint_system': 'relative', # relative or absolute
                'waypoints': [[0, 0]], # in pixels
                'waysleep': [8], # in seconds
                'dialogue': 500}
NPCS['Sivas'] = {'name': 'Sivas',
                'image': 'villager001.png',
                'hit_rect': pygame.Rect(0, 0, 30, 30),
                'health': 500,
                'movement_method': 'waypoint',
                'speed': 100,
                'waypoint_system': 'relative', # relative or absolute
                'waypoints': [[0, 0], [352, 0]], # in pixels
                'waysleep': [5], # in seconds
                'dialogue': 600}
NPCS['Goat'] = {'name': 'Goat',
                'image': 'Goat.png',
                'hit_rect': pygame.Rect(0, 0, 30, 30),
                'health': 500,
                'movement_method': 'waypoint',
                'speed': 100,
                'waypoint_system': 'relative', # relative or absolute
                'waypoints': [[0, 0], [-128, 0], [-128, 128], [0, 128]], # in pixels
                'waysleep': [15], # in seconds
                'dialogue': 700}