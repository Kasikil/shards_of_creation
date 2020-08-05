####################################################################
#
#
# [Untitled Game] -- main --
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
    from random import choice, random
    from socket import *
    import sys

    # Non-Standard Imports
    from settings.settings import *
    from settings.npc_settings import *
    from sprites.itemSprite import Item, Potion, Spell
    from sprites.mobSprite import Mob
    from sprites.npcSprite import Npc
    from sprites.obstacleSprite import Obstacle
    from sprites.playerSprite import Player
    from tilemap import *
    from utilities import draw_player_health
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
        pygame.mixer.pre_init(44100, -16, 1, 2048) # Last value (buffer size) increased to decrease delay in playing
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(500, 100)
        self.load_data()
        self.draw_debug = False
        self.wait_for_up = False

    def draw_text(self, text, font, color, x, y, align="nw"):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if align == 'nw':
            text_rect.topleft = (x, y)
        if align == 'ne':
            text_rect.topright = (x, y)
        if align == 'sw':
            text_rect.bottomleft = (x, y)
        if align == 'se':
            text_rect.bottomright = (x, y)
        if align == 'n':
            text_rect.midtop = (x, y)
        if align == 's':
            text_rect.midbottom = (x, y)
        if align == 'e':
            text_rect.midright = (x, y)
        if align == 'w':
            text_rect.midleft = (x, y)
        if align == 'center':
            text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    def load_data(self):
        self.load_folders()
        self.load_fonts()
        self.load_dim()
        self.load_images()
        self.load_sound()
        self.load_dialogue()

    def load_folders(self):
        self.game_folder = path.dirname(__file__)
        self.assets_folder = path.join(self.game_folder, 'assets')
        self.img_folder = path.join(self.game_folder, 'img')
        self.npc_img_folder = path.join(self.img_folder, 'npcs')
        self.sound_folder = path.join(self.game_folder, 'sound')
        self.music_folder = path.join(self.game_folder, 'music')
        self.dialogue = path.join(self.assets_folder, 'dialogue_scripts')
    
    def load_fonts(self):
        self.title_font_file = path.join(self.assets_folder, 'ENDOR.TTF')
        self.game_over_font = pygame.font.Font(self.title_font_file, GAME_OVER_FONT_SIZE)
        self.game_over_sub_font = pygame.font.Font(self.title_font_file, GAME_OVER_SUB_FONT_SIZE)
        self.pause_font = pygame.font.Font(self.title_font_file, PAUSE_FONT_SIZE)
        self.hud_font_file = path.join(self.assets_folder, 'RINGM.TTF')
        self.hud_font = pygame.font.Font(self.hud_font_file, HUD_FONT_SIZE)
        self.dialogue_font_file = path.join(self.assets_folder, 'arial.TTF')
        self.dialogue_font = pygame.font.Font(self.dialogue_font_file, DIALOGUE_FONT_SIZE)
        self.inventory_item_font = pygame.font.Font(self.dialogue_font_file, INVENTORY_FONT_SIZE)
        fw, fh = self.inventory_item_font.size('Inventory')
        self.inventory_item_font_height = fh
    
    def load_dim(self):
        self.dim_screen = pygame.Surface(self.screen.get_size()).convert_alpha()
        self.dim_screen.fill((0, 0, 0, 180))

    def load_images(self):
        self.player_img = pygame.image.load(path.join(self.img_folder, PLAYER_IMG)).convert_alpha()
        self.projectile_images = {}
        self.projectile_images['lg'] = pygame.image.load(path.join(self.img_folder, PROJECTILE_IMG)).convert_alpha()
        self.projectile_images['sm'] = pygame.transform.scale(self.projectile_images['lg'], (10, 10))
        self.mob_img = pygame.image.load(path.join(self.img_folder, MOB_IMG)).convert_alpha()
        self.splat = pygame.image.load(path.join(self.img_folder, MOB_SPLAT)).convert_alpha()
        self.splat = pygame.transform.scale(self.splat, (TILESIZE, TILESIZE))
        self.casting_flashes = []
        for img in CASTING_FLASH:
            self.casting_flashes.append(pygame.image.load(path.join(self.img_folder, img)).convert_alpha())
        self.item_images = {}
        for item in POTION_ITEMS:
            self.item_images[item] = pygame.image.load(path.join(self.img_folder, POTION_ITEMS[item]['image'])).convert_alpha()
        for item in SPELL_ITEMS:
            self.item_images[item] = pygame.image.load(path.join(self.img_folder, SPELL_ITEMS[item]['image'])).convert_alpha()
        self.npc_images = {}
        for npc in NPCS:
            self.npc_images[NPCS[npc]['name']] = pygame.image.load(path.join(self.npc_img_folder, NPCS[npc]['image'])).convert_alpha()
        
        # lighting effect
        self.fog = pygame.Surface((WIDTH, HEIGHT))
        self.fog.fill(NIGHT_COLOR)
        self.light_mask = pygame.image.load(path.join(self.img_folder, LIGHT_MASK)).convert_alpha()
        self.light_mask = pygame.transform.scale(self.light_mask, LIGHT_RADIUS)
        self.light_rect = self.light_mask.get_rect()

    def load_sound(self):
        # Sound Loading
        pygame.mixer.music.load(path.join(self.music_folder, BACKGROUND_MUSIC))
        self.effect_sounds = {}
        for sounds in EFFECTS_SOUNDS:
            self.effect_sounds[sounds] = pygame.mixer.Sound(path.join(self.sound_folder, EFFECTS_SOUNDS[sounds]))
        self.weapon_sounds = {}
        for casting in CASTING_SOUNDS:
            self.weapon_sounds[casting] = []
            for sound in CASTING_SOUNDS[casting]:
                s = pygame.mixer.Sound(path.join(self.sound_folder, sound))
                s.set_volume(0.3)
                self.weapon_sounds[casting].append(s)
        self.mob_standard_sounds = []
        for sound in MOB_STANDARD_SOUNDS:
            s = pygame.mixer.Sound(path.join(self.sound_folder, sound))
            s.set_volume(1) # Range of 1 - full original to 0 - mute
            self.mob_standard_sounds.append(s)
        self.player_hit_sounds = []
        for sound in PLAYER_HIT_SOUNDS:
            self.player_hit_sounds.append(pygame.mixer.Sound(path.join(self.sound_folder, sound)))
        self.mob_hit_sounds = []
        for sound in MOB_HIT_SOUNDS:
            self.mob_hit_sounds.append(pygame.mixer.Sound(path.join(self.sound_folder, sound)))

    def load_dialogue(self):
        pass

    def new(self):
        """
        Initializes all variables and do all the setup for a new game
        """
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.walls = pygame.sprite.Group()
        self.mobs = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.npcs = pygame.sprite.Group()

        self.map = TiledMap(path.join(self.assets_folder, 'map.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        # Create Boxes Associated With Text Display
        self.dialogue_box = pygame.Rect(DIALOGUE_BOX_X, DIALOGUE_BOX_Y, DIALOGUE_BOX_WIDTH, DIALOGUE_BOX_HEIGHT)
        self.inventory_tab = pygame.Rect(INVENTORY_BOX_X, INVENTORY_BOX_Y - self.inventory_item_font_height - INVENTORY_BOX_OUTLINE, INVENTORY_BOX_WIDTH, self.inventory_item_font_height)
        self.inventory_box = pygame.Rect(INVENTORY_BOX_X, INVENTORY_BOX_Y, INVENTORY_BOX_WIDTH, INVENTORY_BOX_HEIGHT)
        self.inventory_selection_box = pygame.Rect(INVENTORY_BOX_X, INVENTORY_BOX_Y, INVENTORY_ALLOWED_WIDTH, self.inventory_item_font_height)

        for tile_object in self.map.tmxdata.objects:
            obj_center = vector(tile_object.x + tile_object.width / 2,
                                tile_object.y + tile_object.height / 2)
            if tile_object.name == 'player':
                self.player = Player(self, obj_center.x, obj_center.y)
            if tile_object.name == 'mob':
                Mob(self, obj_center.x, obj_center.y)
            if tile_object.name == 'npc':
                Npc(self, obj_center.x, obj_center.y, tile_object.type)
            if tile_object.name == 'wall':
                Obstacle(self, tile_object.x, tile_object.y, 
                tile_object.width, tile_object.height)
            if tile_object.name in POTION_ITEMS:
                Potion(self, obj_center, tile_object.name)
            if tile_object.name in SPELL_ITEMS:
                Spell(self, obj_center, tile_object.name)
        self.camera = Camera(self.map.width, self.map.height)
        self.paused = False
        self.night = False
        self.inventory = False
        self.effect_sounds['level_start'].play()

    def run(self):
        self.playing = True
        pygame.mixer.music.play(loops=-1)
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            if not self.paused and not self.inventory:
                self.update()
            elif self.inventory and not self.paused:
                self.player.update()
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
            if hit.visible:
                hit.pickup()
        # mobs hits player
        hits = pygame.sprite.spritecollide(self.player, self.mobs, False, collide_hit_rect)
        for hit in hits:
            if random() < 0.7:
                choice(self.player_hit_sounds).play()
            self.player.health -= MOB_DAMAGE
            hit.velocity = vector(0, 0)
            if self.player.health <= 0:
                self.playing = False
        if hits:
            self.player.hit()
            self.player.position += vector(MOB_KNOCKBACK, 0).rotate(-hits[0].rotation)

        # projectiles hit mobs
        hits = pygame.sprite.groupcollide(self.mobs, self.projectiles, False, True)
        for mob in hits:
            for projectile in hits[mob]:
                mob.health -= projectile.damage
            mob.velocity = vector(0, 0)

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def render_fog(self):
        # draw the light mask (gradient) onto fog image
        self.fog.fill(NIGHT_COLOR)
        self.light_rect.center = self.camera.apply(self.player).center
        self.fog.blit(self.light_mask, self.light_rect)
        self.screen.blit(self.fog, (0, 0), special_flags=pygame.BLEND_MULT)

    def draw_wrapped_text(self, text, font, color, x, y, allowed_width, line_spacing):
        words = text.split()
        lines = []
        while len(words) > 0:
            line_words = []
            while len(words) > 0:
                line_words.append(words.pop(0))
                fw, fh = font.size(' '.join(line_words + words[:1]))
                if fw > allowed_width:
                    break
            line = ' '.join(line_words)
            lines.append(line)
        y_offset = 0
        for line in lines:
            fw, fh = font.size(line)
            ty = y + y_offset
            self.draw_text(line, font, 
                           color, x, ty)
            y_offset += fh + line_spacing

    def draw_dialogue_box(self):
        pygame.draw.rect(self.screen, BLACK, self.dialogue_box)
        pygame.draw.rect(self.screen, WHITE, self.dialogue_box, DIALOGUE_BOX_OUTLINE)
        if self.player.busy and self.player.conversation_partner:
            self.draw_wrapped_text(self.player.conversation_partner.dialogue, self.dialogue_font,
                                   WHITE, DIALOGUE_TEXT_X, DIALOGUE_TEXT_Y, DIALOGUE_ALLOWED_WIDTH, DIALOGUE_LINE_SPACING)

    def draw_inventory(self):
        pygame.draw.rect(self.screen, BLACK, self.inventory_box)
        pygame.draw.rect(self.screen, WHITE, self.inventory_box, INVENTORY_BOX_OUTLINE)
        pygame.draw.rect(self.screen, BLACK, self.inventory_tab)
        pygame.draw.rect(self.screen, WHITE, self.inventory_tab, INVENTORY_BOX_OUTLINE)
        self.draw_text('Inventory', self.inventory_item_font, WHITE, self.inventory_tab.x + INVENTORY_BOX_OUTLINE, self.inventory_tab.y)
        inventory_item_y = INVENTORY_TEXT_Y
        inventory_idx = 0
        for item in self.player.player_inventory:
            self.draw_wrapped_text(item.type, self.inventory_item_font, WHITE, INVENTORY_TEXT_X, 
                                   inventory_item_y, INVENTORY_ALLOWED_WIDTH, INVENTORY_LINE_SPACING)
            if self.player.inventory_idx == inventory_idx:
                self.inventory_selection_box.topleft = (INVENTORY_BOX_X + INVENTORY_BOX_OUTLINE + 1, inventory_item_y)
                pygame.draw.rect(self.screen, WHITE, self.inventory_selection_box, INVENTORY_SELECTION_OUTLINE)
            inventory_idx += 1
            inventory_item_y += self.inventory_item_font_height
        if len(self.player.player_inventory) > 0:
            self.screen.blit(self.player.player_inventory[self.player.inventory_idx].image, vector(INVENTORY_IMAGE_X, INVENTORY_IMAGE_Y))
            self.draw_wrapped_text(self.player.player_inventory[self.player.inventory_idx].details, 
                                   self.dialogue_font, WHITE, int(INVENTORY_IMAGE_X - INVENTORY_BOX_OUTLINE * 4), 
                                   INVENTORY_IMAGE_Y + TILESIZE + INVENTORY_LINE_SPACING, 
                                   INVENTORY_ALLOWED_WIDTH - INVENTORY_BOX_OUTLINE, INVENTORY_LINE_SPACING)
        pygame.draw.line(self.screen, WHITE, vector(WIDTH / 2, INVENTORY_BOX_Y), vector(WIDTH / 2, INVENTORY_BOX_Y + INVENTORY_BOX_HEIGHT), INVENTORY_BOX_OUTLINE)

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
            if isinstance(sprite, Item):
                if not sprite.visible:
                    continue
            self.screen.blit(sprite.image, self.camera.apply(sprite))
            if self.draw_debug:
                pygame.draw.rect(self.screen, CYAN, self.camera.apply_rect(sprite.hit_rect), 1)
        if self.draw_debug:
            for wall in self.walls:
                pygame.draw.rect(self.screen, CYAN, self.camera.apply_rect(wall.rect), 1)

        # pygame.draw.rect(self.screen, WHITE, self.player.hit_rect, 2)
        if self.night:
            self.render_fog()

        # HUD functions
        draw_player_health(self.screen, 10, 10, self.player.health / PLAYER_HEALTH)
        self.draw_dialogue_box()

        # self.draw_text('Shades: {}'.format(len(self.mobs)), self.hud_font, WHITE, 
        #                 WIDTH - 10, 10, align="ne")

        # Draw inventory
        if self.inventory:
            self.draw_inventory()

        # Paused
        if self.paused:
            self.screen.blit(self.dim_screen, (0, 0))
            self.draw_text('Paused', self.pause_font, RED, WIDTH / 2, HEIGHT / 2, align='center')

        # Always last in drawing "flip"
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            # Check for closing the window *x*
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYUP:
                self.wait_for_up = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                if event.key == pygame.K_h and DEBUG:
                    self.draw_debug = not self.draw_debug
                if event.key == pygame.K_p:
                    self.paused = not self.paused
                if event.key == pygame.K_n:
                    self.night = not self.night

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        self.screen.fill(BLACK)
        self.draw_text('GAME OVER', self.game_over_font, RED, 
                        WIDTH / 2, HEIGHT / 2, align="center")
        self.draw_text('Press a key to start', self.game_over_sub_font, WHITE, 
                        WIDTH / 2, HEIGHT * 3 / 4, align="center")
        pygame.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        pygame.event.wait()
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.quit()
                if event.type == pygame.KEYUP:
                    waiting = False


game = Game()
game.show_start_screen()
while True:
    game.new()
    game.run()
    game.show_go_screen()