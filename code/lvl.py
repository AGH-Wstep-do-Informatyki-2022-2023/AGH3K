import pygame
from player import Player
from settings import *
from sprites import *
from pytmx.util_pygame import load_pygame

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.all_sprites = CameraGroup()
        self.collision_sprites = pygame.sprite.Group()
        self.setup()

    def setup(self):
        tmx_data = load_pygame('data\map48.tmx')

        for x, y, surf in tmx_data.get_layer_by_name("sea").tiles():
            Generic((x * TILE_SIZE, y * TILE_SIZE), surf, [self.all_sprites], LAYERS["water"])

        for obj in tmx_data.get_layer_by_name("trees"):
            Tree((obj.x, obj.y), pygame.transform.scale(obj.image, (obj.width * 2, obj.height * 2)), [self.all_sprites, self.collision_sprites], obj.name)

        Generic(pos = (0,0), surf = pygame.transform.scale_by(pygame.image.load('graphics/world/ground48.png').convert_alpha(), (2, 2)), groups = self.all_sprites, z = LAYERS['ground'])
        self.player = Player((640, 360), self.all_sprites, self.collision_sprites)

    def run(self, dt):
        self.display_surface.fill('blue')
        # self.all_sprites.draw(self.display_surface)
        self.all_sprites.custom_draw(self.player)
        self.all_sprites.update(dt)

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        
    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
        self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2
        
        for layer in LAYERS.values():
            for sprite in self.sprites():
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, offset_rect)