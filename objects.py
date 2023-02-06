import pygame

class WindowIcon():
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Sprites/icon.png')
class WallOne():
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Sprites/wall1.png')
class WallTwo():
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Sprites/wall2.png')
class WallThree():
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Sprites/wall3.png')
class WallFour():
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Sprites/wall4.png')
class WallFive():
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Sprites/wall5.png')
class Stair():
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Sprites/stairs.png')
class Weapon():
    X = 0
    Y = 0
    Rotation = 0
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Sprites/sword.png')
class Wizard():
    X = 0
    Y = 0
    Flipped = False
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Sprites/player.png')
class ZombieOne():
    X = 0
    Y = 0
    Alive = False
    Flipped = False
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Sprites/zombie.png')
class ZombieTwo():
    X = 0
    Y = 0
    Alive = False
    Flipped = False
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Sprites/zombie.png')
class DemonOne():
    X = 0
    Y = 0
    Spawn = 0
    TimerStart = 0
    TimerCurrent = 0
    TimerElapsed = 0
    Timer = False
    Alive = False
    Flipped = False
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Sprites/demon.png')
class DemonTwo():
    X = 0
    Y = 0
    Spawn = 0
    TimerStart = 0
    TimerCurrent = 0
    TimerElapsed = 0
    Timer = False
    Alive = False
    Flipped = False
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Sprites/demon.png')
class DemonspawnOne():
    X = 0
    Y = 0
    Alive = False
    Flipped = False
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Sprites/demonspawn.png')
class DemonspawnTwo():
    X = 0
    Y = 0
    Alive = False
    Flipped = False
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Sprites/demonspawn.png')
class DemonspawnThree():
    X = 0
    Y = 0
    Alive = False
    Flipped = False
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Sprites/demonspawn.png')
class DemonspawnFour():
    X = 0
    Y = 0
    Alive = False
    Flipped = False
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Sprites/demonspawn.png')
class DemonspawnFive():
    X = 0
    Y = 0
    Alive = False
    Flipped = False
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Sprites/demonspawn.png')
class DemonspawnSix():
    X = 0
    Y = 0
    Alive = False
    Flipped = False
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Sprites/demonspawn.png')
class BatOne():
    X = 0
    Y = 0
    AnimFrame = 1
    Flipped = False
    def __init__(self):
        super().__init__()
        self.frame1 = pygame.image.load('./Sprites/bat_frame1.png')
        self.frame2 = pygame.image.load('./Sprites/bat_frame2.png')
