import asyncio
import pygame
import time

from objects import WindowIcon
from objects import WallOne
from objects import WallTwo
from objects import WallThree
from objects import WallFour
from objects import WallFive
from objects import Stair
from objects import Wizard
from objects import Weapon
from objects import ZombieOne
from objects import ZombieTwo
from objects import DemonOne
from objects import DemonTwo
from objects import DemonspawnOne
from objects import DemonspawnTwo
from objects import DemonspawnThree
from objects import DemonspawnFour
from objects import DemonspawnFive
from objects import DemonspawnSix

pygame.init()
Window = pygame.display.set_mode((960, 540), pygame.RESIZABLE)
WindowWidth = pygame.display.Info().current_w
Screen = Window.copy()
pygame.display.set_caption('Crossrain')
pygame.display.set_icon(WindowIcon().image)

Clock = pygame.time.Clock()

Font1 = pygame.font.Font('./PublicPixel.ttf', 50)
Font2 = pygame.font.Font('./PublicPixel.ttf', 25)
Font3 = pygame.font.Font('./PublicPixel.ttf', 15)

Wall1 = WallOne()
Wall2 = WallTwo()
Wall3 = WallThree()
Wall4 = WallFour()
Wall5 = WallFive()
Stairs = Stair()
Player = Wizard()
Sword = Weapon()
Zombie1 = ZombieOne()
Zombie2 = ZombieTwo()
Demon1 = DemonOne()
Demon2 = DemonTwo()
Demonspawn1 = DemonspawnOne()
Demonspawn2 = DemonspawnTwo()
Demonspawn3 = DemonspawnThree()
Demonspawn4 = DemonspawnFour()
Demonspawn5 = DemonspawnFive()
Demonspawn6 = DemonspawnSix()

