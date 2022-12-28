import pygame
from spritesheet import SpriteSheet
from settings import *
from supp import *


class Player(pygame.sprite.Sprite):
    def __init__(self, position, group):
        super().__init__(group)

        self.import_assets()
        self.status = "down"
        self.frame_index = 0

        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=position)

        self.direction = pygame.math.Vector2(0, 0)
        # !
        self.position = pygame.math.Vector2(self.rect.center)
        self.speed = 200

    def import_assets(self):
        asset_rects = [(0, 0, 32, 32), (32, 0, 32, 32), (64, 0, 32, 32), (96, 0, 32, 32)]
        up_ss = SpriteSheet('graphics/player/Character_Up.png')
        up_animation = up_ss.images_at(asset_rects)
        
        down_ss = SpriteSheet('graphics/player/Character_Down.png')
        down_animation = down_ss.images_at(asset_rects)
        
        left_ss = SpriteSheet('graphics/player/Character_Left.png')
        left_animation = left_ss.images_at(asset_rects)
        
        right_ss = SpriteSheet('graphics/player/Character_Right.png')
        right_animation = right_ss.images_at(asset_rects)
        

        self.animations = {'up': up_animation, 'down': down_animation, 'left': left_animation, 'right': right_animation}


    def animate(self, dt):
        self.frame_index += 4 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
            
        self.image = self.animations[self.status][int(self.frame_index)]

    def input(self):
        keys = pygame.key.get_pressed()

# Szanujmy się, kto używa strzałek?
        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def move(self, dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        self.position.x += self.direction.x*self.speed*dt
        self.rect.center = self.position

        self.position.y += self.direction.y*self.speed*dt
        self.rect.center = self.position

    def update(self, dt):
        self.input()
        self.move(dt)
        self.animate(dt)
