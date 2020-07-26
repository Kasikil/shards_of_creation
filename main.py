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

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        game_folder = path.join(game_folder, 'assets')
        self.map = Map(path.join(game_folder, 'map2.txt'))
        self.player_img = pygame.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
        self.mob_img = pygame.image.load(path.join(img_folder, MOB_IMG)).convert_alpha()
        self.wall_img = pygame.image.load(path.join(img_folder, WALL_IMG)).convert_alpha()
        self.wall_img = pygame.transform.scale(self.wall_img, (TILESIZE, TILESIZE))

    def new(self):
        """
        Initializes all variables and do all the setup for a new game
        """
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.mobs = pygame.sprite.Group()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'M':
                    Mob(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
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
        self.screen.fill(BGCOLOR)
        # self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        # pygame.draw.rect(self.screen, WHITE, self.player.hit_rect, 2)
        # Always last in drawing "flip"
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            # Check for closing the window *x*
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass


game = Game()
game.show_start_screen()
while True:
    game.new()
    game.run()