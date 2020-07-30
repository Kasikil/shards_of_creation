####################################################################
#
#
# Shards of Creation -- settings.settings --
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

# Title
PAUSE_FONT_SIZE = 50
GAME_OVER_FONT_SIZE = 100
GAME_OVER_SUB_FONT_SIZE = 75

# HUD
HUD_FONT_SIZE = 30

# Dialogue Box
DIALOGUE_BOX_HEIGHT = TILESIZE * 2
DIALOGUE_BOX_WIDTH = TILESIZE * 6
DIALOGUE_BOX_X = WIDTH - DIALOGUE_BOX_WIDTH
DIALOGUE_BOX_Y = HEIGHT - DIALOGUE_BOX_HEIGHT
DIALOGUE_BOX_OUTLINE = 2
DIALOGUE_BUFFER = 2
DIALOGUE_TEXT_X = WIDTH - DIALOGUE_BOX_WIDTH + DIALOGUE_BOX_OUTLINE + DIALOGUE_BUFFER
DIALOGUE_TEXT_Y = HEIGHT - DIALOGUE_BOX_HEIGHT + DIALOGUE_BOX_OUTLINE + DIALOGUE_BUFFER
DIALOGUE_FONT_SIZE = 12
DIALOGUE_ALLOWED_WIDTH = WIDTH - DIALOGUE_TEXT_X

# Mob Settings
MOB_IMG = 'maurice_flip.png'
MOB_SPLAT = 'shade_splat.png'
MOB_SPEEDS = [150, 100, 75, 125]
MOB_HIT_RECT = pygame.Rect(0, 0, 35, 35)
MOB_HEALTH = 100
MOB_DAMAGE = 10
MOB_KNOCKBACK = 20
AVOID_RADIUS = 50
DETECT_RADIUS = 200

# Weapon Settings
PROJECTILE_IMG = 'i-vampiricism.png'
WEAPONS = {}
WEAPONS['vampirism'] = {'projectile_speed': 500,
                        'projectile_lifetime': 1000,
                        'rate': 250,
                        'oomf': 200,
                        'spread': 5,
                        'damage': 10,
                        'projectile_size': 'lg',
                        'projectile_count': 1}

WEAPONS['fire_blast'] = {'projectile_speed': 400,
                        'projectile_lifetime': 500,
                        'rate': 900,
                        'oomf': 300,
                        'spread': 20,
                        'damage': 5,
                        'projectile_size': 'sm',
                        'projectile_count': 12}

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
DAMAGE_ALPHA = [alpha for alpha in range(0, 255, 25)]
NIGHT_COLOR = (20, 20, 20)
LIGHT_RADIUS = (500, 500)
LIGHT_MASK = 'light_350_med.png'

# Layers
WALL_LAYER = 1
ITEMS_LAYER = 1
PLAYER_LAYER = 2
MOB_LAYER = 2
NPC_LAYER = 2
PROJECTILE_LAYER = 3
EFFECTS_LAYER = 4

# Items
ITEM_IMAGES = {'health': 'health_potion.png',
               'fire_blast': 'fire_blast.png'}
HEALTH_PACK_AMOUNT = 20
BOB_RANGE = 15
BOB_SPEED = 0.4

# Sounds
BACKGROUND_MUSIC = 'Ketsa_-_08_-_Multiverse.mp3'
PLAYER_HIT_SOUNDS = ['elephant.wav']
MOB_STANDARD_SOUNDS = ['shade1.wav', 'shade2.wav', 'shade3.wav', 'shade4.wav', 'shade5.wav']
MOB_HIT_SOUNDS = ['shade14.wav']
CASTING_SOUNDS = {'vampirism': ['vampiristic_kiss.wav'],
                  'fire_blast': ['Fireball.wav']}
EFFECTS_SOUNDS = {'level_start': 'spell.wav', 
                  'health_up': 'bottle.wav',
                  'spell_pickup': 'spell_pickup.wav'}
