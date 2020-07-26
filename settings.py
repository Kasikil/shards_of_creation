####################################################################
#
#
# Shards of Creation -- settings --
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

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Game Settings
WIDTH = 1024 # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 512 # 16 * 32 or 32 * 16 or 64 * 8
FPS = 60
TITLE = 'Shards of Creation'
BGCOLOR = DARKGREY

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Player Settings
PLAYER_SPEED = 300
PLAYER_ROTATION_SPEED = 250 # degress/second
PLAYER_IMG = 'elephant.png'
PLAYER_HIT_RECT = pygame.Rect(0, 0, 35, 35)