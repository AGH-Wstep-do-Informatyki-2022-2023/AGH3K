import pygame
from settings import *
from supp import *


class Player(pygame.sprite.Sprite):
    def __init__(self, position, group):
        super().__init__(group)

        self.import_assets()
        self.status = "idle"
        self.frame_index = 0

        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=position)

        self.direction = pygame.math.Vector2(0, 0)
        # !
        self.position = pygame.math.Vector2(self.rect.center)
        self.speed = 200

    def import_assets(self):
        self.animations = {"idle": []}
        image_surf = pygame.image.load("../graphics/player/idle/0.png").convert_alpha()
        self.animations["idle"] = [image_surf]

# Jak sie załatwi assety to, to sie przyda
#        self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
#                           'right_idle': [], 'left_idle': [], 'up_idle': [], 'down_idle': [],
#                           'right_hoe': [], 'left_hoe': [], 'up_hoe': [], 'down_hoe': [],
#                           'right_axe': [], 'left_axe': [], 'up_axe': [], 'down_axe': [],
#                           'right_water': [], 'left_water': [], 'up_water': [], 'down_water': []}
#


#        for animation in self.animations.keys():
#            full_path = "../graphic/player/"
#            self.animations[animation] = import_folder(full_path)

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
