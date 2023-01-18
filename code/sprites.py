import pygame
from settings import *

class Generic(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, z = LAYERS['main']):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)
        self.z = z
        self.hitbox = self.rect.copy().inflate((-self.rect.width * 0.2,-self.rect.height * 0.2))

class Tree(Generic):
    def __init__(self, pos, surf, groups, z, name):
        super().__init__(pos, surf, groups, z)

class Fence(Generic):
    def __init__(self, pos, surf, groups, z):
        super().__init__(pos, surf, groups, z)
        self.hitbox = self.rect.copy().inflate((-self.rect.width * 0.4,-self.rect.height * 0.4))

class Tree_Top(Tree):
    def __init__(self, pos, surf, groups, z, name):
        super().__init__(pos, surf, groups, z, name)
        self.hitbox = self.rect.copy().inflate((-self.rect.width * 0.99,-self.rect.height * 0.99))
        
class Tree_Bottom(Tree):
    def __init__(self, pos, surf, groups, z, name):
        super().__init__(pos, surf, groups, z, name)
        self.hitbox = self.rect.copy().inflate((-self.rect.width * 0.7,-self.rect.height * 0.3))

class Decoration(Generic):
    def __init__(self, pos, surf, groups, z):
        super().__init__(pos, surf, groups, z)
        self.hitbox = self.rect.copy().inflate((-self.rect.width * 0.7,-self.rect.height * 0.7))

class Log(Generic):
    def __init__(self, pos, surf, groups, z):
        super().__init__(pos, surf, groups, z)
        self.hitbox = self.rect.copy().inflate((-self.rect.width * 0.6,-self.rect.height * 0.7))

class House_Bottom(Tree):
    def __init__(self, pos, surf, groups, z, name):
        super().__init__(pos, surf, groups, z, name)
        self.hitbox = self.rect.copy().inflate((-self.rect.width * 0.3,-self.rect.height * 0.6))
