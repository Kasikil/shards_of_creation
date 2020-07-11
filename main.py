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
    import sys
    import random
    import math
    import os
    import getopt
    import pygame
    from socket import *
    from pygame.locals import *
except ImportError as err:
    print ('Couldn\'t load module. {}'.format(err))
    sys.exit(2)

WIDTH = 360
HEIGHT = 480
FPS = 30

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

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
        pygame.display.set_caption("Shards of Creation")
        self.clock = pygame.time.Clock()

    def game_loop(self):
        running = True
        while running:
            # keep loop running at the correct speed
            self.clock.tick(FPS)
            # Prcoess input (events)
            for event in pygame.event.get():
                # Check for closing the window *x*
                if event.type == pygame.QUIT:
                    running = False
            # Update

            # Draw / Render
            self.screen.fill(BLACK)
            # ***AFTER*** drawing everything, flip the display
            pygame.display.flip()


game = Game()
game.game_loop()
pygame.quit()