async def Game():
    Running = True

    RoomCompleted = False
    Room = 0
    Enemies = 0

    while Running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False

        DeltaTime = Clock.tick(60) / 1000

        FPS = Clock.get_fps()
        FPSStr = str(round(FPS))
        FPSText = Font2.render('FPS:'+FPSStr, False, (255, 255, 255))

        if RoomCompleted == True:
            if Room == 1:
                Enemies = 1
                Room = 2
                Player.X = 480
                Player.Y = 450
                Sword.X = 480
                Sword.Y = 375
                Sword.Rotation = 0
                Zombie1.X = 480
                Zombie1.Y = 75
                Zombie1.Alive = True
                RoomCompleted = False
            elif Room == 2:
                Enemies = 2
                Room = 3
                Player.X = 480
                Player.Y = 450
                Sword.X = 480
                Sword.Y = 375
                Sword.Rotation = 0
                Zombie1.X = 305
                Zombie1.Y = 100
                Zombie2.X = 655
                Zombie2.Y = 100
                Zombie1.Alive = True
                Zombie2.Alive = True
                RoomCompleted = False
            elif Room == 3:
                Enemies = 1
                Room = 4
                Player.X = 480
                Player.Y = 450
                Sword.X = 480
                Sword.Y = 375
                Sword.Rotation = 0
                Zombie1.X = 100
                Zombie1.Y = 475
                Zombie1.Alive = True
                RoomCompleted = False
            elif Room == 4:
                Enemies = 2
                Room = 5
                Player.X = 480
                Player.Y = 450
                Sword.X = 480
                Sword.Y = 375
                Sword.Rotation = 0
                Zombie1.X = 305
                Zombie1.Y = 475
                Zombie2.X = 655
                Zombie2.Y = 475
                Zombie1.Alive = True
                Zombie2.Alive = True
                RoomCompleted = False
            elif Room == 5:
                Enemies = 1
                Room = 6
                Player.X = 480
                Player.Y = 450
                Sword.X = 480
                Sword.Y = 375
                Sword.Rotation = 0
                Demon1.X = 480
                Demon1.Y = 75
                Demon1.Alive = True
                RoomCompleted = False
            elif Room == 6:
                Enemies = 3
                Room = 7
                Player.X = 480
                Player.Y = 450
                Sword.X = 480
                Sword.Y = 375
                Sword.Rotation = 0
                Zombie1.X = 305
                Zombie1.Y = 100
                Zombie2.X = 655
                Zombie2.Y = 100
                Demon1.X = 480
                Demon1.Y = 75
                Zombie1.Alive = True
                Zombie2.Alive = True
                Demon1.Alive = True
                RoomCompleted = False
            elif Room == 7:
                Enemies = 3
                Room = 8
                Player.X = 480
                Player.Y = 450
                Sword.X = 480
                Sword.Y = 375
                Sword.Rotation = 0
                Zombie1.X = 250
                Zombie1.Y = 125
                Zombie2.X = 250
                Zombie2.Y = 250
                Demon1.X = 100
                Demon1.Y = 75
                Zombie1.Alive = True
                Zombie2.Alive = True
                Demon1.Alive = True
                RoomCompleted = False
            elif Room == 8:
                Enemies = 3
                Room = 9
                Player.X = 480
                Player.Y = 450
                Sword.X = 480
                Sword.Y = 375
                Sword.Rotation = 0
                Zombie1.X = 710
                Zombie1.Y = 125
                Zombie2.X = 710
                Zombie2.Y = 250
                Demon1.X = 860
                Demon1.Y = 75
                Zombie1.Alive = True
                Zombie2.Alive = True
                Demon1.Alive = True
                RoomCompleted = False
            elif Room == 9:
                Enemies = 4
                Room = 10
                Player.X = 480
                Player.Y = 450
                Sword.X = 480
                Sword.Y = 375
                Sword.Rotation = 0
                Zombie1.X = 305
                Zombie1.Y = 475
                Zombie2.X = 655
                Zombie2.Y = 475
                Demon1.X = 100
                Demon1.Y = 75
                Demon2.X = 860
                Demon2.Y = 75
                Zombie1.Alive = True
                Zombie2.Alive = True
                Demon1.Alive = True
                Demon2.Alive = True
                RoomCompleted = False
            else:
                Enemies = 0
                Room = 0

        if Room == 0:
            Zombie1.Alive = False
            Zombie2.Alive = False
            Demon1.Alive = False
            Demon2.Alive = False
            Demonspawn1.Alive = False
            Demonspawn2.Alive = False
            Demonspawn3.Alive = False
            Demonspawn4.Alive = False
            Demonspawn5.Alive = False
            Demonspawn6.Alive = False
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                Player.X = 480
                Player.Y = 450
                Sword.X = 480
                Sword.Y = 375
                Sword.Rotation = 0
                Enemies = 0
                Room = 1
                RoomCompleted = False

        if not Room == 0:
            if pygame.key.get_pressed()[pygame.K_w]:
                if not pygame.key.get_pressed()[pygame.K_s]:
                    Player.Y = int(Player.Y - (500 * DeltaTime))
            if pygame.key.get_pressed()[pygame.K_s]:
                if not pygame.key.get_pressed()[pygame.K_w]:
                    Player.Y = int(Player.Y + (500 * DeltaTime))
            if pygame.key.get_pressed()[pygame.K_a]:
                if not pygame.key.get_pressed()[pygame.K_d]:
                    Player.X = int(Player.X - (500 * DeltaTime))
                    Player.Flipped = True
            if pygame.key.get_pressed()[pygame.K_d]:
                if not pygame.key.get_pressed()[pygame.K_a]:
                    Player.X = int(Player.X + (500 * DeltaTime))
                    Player.Flipped = False
                    
            if Player.X < 83:
                Player.X = 83
                
            if Player.X > 877:
                Player.X = 877
                
            if Player.Y > 494:
                Player.Y = 494

            if Player.X < 400:
                if Player.Y < 40:
                    Player.X = 400
                elif Player.Y < 68:
                    Player.Y = 68
            elif Player.X > 557:
                if Player.Y < 40:
                    Player.X = 557
                elif Player.Y < 68:
                    Player.Y = 68

            if Player.Y < 24:
                if not Enemies == 0:
                    Player.Y = 24
                else:
                    RoomCompleted = True

            if pygame.key.get_pressed()[pygame.K_w]:
                if pygame.key.get_pressed()[pygame.K_a]:
                    Sword.X = Player.X - 99
                    Sword.Y = Player.Y - 75
                    Sword.Rotation = 45
                elif pygame.key.get_pressed()[pygame.K_d]:
                    Sword.X = Player.X + 75
                    Sword.Y = Player.Y - 75
                    Sword.Rotation = 315
                else:
                    Sword.X = Player.X
                    Sword.Y = Player.Y - 75
                    Sword.Rotation = 0

            if pygame.key.get_pressed()[pygame.K_s]:
                if pygame.key.get_pressed()[pygame.K_a]:
                    Sword.X = Player.X - 99
                    Sword.Y = Player.Y + 75
                    Sword.Rotation = 135
                elif pygame.key.get_pressed()[pygame.K_d]:
                    Sword.X = Player.X + 75
                    Sword.Y = Player.Y + 75
                    Sword.Rotation = 225
                else:
                    Sword.X = Player.X
                    Sword.Y = Player.Y + 75
                    Sword.Rotation = 180

            if pygame.key.get_pressed()[pygame.K_d]:
                if not pygame.key.get_pressed()[pygame.K_a]:
                    if not pygame.key.get_pressed()[pygame.K_w]:
                        if not pygame.key.get_pressed()[pygame.K_s]:
                            Sword.X = Player.X + 75
                            Sword.Y = Player.Y
                            Sword.Rotation = 270

            if pygame.key.get_pressed()[pygame.K_a]:
                if not pygame.key.get_pressed()[pygame.K_d]:
                    if not pygame.key.get_pressed()[pygame.K_w]:
                        if not pygame.key.get_pressed()[pygame.K_s]:
                            Sword.X = Player.X - 99
                            Sword.Y = Player.Y
                            Sword.Rotation = 90

            PlayerRect = Player.image.get_rect(center=(Player.X, Player.Y))
            SwordRect = Sword.image.get_rect(center=(Sword.X, Sword.Y))
            Zombie1Rect = Zombie1.image.get_rect(center=(Zombie1.X, Zombie1.Y))
            Zombie2Rect = Zombie2.image.get_rect(center=(Zombie2.X, Zombie2.Y))
            Demon1Rect = Demon1.image.get_rect(center=(Demon1.X, Demon1.Y))
            Demon2Rect = Demon2.image.get_rect(center=(Demon2.X, Demon2.Y))
            Demonspawn1Rect = Demonspawn1.image.get_rect(center=(Demonspawn1.X, Demonspawn1.Y))
            Demonspawn2Rect = Demonspawn2.image.get_rect(center=(Demonspawn2.X, Demonspawn2.Y))
            Demonspawn3Rect = Demonspawn3.image.get_rect(center=(Demonspawn3.X, Demonspawn3.Y))
            Demonspawn4Rect = Demonspawn4.image.get_rect(center=(Demonspawn4.X, Demonspawn4.Y))
            Demonspawn5Rect = Demonspawn5.image.get_rect(center=(Demonspawn5.X, Demonspawn5.Y))
            Demonspawn6Rect = Demonspawn6.image.get_rect(center=(Demonspawn6.X, Demonspawn6.Y))

            SwordRotated = pygame.transform.rotate(Sword.image, Sword.Rotation)

            if Zombie1.Alive == True:
                if Zombie1.X < Player.X:
                    Zombie1.Flipped = False
                else:
                    Zombie1.Flipped = True
                if Zombie1Rect.colliderect(SwordRect):
                    Zombie1.Alive = False
                    Enemies = Enemies - 1
                elif Zombie1Rect.colliderect(PlayerRect):
                    Room = 0
                
                if Zombie1.X < Player.X - 10:
                    Zombie1.X = int(Zombie1.X + (315 * DeltaTime))
                elif Zombie1.X > Player.X + 10:
                    Zombie1.X = int(Zombie1.X - (315 * DeltaTime))

                if Zombie1.Y < Player.Y - 10:
                    Zombie1.Y = int(Zombie1.Y + (315 * DeltaTime))
                elif Zombie1.Y > Player.Y + 10:
                    Zombie1.Y = int(Zombie1.Y - (315 * DeltaTime))
                    
                if Zombie1.X < 66:
                    Zombie1.X = 66
                
                if Zombie1.X > 865:
                    Zombie1.X = 865
                
                if Zombie1.Y > 494:
                    Zombie1.Y = 494

                if Zombie1.X < 400:
                    if Zombie1.Y < 40:
                        Zombie1.X = 400
                    elif Zombie1.Y < 68:
                        Zombie1.Y = 68
                elif Zombie1.X > 557:
                    if Zombie1.Y < 40:
                        Zombie1.X = 557
                    elif Zombie1.Y < 68:
                        Zombie1.Y = 68

                if Zombie1.Y < 24:
                    Zombie1.Y = 24

            if Zombie2.Alive == True:
                if Zombie2.X < Player.X:
                    Zombie2.Flipped = False
                else:
                    Zombie2.Flipped = True
                if Zombie2Rect.colliderect(SwordRect):
                    Zombie2.Alive = False
                    Enemies = Enemies - 1
                elif Zombie2Rect.colliderect(PlayerRect):
                    Room = 0
                
                if Zombie2.X < Player.X - 10:
                    Zombie2.X = int(Zombie2.X + (315 * DeltaTime))
                elif Zombie2.X > Player.X + 10:
                    Zombie2.X = int(Zombie2.X - (315 * DeltaTime))

                if Zombie2.Y < Player.Y - 10:
                    Zombie2.Y = int(Zombie2.Y + (315 * DeltaTime))
                elif Zombie2.Y > Player.Y + 10:
                    Zombie2.Y = int(Zombie2.Y - (315 * DeltaTime))
                    
                if Zombie2.X < 66:
                    Zombie2.X = 66
                
                if Zombie2.X > 865:
                    Zombie2.X = 865
                
                if Zombie2.Y > 494:
                    Zombie2.Y = 494

                if Zombie2.X < 400:
                    if Zombie2.Y < 40:
                        Zombie2.X = 400
                    elif Zombie2.Y < 68:
                        Zombie2.Y = 68
                elif Zombie2.X > 557:
                    if Zombie2.Y < 40:
                        Zombie2.X = 557
                    elif Zombie2.Y < 68:
                        Zombie1.Y = 68

                if Zombie2.Y < 24:
                    Zombie2.Y = 24
                    
            if Demon1.Alive == True:
                if Demon1.X > Player.X:
                    Demon1.Flipped = True
                else:
                    Demon1.Flipped = False
                    
                if Demon1.X < Player.X - 360:
                    Demon1.X = int(Demon1.X + (125 * DeltaTime))
                elif Demon1.X > Player.X + 360:
                    Demon1.X = int(Demon1.X - (125 * DeltaTime))

                if Demon1.Y < Player.Y - 270:
                    Demon1.Y = int(Demon1.Y + (125 * DeltaTime))
                elif Demon1.Y > Player.Y + 270:
                    Demon1.Y = int(Demon1.Y - (125 * DeltaTime))
                
                if Demon1.Timer == False:
                    Demon1.Timer = True
                    Demon1.TimerStart = int(time.time())
                
                Demon1.TimerCurrent = int(time.time())
                
                Demon1.TimerElapsed = Demon1.TimerCurrent - Demon1.TimerStart
                
                if Demon1.TimerElapsed > 0.99:
                    Demon1.TimerStart = 0
                    Demon1.TimerCurrent = 0
                    Demon1.TimerElapsed = 0
                    Demon1.Timer = False
                    if Demon1.Spawn == 0:
                        Enemies = Enemies + 1
                        Demon1.Spawn = 1
                        Demonspawn1.X = Demon1.X
                        Demonspawn1.Y = Demon1.Y
                        Demonspawn1.Alive = True
                    elif Demon1.Spawn == 1:
                        Enemies = Enemies + 1
                        Demon1.Spawn = 2
                        Demonspawn2.X = Demon1.X
                        Demonspawn2.Y = Demon1.Y
                        Demonspawn2.Alive = True
                    elif Demon1.Spawn == 2:
                        Enemies = Enemies + 1
                        Demon1.Spawn = 3
                        Demonspawn3.X = Demon1.X
                        Demonspawn3.Y = Demon1.Y
                        Demonspawn3.Alive = True
                    
                if Demon1Rect.colliderect(SwordRect):
                    Enemies = Enemies - 1
                    Demon1.Alive = False
                
                if Demon1Rect.colliderect(PlayerRect):
                    Room = 0
                    
            if Demon2.Alive == True:
                if Demon2.X > Player.X:
                    Demon2.Flipped = True
                else:
                    Demon2.Flipped = False
                    
                if Demon2.X < Player.X - 360:
                    Demon2.X = int(Demon2.X + (125 * DeltaTime))
                elif Demon2.X > Player.X + 360:
                    Demon2.X = int(Demon2.X - (125 * DeltaTime))

                if Demon2.Y < Player.Y - 270:
                    Demon2.Y = int(Demon2.Y + (125 * DeltaTime))
                elif Demon2.Y > Player.Y + 270:
                    Demon2.Y = int(Demon2.Y - (125 * DeltaTime))
                
                if Demon2.Timer == False:
                    Demon2.Timer = True
                    Demon2.TimerStart = int(time.time())
                
                Demon2.TimerCurrent = int(time.time())
                
                Demon2.TimerElapsed = Demon2.TimerCurrent - Demon2.TimerStart
                
                if Demon2.TimerElapsed > 0.99:
                    Demon2.TimerStart = 0
                    Demon2.TimerCurrent = 0
                    Demon2.TimerElapsed = 0
                    Demon2.Timer = False
                    if Demon2.Spawn == 0:
                        Enemies = Enemies + 1
                        Demon2.Spawn = 1
                        Demonspawn4.X = Demon2.X
                        Demonspawn4.Y = Demon2.Y
                        Demonspawn4.Alive = True
                    elif Demon2.Spawn == 1:
                        Enemies = Enemies + 1
                        Demon2.Spawn = 2
                        Demonspawn5.X = Demon2.X
                        Demonspawn5.Y = Demon2.Y
                        Demonspawn5.Alive = True
                    elif Demon2.Spawn == 2:
                        Enemies = Enemies + 1
                        Demon2.Spawn = 3
                        Demonspawn6.X = Demon2.X
                        Demonspawn6.Y = Demon2.Y
                        Demonspawn6.Alive = True
                    
                if Demon2Rect.colliderect(SwordRect):
                    Enemies = Enemies - 1
                    Demon2.Alive = False
                
                if Demon2Rect.colliderect(PlayerRect):
                    Room = 0

            if Demonspawn1.Alive == True:
                if Demonspawn1.X < Player.X:
                    Demonspawn1.Flipped = False
                else:
                    Demonspawn1.Flipped = True
                    
                if Demonspawn1.X > Player.X + 10:
                    Demonspawn1.X = int(Demonspawn1.X - (560 * DeltaTime))
                elif Demonspawn1.X < Player.X - 10:
                    Demonspawn1.X = int(Demonspawn1.X + (560 * DeltaTime))

                if Demonspawn1.Y > Player.Y + 10:
                    Demonspawn1.Y = int(Demonspawn1.Y - (560 * DeltaTime))
                elif Demonspawn1.Y < Player.Y - 10:
                    Demonspawn1.Y = int(Demonspawn1.Y + (560 * DeltaTime))
                    
                if Demonspawn1Rect.colliderect(SwordRect):
                    Enemies = Enemies - 1
                    Demonspawn1.Alive = False
                elif Demonspawn1Rect.colliderect(PlayerRect):
                    Room = 0
                    
            if Demonspawn2.Alive == True:
                if Demonspawn2.X < Player.X:
                    Demonspawn2.Flipped = False
                else:
                    Demonspawn2.Flipped = True
                    
                if Demonspawn2.X > Player.X + 10:
                    Demonspawn2.X = int(Demonspawn2.X - (560 * DeltaTime))
                elif Demonspawn2.X < Player.X - 10:
                    Demonspawn2.X = int(Demonspawn2.X + (560 * DeltaTime))

                if Demonspawn2.Y > Player.Y + 10:
                    Demonspawn2.Y = int(Demonspawn2.Y - (560 * DeltaTime))
                elif Demonspawn2.Y < Player.Y - 10:
                    Demonspawn2.Y = int(Demonspawn2.Y + (560 * DeltaTime))
                    
                if Demonspawn2Rect.colliderect(SwordRect):
                    Enemies = Enemies - 1
                    Demonspawn2.Alive = False
                elif Demonspawn2Rect.colliderect(PlayerRect):
                    Room = 0

            if Demonspawn3.Alive == True:
                if Demonspawn3.X < Player.X:
                    Demonspawn3.Flipped = False
                else:
                    Demonspawn3.Flipped = True
                    
                if Demonspawn3.X > Player.X + 10:
                    Demonspawn3.X = int(Demonspawn3.X - (560 * DeltaTime))
                elif Demonspawn3.X < Player.X - 10:
                    Demonspawn3.X = int(Demonspawn3.X + (560 * DeltaTime))

                if Demonspawn3.Y > Player.Y + 10:
                    Demonspawn3.Y = int(Demonspawn3.Y - (560 * DeltaTime))
                elif Demonspawn3.Y < Player.Y - 10:
                    Demonspawn3.Y = int(Demonspawn3.Y + (560 * DeltaTime))
                    
                if Demonspawn3Rect.colliderect(SwordRect):
                    Enemies = Enemies - 1
                    Demonspawn3.Alive = False
                elif Demonspawn3Rect.colliderect(PlayerRect):
                    Room = 0

            if Demonspawn4.Alive == True:
                if Demonspawn4.X < Player.X:
                    Demonspawn4.Flipped = False
                else:
                    Demonspawn4.Flipped = True
                    
                if Demonspawn4.X > Player.X + 10:
                    Demonspawn4.X = int(Demonspawn4.X - (560 * DeltaTime))
                elif Demonspawn4.X < Player.X - 10:
                    Demonspawn4.X = int(Demonspawn4.X + (560 * DeltaTime))

                if Demonspawn4.Y > Player.Y + 10:
                    Demonspawn4.Y = int(Demonspawn4.Y - (560 * DeltaTime))
                elif Demonspawn4.Y < Player.Y - 10:
                    Demonspawn4.Y = int(Demonspawn4.Y + (560 * DeltaTime))
                    
                if Demonspawn4Rect.colliderect(SwordRect):
                    Enemies = Enemies - 1
                    Demonspawn4.Alive = False
                elif Demonspawn4Rect.colliderect(PlayerRect):
                    Room = 0
                    
            if Demonspawn5.Alive == True:
                if Demonspawn5.X < Player.X:
                    Demonspawn5.Flipped = False
                else:
                    Demonspawn5.Flipped = True
                    
                if Demonspawn5.X > Player.X + 10:
                    Demonspawn5.X = int(Demonspawn5.X - (560 * DeltaTime))
                elif Demonspawn5.X < Player.X - 10:
                    Demonspawn5.X = int(Demonspawn5.X + (560 * DeltaTime))

                if Demonspawn5.Y > Player.Y + 10:
                    Demonspawn5.Y = int(Demonspawn5.Y - (560 * DeltaTime))
                elif Demonspawn5.Y < Player.Y - 10:
                    Demonspawn5.Y = int(Demonspawn5.Y + (560 * DeltaTime))
                    
                if Demonspawn5Rect.colliderect(SwordRect):
                    Enemies = Enemies - 1
                    Demonspawn5.Alive = False
                elif Demonspawn5Rect.colliderect(PlayerRect):
                    Room = 0

            if Demonspawn6.Alive == True:
                if Demonspawn6.X < Player.X:
                    Demonspawn6.Flipped = False
                else:
                    Demonspawn6.Flipped = True
                    
                if Demonspawn6.X > Player.X + 10:
                    Demonspawn6.X = int(Demonspawn6.X - (560 * DeltaTime))
                elif Demonspawn6.X < Player.X - 10:
                    Demonspawn6.X = int(Demonspawn6.X + (560 * DeltaTime))

                if Demonspawn6.Y > Player.Y + 10:
                    Demonspawn6.Y = int(Demonspawn6.Y - (560 * DeltaTime))
                elif Demonspawn6.Y < Player.Y - 10:
                    Demonspawn6.Y = int(Demonspawn6.Y + (560 * DeltaTime))
                    
                if Demonspawn6Rect.colliderect(SwordRect):
                    Enemies = Enemies - 1
                    Demonspawn6.Alive = False
                elif Demonspawn6Rect.colliderect(PlayerRect):
                    Room = 0

            if Zombie1.Alive == False:
                Zombie1.X = -100
                Zombie1.Y = -100

            if Zombie2.Alive == False:
                Zombie2.X = -100
                Zombie2.Y = -100
                
            if Demon1.Alive == False:
                Demon1.Spawn = 0
                Demon1.Timer = False
                Demon1.TimerStart = 0
                Demon1.TimerCurrent = 0
                Demon1.TimerElapsed = 0
                Demon1.X = -100
                Demon1.Y = -100

            if Demon2.Alive == False:
                Demon2.Spawn = 0
                Demon2.Timer = False
                Demon2.TimerStart = 0
                Demon2.TimerCurrent = 0
                Demon2.TimerElapsed = 0
                Demon2.X = -100
                Demon2.Y = -100

            if Demonspawn1.Alive == False:
                Demonspawn1.X = -100
                Demonspawn1.Y = -100

            if Demonspawn2.Alive == False:
                Demonspawn2.X = -100
                Demonspawn2.Y = -100

            if Demonspawn3.Alive == False:
                Demonspawn3.X = -100
                Demonspawn3.Y = -100

            if Demonspawn4.Alive == False:
                Demonspawn4.X = -100
                Demonspawn4.Y = -100

            if Demonspawn5.Alive == False:
                Demonspawn5.X = -100
                Demonspawn5.Y = -100

            if Demonspawn6.Alive == False:
                Demonspawn6.X = -100
                Demonspawn6.Y = -100

            if Player.Flipped == False:
                PlayerFlipped = pygame.transform.flip(Player.image, False, False)
            elif Player.Flipped == True:
                PlayerFlipped = pygame.transform.flip(Player.image, True, False)
            if Zombie1.Flipped == False:
                Zombie1Flipped = pygame.transform.flip(Zombie1.image, False, False)
            elif Zombie1.Flipped == True:
                Zombie1Flipped = pygame.transform.flip(Zombie1.image, True, False)
            if Zombie2.Flipped == False:
                Zombie2Flipped = pygame.transform.flip(Zombie2.image, False, False)
            elif Zombie2.Flipped == True:
                Zombie2Flipped = pygame.transform.flip(Zombie2.image, True, False)
            if Demon1.Flipped == False:
                Demon1Flipped = pygame.transform.flip(Demon1.image, False, False)
            elif Demon1.Flipped == True:
                Demon1Flipped = pygame.transform.flip(Demon1.image, True, False)
            if Demon2.Flipped == False:
                Demon2Flipped = pygame.transform.flip(Demon2.image, False, False)
            elif Demon2.Flipped == True:
                Demon2Flipped = pygame.transform.flip(Demon2.image, True, False)
            if Demonspawn1.Flipped == False:
                Demonspawn1Flipped = pygame.transform.flip(Demonspawn1.image, False, False)
            elif Demonspawn1.Flipped == True:
                Demonspawn1Flipped = pygame.transform.flip(Demonspawn1.image, True, False)
            if Demonspawn2.Flipped == False:
                Demonspawn2Flipped = pygame.transform.flip(Demonspawn2.image, False, False)
            elif Demonspawn2.Flipped == True:
                Demonspawn2Flipped = pygame.transform.flip(Demonspawn2.image, True, False)
            if Demonspawn3.Flipped == False:
                Demonspawn3Flipped = pygame.transform.flip(Demonspawn3.image, False, False)
            elif Demonspawn3.Flipped == True:
                Demonspawn3Flipped = pygame.transform.flip(Demonspawn3.image, True, False)
            if Demonspawn4.Flipped == False:
                Demonspawn4Flipped = pygame.transform.flip(Demonspawn4.image, False, False)
            elif Demonspawn4.Flipped == True:
                Demonspawn4Flipped = pygame.transform.flip(Demonspawn4.image, True, False)
            if Demonspawn5.Flipped == False:
                Demonspawn5Flipped = pygame.transform.flip(Demonspawn5.image, False, False)
            elif Demonspawn5.Flipped == True:
                Demonspawn5Flipped = pygame.transform.flip(Demonspawn5.image, True, False)
            if Demonspawn6.Flipped == False:
                Demonspawn6Flipped = pygame.transform.flip(Demonspawn6.image, False, False)
            elif Demonspawn6.Flipped == True:
                Demonspawn6Flipped = pygame.transform.flip(Demonspawn6.image, True, False)

        Screen.fill((66, 40, 53))

        Screen.blit(Wall1.image, (0, 0))
        Screen.blit(Wall4.image, (64, 0))
        Screen.blit(Wall1.image, (128, 0))
        Screen.blit(Wall2.image, (192, 0))
        Screen.blit(Wall1.image, (256, 0))
        Screen.blit(Wall5.image, (320, 0))
        Screen.blit(Stairs.image, (384, -32))
        Screen.blit(Wall1.image, (576, 0))
        Screen.blit(Wall4.image, (640, 0))
        Screen.blit(Wall1.image, (704, 0))
        Screen.blit(Wall3.image, (768, 0))
        Screen.blit(Wall1.image, (832, 0))
        Screen.blit(Wall5.image, (896, 0))


        Screen.blit(Wall4.image, (896, 64))
        Screen.blit(Wall1.image, (896, 128))
        Screen.blit(Wall1.image, (896, 192))
        Screen.blit(Wall5.image, (896, 256))
        Screen.blit(Wall1.image, (896, 320))
        Screen.blit(Wall4.image, (896, 384))
        Screen.blit(Wall4.image, (896, 448))
        Screen.blit(Wall1.image, (896, 518))
        
        
        Screen.blit(Wall5.image, (0, 64))
        Screen.blit(Wall4.image, (0, 128))
        Screen.blit(Wall1.image, (0, 192))
        Screen.blit(Wall1.image, (0, 256))
        Screen.blit(Wall4.image, (0, 320))
        Screen.blit(Wall4.image, (0, 384))
        Screen.blit(Wall1.image, (0, 448))
        Screen.blit(Wall5.image, (0, 518))


        Screen.blit(Wall1.image, (64, 518))
        Screen.blit(Wall4.image, (128, 518))
        Screen.blit(Wall4.image, (192, 518))
        Screen.blit(Wall1.image, (256, 518))
        Screen.blit(Wall5.image, (320, 518))
        Screen.blit(Stairs.image, (384, 518))
        Screen.blit(Wall5.image, (576, 518))
        Screen.blit(Wall1.image, (640, 518))
        Screen.blit(Wall4.image, (704, 518))
        Screen.blit(Wall1.image, (768, 518))
        Screen.blit(Wall1.image, (832, 518))

        if Room == 0:
            Title = Font1.render('Crossrain', False, (255, 255, 255))
            StartPrompt = Font3.render('Enter to start', False, (255, 255, 255))
            MoveInstructions = Font3.render('WASD to move/aim', False, (255, 255, 255))
            Version = Font2.render('v0.2.0', False, (255, 255, 255))
            Screen.blit(Title, ((WindowWidth/2)-220, 75))
            Screen.blit(StartPrompt, ((WindowWidth/2)-110, 200))
            Screen.blit(MoveInstructions, (30, 500))
            Screen.blit(Version, (800, 500))
        else:
            CurrentRoom = Font2.render('Room:'+str(Room), False, (255, 255, 255))
            Screen.blit(PlayerFlipped, (PlayerRect))
            Screen.blit(SwordRotated, (SwordRect))
            if Zombie1.Alive == True:
                Screen.blit(Zombie1Flipped, (Zombie1Rect))
            if Zombie2.Alive == True:
                Screen.blit(Zombie2Flipped, (Zombie2Rect))
            if Demonspawn1.Alive == True:
                Screen.blit(Demonspawn1Flipped, (Demonspawn1Rect))
            if Demonspawn2.Alive == True:
                Screen.blit(Demonspawn2Flipped, (Demonspawn2Rect))
            if Demonspawn3.Alive == True:
                Screen.blit(Demonspawn3Flipped, (Demonspawn3Rect))
            if Demonspawn4.Alive == True:
                Screen.blit(Demonspawn4Flipped, (Demonspawn4Rect))
            if Demonspawn5.Alive == True:
                Screen.blit(Demonspawn5Flipped, (Demonspawn5Rect))
            if Demonspawn6.Alive == True:
                Screen.blit(Demonspawn6Flipped, (Demonspawn6Rect))
            if Demon1.Alive == True:
                Screen.blit(Demon1Flipped, (Demon1Rect))
            if Demon2.Alive == True:
                Screen.blit(Demon2Flipped, (Demon2Rect))
            Screen.blit(CurrentRoom, (750, 15))

        Screen.blit(FPSText, (25, 15))

        Window.blit(pygame.transform.scale(Screen, Window.get_rect().size), (0, 0))
        pygame.display.flip()

        if not Running:
            pygame.quit()
            return

        await asyncio.sleep(0)

asyncio.run(Game())
