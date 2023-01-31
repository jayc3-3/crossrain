import pygame

class WindowIcon():
    def __init__(self):
        self.image = pygame.image.load('./Sprites/icon.png')
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Sprites/player.png')
class WoodenSword(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Sprites/swordwood.png')
class ZombieOne(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Sprites/zombie.png')
class ZombieTwo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Sprites/zombie.png')
class WallFront1:
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Sprites/wallfront.png')
