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
class Demon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Sprites/demon.png')
class DemonTwo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Sprites/demon.png')
class DemonSpawnOne(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Sprites/demonspawn.png')
class DemonSpawnTwo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Sprites/demonspawn.png')
class DemonSpawnThree(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Sprites/demonspawn.png')
class DemonSpawnFour(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Sprites/demonspawn.png')
class DemonSpawnFive(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Sprites/demonspawn.png')
class DemonSpawnSix(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Sprites/demonspawn.png')
class WallFront1:
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Sprites/wallfront.png')
