import pygame

class WindowIcon():
    def __init__(self):
        super().__init__()
        
        self.Image = pygame.image.load('./Sprites/icon.png')
class WallOne():
    def __init__(self):
        super().__init__()
        
        self.Image = pygame.image.load('./Sprites/wall1.png')
class WallTwo():
    def __init__(self):
        super().__init__()
        
        self.Image = pygame.image.load('./Sprites/wall2.png')
class WallThree():
    def __init__(self):
        super().__init__()
        
        self.Image = pygame.image.load('./Sprites/wall3.png')
class WallFour():
    def __init__(self):
        super().__init__()
        
        self.Image = pygame.image.load('./Sprites/wall4.png')
class WallFive():
    def __init__(self):
        super().__init__()
        
        self.Image = pygame.image.load('./Sprites/wall5.png')
class Stair():
    def __init__(self):
        super().__init__()
        
        self.Image = pygame.image.load('./Sprites/stairs.png')
class Weapon():
    X = 0
    Y = 0
    Rotation = 0
    
    def __init__(self):
        super().__init__()
        
        self.Image = pygame.image.load('./Sprites/sword.png')
class Wizard():
    X = 0
    Y = 0
    DamageTimer = False
    DamageTimerStart = 0
    DamageTimerCurrent = 0
    DamageTimerElapsed = 0
    Health = 3
    Flipped = False
    
    def __init__(self):
        super().__init__()
        
        self.Image = pygame.image.load('./Sprites/player.png')
class Zombie():
    X = 0
    Y = 0
    Anim = 0
    AnimFrame = 0
    Alive = False
    Flipped = False
    
    def __init__(self):
        super().__init__()
        
        self.CurrentFrame = pygame.image.load('./Sprites/zombie.png')
        self.Alive0 = pygame.image.load('./Sprites/zombie.png')
        self.Dying0 = pygame.image.load('./Sprites/zombie_dying0.png')
        self.Dying1 = pygame.image.load('./Sprites/zombie_dying1.png')
        self.Dying2 = pygame.image.load('./Sprites/zombie_dying2.png')
        self.Dying3 = pygame.image.load('./Sprites/zombie_dying3.png')
        self.Dying4 = pygame.image.load('./Sprites/zombie_dying4.png')
class Demon():
    X = 0
    Y = 0
    Health = 2
    Anim = 0
    AnimFrame = 0
    Spawn = 0
    SpawnTimerStart = 0
    SpawnTimerCurrent = 0
    SpawnTimerElapsed = 0
    SpawnTimer = False
    Alive = False
    Flipped = False
    
    def __init__(self):
        super().__init__()
        
        self.CurrentFrame = pygame.image.load('./Sprites/demon.png')
        self.Alive0 = pygame.image.load('./Sprites/demon.png')
        self.Dying0 = pygame.image.load('./Sprites/demon_dying0.png')
        self.Dying1 = pygame.image.load('./Sprites/demon_dying1.png')
        self.Dying2 = pygame.image.load('./Sprites/demon_dying2.png')
        self.Dying3 = pygame.image.load('./Sprites/demon_dying3.png')
        self.Dying4 = pygame.image.load('./Sprites/demon_dying4.png')
class Demonspawn():
    X = 0
    Y = 0
    Alive = False
    Flipped = False
    
    def __init__(self):
        super().__init__()
        
        self.Image = pygame.image.load('./Sprites/demonspawn.png')
class Bat():
    X = 0
    Y = 0
    Health = 3
    DamageTimer = False
    DamageTimerStart = 0
    DamageTimerCurrent = 0
    DamageTimerElapsed = 0
    Anim = 0
    AnimFrame = 0
    Alive = False
    Flipped = False

    def __init__(self):
        super().__init__()
    
        self.CurrentFrame = pygame.image.load('./Sprites/bat_alive0.png')
        self.Anim1Frame0 = pygame.image.load('./Sprites/bat_alive0.png')
        self.Anim1Frame1 = pygame.image.load('./Sprites/bat_alive1.png')
        self.Anim2Frame0 = pygame.image.load('./Sprites/bat_hit.png')
        self.Anim3Frame0 = pygame.image.load('./Sprites/bat_dying0.png')
        self.Anim3Frame1 = pygame.image.load('./Sprites/bat_dying1.png')
        self.Anim3Frame2 = pygame.image.load('./Sprites/bat_dying2.png')
        self.Anim3Frame3 = pygame.image.load('./Sprites/bat_dying3.png')
        self.Anim3Frame4 = pygame.image.load('./Sprites/bat_dying4.png')

class WizardHealth():
    def __init__(self):
        super().__init__()

        self.Image = pygame.image.load('./Sprites/player.png')
