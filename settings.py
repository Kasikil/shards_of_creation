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
CYAN = (0, 255, 255)

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
MOB_SPEEDS = [150, 100, 75, 125]
MOB_HIT_RECT = pygame.Rect(0, 0, 35, 35)
MOB_HEALTH = 100
MOB_DAMAGE = 10
MOB_KNOCKBACK = 20
AVOID_RADIUS = 50
DETECT_RADIUS = 200

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

# Effects
CASTING_FLASH = ['cloud_magic_trail0.png', 'cloud_magic_trail1.png', 
'cloud_magic_trail2.png', 'cloud_magic_trail3.png']
FLASH_DURATION = 40

# Layers
WALL_LAYER = 1
ITEMS_LAYER = 1
PLAYER_LAYER = 2
MOB_LAYER = 2
PROJECTILE_LAYER = 3
EFFECTS_LAYER = 4

# Items
ITEM_IMAGES = {'health': 'health_potion.png'}
HEALTH_PACK_AMOUNT = 20
BOB_RANGE = 15
BOB_SPEED = 0.4

# Sounds
BACKGROUND_MUSIC = 'Ketsa_-_08_-_Multiverse.mp3'
PLAYER_HIT_SOUNDS = ['elephant.wav']
MOB_STANDARD_SOUNDS = ['shade1.wav', 'shade2.wav', 'shade3.wav', 'shade4.wav', 'shade5.wav']
MOB_HIT_SOUNDS = ['shade14.wav']
CASTING_SOUNDS_VAMPIRISM = ['vampiristic_kiss.wav']
EFFECTS_SOUNDS = {'level_start': 'spell.wav', 'health_up': 'bottle.wav'}
