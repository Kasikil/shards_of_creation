####################################################################
#
#
# Shards of Creation -- main --
# A Fantasy Narrative RPG
# Liscense Here
#
#
####################################################################
VERSION = "0.1"

try:
    # Standard Python Imports
    import getopt
    import math
    from os import path
    import pygame    
    from pygame.locals import *
    import random
    from socket import *
    import sys

    # Non-Standard Imports
    from settings import *
    from sprites import *
    from tilemap import *
except ImportError as err:
    print ('Couldn\'t load module. {}'.format(err))
    sys.exit(2)

# HUD Functions
def draw_player_health(surface, x, y, percentage):
    if percentage < 0:
        percentage = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 20
    fill = percentage * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    if percentage > 0.6:
        color = GREEN
    elif percentage > 0.3:
        color = YELLOW
    else:
        color = RED
    pygame.draw.rect(surface, color, fill_rect)
    pygame.draw.rect(surface, WHITE, outline_rect, 2)

class Game():
    """
    This class is the main game loop as well as the 
    associated methods and variables for running 
    this loop.
    """

    def __init__(self):
        """
        Initializes pygame and create game window
        """
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(500, 100)
        self.load_data()
        self.draw_debug = False

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        assets_folder = path.join(game_folder, 'assets')
        self.map = TiledMap(path.join(assets_folder, 'map.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.player_img = pygame.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
        self.projectile_img = pygame.image.load(path.join(img_folder, PROJECTILE_IMG)).convert_alpha()
        self.mob_img = pygame.image.load(path.join(img_folder, MOB_IMG)).convert_alpha()
        self.wall_img = pygame.image.load(path.join(img_folder, WALL_IMG)).convert_alpha()
        self.wall_img = pygame.transform.scale(self.wall_img, (TILESIZE, TILESIZE))
        self.casting_flashes = []
        for img in CASTING_FLASH:
            self.casting_flashes.append(pygame.image.load(path.join(img_folder, img)).convert_alpha())
        self.item_images = {}
        for item in ITEM_IMAGES:
            self.item_images[item] = pygame.image.load(path.join(img_folder, ITEM_IMAGES[item])).convert_alpha()

    def new(self):
        """
        Initializes all variables and do all the setup for a new game
        """
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.walls = pygame.sprite.Group()
        self.mobs = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        
        for tile_object in self.map.tmxdata.objects:
            obj_center = vector(tile_object.x + tile_object.width / 2,
                                tile_object.y + tile_object.height / 2)
            if tile_object.name == 'player':
                self.player = Player(self, obj_center.x, obj_center.y)
            if tile_object.name == 'mob':
                Mob(self, obj_center.x, obj_center.y)
            if tile_object.name == 'wall':
                Obstacle(self, tile_object.x, tile_object.y, 
                tile_object.width, tile_object.height)
            if tile_object.name in ['health']:
                Item(self, obj_center, tile_object.name)
        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        """
        Update portion of the game loop
        """
        self.all_sprites.update()
        self.camera.update(self.player)
        # player hits items
        hits = pygame.sprite.spritecollide(self.player, self.items, False)
        for hit in hits:
            if hit.type == 'health' and self.player.health < PLAYER_HEALTH:
                hit.kill()
                self.player.add_health(HEALTH_PACK_AMOUNT)

        # mobs hits player
        hits = pygame.sprite.spritecollide(self.player, self.mobs, False, collide_hit_rect)
        for hit in hits:
            self.player.health -= MOB_DAMAGE
            hit.velocity = vector(0, 0)
            if self.player.health <= 0:
                self.playing = False
        if hits:
            self.player.position += vector(MOB_KNOCKBACK, 0).rotate(-hits[0].rotation)
        # projectiles hit mobs
        hits = pygame.sprite.groupcollide(self.mobs, self.projectiles, False, True)
        for hit in hits:
            hit.health -= PROJECTILE_DAMAGE
            hit.velocity = vector(0, 0)

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        """
        Draw portion of the game loop
        """
        if DEBUG:
            pygame.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        # self.screen.fill(BGCOLOR)
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        # self.draw_grid()
        for sprite in self.all_sprites:
            if isinstance(sprite, Mob):
                sprite.draw_health()
            self.screen.blit(sprite.image, self.camera.apply(sprite))
            if self.draw_debug:
                pygame.draw.rect(self.screen, CYAN, self.camera.apply_rect(sprite.hit_rect), 1)
        if self.draw_debug:
            for wall in self.walls:
                pygame.draw.rect(self.screen, CYAN, self.camera.apply_rect(wall.rect), 1)

        # pygame.draw.rect(self.screen, WHITE, self.player.hit_rect, 2)
        # Always last in drawing "flip"
        # HUD functions
        draw_player_health(self.screen, 10, 10, self.player.health / PLAYER_HEALTH)
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            # Check for closing the window *x*
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                if event.key == pygame.K_h and DEBUG:
                    self.draw_debug = not self.draw_debug

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass


game = Game()
game.show_start_screen()
while True:
    game.new()
    game.run()