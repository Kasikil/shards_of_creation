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
LOGO_IMG = 'logo.png'
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
DIALOGUE_TEXT_X = DIALOGUE_BOX_X + DIALOGUE_BOX_OUTLINE + DIALOGUE_BUFFER
DIALOGUE_TEXT_Y = DIALOGUE_BOX_Y + DIALOGUE_BOX_OUTLINE + DIALOGUE_BUFFER
DIALOGUE_FONT_SIZE = 12
DIALOGUE_ALLOWED_WIDTH = WIDTH - DIALOGUE_TEXT_X
DIALOGUE_LINE_SPACING = 1

# Inventory
INVENTORY_BOX_HEIGHT = TILESIZE * 12
INVENTORY_BOX_WIDTH = TILESIZE * 12
INVENTORY_BOX_X = WIDTH / 2 - INVENTORY_BOX_WIDTH / 2
INVENTORY_BOX_Y = HEIGHT / 2 - INVENTORY_BOX_HEIGHT / 2
INVENTORY_BOX_OUTLINE = 2
INVENTORY_TEXT_BUFFER = 2
INVENTORY_BUFFER = 12
INVENTORY_TEXT_X = INVENTORY_BOX_X + INVENTORY_BOX_OUTLINE + INVENTORY_BUFFER
INVENTORY_TEXT_Y = INVENTORY_BOX_Y + INVENTORY_BOX_OUTLINE + INVENTORY_BUFFER
INVENTORY_FONT_SIZE = 16
INVENTORY_ALLOWED_WIDTH = (INVENTORY_BOX_WIDTH / 2) - 2 * INVENTORY_BOX_OUTLINE
INVENTORY_LINE_SPACING = 3
INVENTORY_SELECTION_OUTLINE = 1
INVENTORY_IMAGE_X = INVENTORY_TEXT_X + INVENTORY_BOX_WIDTH / 2
INVENTORY_IMAGE_Y = INVENTORY_TEXT_Y

# Mob Settings
MOB_IMG = 'shade.png'
MOB_SPLAT = 'shade_splat.png'
MOB_SPEEDS = [150, 100, 75, 125]
MOB_HIT_RECT = pygame.Rect(0, 0, 35, 35)
MOB_HEALTH = 100
MOB_DAMAGE = 10
MOB_KNOCKBACK = 20
AVOID_RADIUS = 50
DETECT_RADIUS = 200

# Weapon Settings
PROJECTILE_IMG = 'FireBlast.png'
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
PLAYER_IMG = 'player.png'
PLAYER_HIT_RECT = pygame.Rect(0, 0, 25, 25)
PROJECTILE_LAUNCH_OFFSET = vector(15, 5)

# Effects
CASTING_FLASH = ['CastingEffect0.png', 'CastingEffect1.png']
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
POTION_ITEMS = {}
POTION_ITEMS['health_potion_01'] = {'image': 'HealthPotion.png',
                                    'name': 'Standard Health Potion',
                                    'details': 'This potion will restore 20 points of health when used. It has a single use and then will disappear. This potion cannot be used when health is already full.',
                                    'health_value': 20}
POTION_ITEMS['health_potion_02'] = {'image': 'HealthPotion.png',
                                    'name': 'Moderate Health Potion',
                                    'details': 'This potion will restore 40 points of health when used. It has a single use and then will disappear. This potion cannot be used when health is already full.',
                                    'health_value': 40}
SPELL_ITEMS = {}
SPELL_ITEMS['fire_blast_01'] = {'image': 'FireSpell.png',
                                'name': 'Fire Blast',
                                'details': 'Activating this spell will cause a fire spray to originate when you cast. More damage will be done cumilatively, but each spell projectile will cause less damage. This spell cannot be used if your current spell is already set to fire spell.'}
BOB_RANGE = 15
BOB_SPEED = 0.4
HIDDEN_ITEM_POSITION = vector(10000, 10000)

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
