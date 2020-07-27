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

vector = pygame.math.Vector2

# Debug Settings
DEBUG = True

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)

# Game Settings
WIDTH = 1024 # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 512 # 16 * 32 or 32 * 16 or 64 * 8
FPS = 60
TITLE = 'Shards of Creation'
BGCOLOR = BROWN

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Wall Settings
WALL_IMG = 'stone2_gray3.png'

# Mob Settings
MOB_IMG = 'maurice_flip.png'
MOB_SPEED = 150
MOB_HIT_RECT = pygame.Rect(0, 0, 35, 35)
MOB_HEALTH = 100
MOB_DAMAGE = 10
MOB_KNOCKBACK = 20

# Projectile Settings
PROJECTILE_IMG = 'i-vampiricism.png'
PROJECTILE_SPEED = 500
PROJECTILE_LIFETIME = 1000 # ms
PROJECTILE_RATE = 150
PROJECTILE_OOMF = 200
PROJECTILE_SPREAD = 5
PROJECTILE_DAMAGE = 10

# Player Settings
PLAYER_HEALTH = 100
PLAYER_SPEED = 300
PLAYER_ROTATION_SPEED = 250 # degress/second
PLAYER_IMG = 'elephant.png'
PLAYER_HIT_RECT = pygame.Rect(0, 0, 30, 30)
PROJECTILE_LAUNCH_OFFSET = vector(15, 5)