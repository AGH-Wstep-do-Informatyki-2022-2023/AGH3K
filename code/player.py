import pygame
from spritesheet import SpriteSheet
from settings import *
from supp import *


class Player(pygame.sprite.Sprite):
    def __init__(self, position, group, collision_sprites):
        super().__init__(group)

        self.import_assets()
        self.status = "down"
        self.frame_index = 0
        self.idle = False

        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=position)
        self.z = LAYERS['main']

        self.hitbox = self.rect.copy().inflate((-7,-7))
        self.collision_sprites = collision_sprites

        self.direction = pygame.math.Vector2(0, 0)
        # !
        self.position = pygame.math.Vector2(self.rect.center)
        self.speed = 200

    def scale_assets(self, asset_list):
        for i in range(len(asset_list)):
            asset_list[i] = pygame.transform.scale(asset_list[i], (64, 64))
        return asset_list

    def import_assets(self):
        asset_rects = [(0, 0, 16, 16), (16, 0, 16, 16), (32, 0, 16, 16), (48, 0, 16, 16)]
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
        if not self.idle:
            self.frame_index += 4 * dt
            if self.frame_index >= len(self.animations[self.status]):
                self.frame_index = 0
                
            self.image = self.animations[self.status][int(self.frame_index)]
        else:
            self.image = self.animations[self.status][0]

    def input(self):
        keys = pygame.key.get_pressed()
        self.idle = True
# Szanujmy się, kto używa strzałek?
        if keys[pygame.K_w]:
            self.direction.y = -1
            self.status = 'up'
            self.idle = False
        elif keys[pygame.K_s]:
            self.direction.y = 1
            self.status = 'down'
            self.idle = False
        else:
            self.direction.y = 0

        if keys[pygame.K_a]:
            self.direction.x = -1
            self.status = 'left'
            self.idle = False
        elif keys[pygame.K_d]:
            self.direction.x = 1
            self.status = 'right'
            self.idle = False
        else:
            self.direction.x = 0

    def collision(self, direction):
        for sprite in self.collision_sprites.sprites():
            if hasattr(sprite, "hitbox"):
                if sprite.hitbox.colliderect(self.hitbox):
                    if direction == "horizontal":
                        if self.direction.x > 0:
                            self.hitbox.right = sprite.hitbox.left
                        if self.direction.x < 0:
                            self.hitbox.left = sprite.hitbox.right
                        self.rect.centerx = self.hitbox.centerx
                        self.position.x = self.hitbox.centerx
                    if direction == "vertical":
                        if self.direction.y > 0:
                            self.hitbox.bottom = sprite.hitbox.top
                        if self.direction.y < 0:
                            self.hitbox.top = sprite.hitbox.bottom
                        self.rect.centery = self.hitbox.centery
                        self.position.y = self.hitbox.centery
                        


    def move(self, dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        self.position.x += self.direction.x*self.speed*dt
        self.hitbox.centerx = round(self.position.x)
        self.rect.centerx = self.hitbox.centerx
        self.collision("horizontal")

        self.position.y += self.direction.y*self.speed*dt
        self.hitbox.centery = round(self.position.y)
        self.rect.centery = self.hitbox.centery
        self.collision("vertical")

    def update(self, dt):
        self.input()
        self.move(dt)
        self.animate(dt)
