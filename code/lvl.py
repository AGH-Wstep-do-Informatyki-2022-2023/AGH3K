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

        for x, y, surf in tmx_data.get_layer_by_name("collisions").tiles():
            Generic((x * TILE_SIZE, y * TILE_SIZE), pygame.Surface((TILE_SIZE, TILE_SIZE)), [self.collision_sprites], LAYERS["main"])
        
        for x, y, surf in tmx_data.get_layer_by_name("fance").tiles():
            Fence((x * TILE_SIZE, y * TILE_SIZE), surf, [self.all_sprites, self.collision_sprites], LAYERS["main"])

        for x, y, surf in tmx_data.get_layer_by_name("soil").tiles():
            Fence((x * TILE_SIZE, y * TILE_SIZE), surf, [self.all_sprites], LAYERS["house bottom"])

        for x, y, surf in tmx_data.get_layer_by_name("decorations").tiles():
            Decoration((x * TILE_SIZE, y * TILE_SIZE), surf, [self.all_sprites, self.collision_sprites], LAYERS["house bottom"])

        for x, y, surf in tmx_data.get_layer_by_name("campfire").tiles():
            Generic((x * TILE_SIZE, y * TILE_SIZE), surf, [self.all_sprites], LAYERS["house bottom"])

        for x, y, surf in tmx_data.get_layer_by_name("log").tiles():
            Log((x * TILE_SIZE, y * TILE_SIZE), surf, [self.all_sprites, self.collision_sprites], LAYERS["house bottom"])

        for x, y, surf in tmx_data.get_layer_by_name("water").tiles():
            Generic((x * TILE_SIZE, y * TILE_SIZE), surf, [self.all_sprites], LAYERS["main"])
        
        for x, y, surf in tmx_data.get_layer_by_name("flowers").tiles():
            Generic((x * TILE_SIZE, y * TILE_SIZE), surf, [self.all_sprites], LAYERS["house bottom"])

        for obj in tmx_data.get_layer_by_name("tree_top"):
            Tree_Top((obj.x, obj.y), pygame.transform.scale(obj.image, (obj.width * 2, obj.height * 2)), [self.all_sprites, self.collision_sprites], LAYERS["house top"], obj.name)

        for obj in tmx_data.get_layer_by_name("tree_bottom"):
            Tree_Bottom((obj.x, obj.y), pygame.transform.scale(obj.image, (obj.width * 2, obj.height * 2)), [self.all_sprites, self.collision_sprites], LAYERS["main"], obj.name)

        for obj in tmx_data.get_layer_by_name("house_bottom"):
            House_Bottom((obj.x, obj.y), pygame.transform.scale(obj.image, (obj.width * 1, obj.height * 1)), [self.all_sprites, self.collision_sprites], LAYERS["house bottom"], obj.name)

        for obj in tmx_data.get_layer_by_name("house_top"):
            House_Bottom((obj.x, obj.y), pygame.transform.scale(obj.image, (obj.width * 1, obj.height * 1)), [self.all_sprites], LAYERS["house top"], obj.name)

        Generic(pos = (0,0), surf = pygame.transform.scale_by(pygame.image.load('graphics/world/ground48.png').convert_alpha(), (2, 2)), groups = self.all_sprites, z = LAYERS['ground'])
        self.player = Player((1000, 1000), self.all_sprites, self.collision_sprites)

    def run(self, dt):
        self.display_surface.fill((80,167,232,255))
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