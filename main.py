#Modules
import asyncio
import pygame
import os
import time

#Objects
from objects import WindowIcon
from objects import WallOne
from objects import WallTwo
from objects import WallThree
from objects import WallFour
from objects import WallFive
from objects import Stair
from objects import Weapon
from objects import WizardHealth
from objects import Wizard
from objects import Zombie
from objects import Demon
from objects import Demonspawn
from objects import Bat

#Initialization
pygame.init()
Window = pygame.display.set_mode((960, 540), pygame.RESIZABLE)
Screen = Window.copy()
pygame.display.set_caption("Crossrain")
pygame.display.set_icon(WindowIcon().Image)

Clock = pygame.time.Clock()

LargeFont = pygame.font.Font('./PublicPixel.ttf', 50)
MediumFont = pygame.font.Font('./PublicPixel.ttf', 25)
SmallFont = pygame.font.Font('./PublicPixel.ttf', 15)

#Load audio
pygame.mixer.music.load('./Audio/music.ogg')
pygame.mixer.music.play(-1)
PlayerHurt = pygame.mixer.Sound('./Audio/player_hurt.wav')
EnemyHurt = pygame.mixer.Sound('./Audio/enemy_hurt.wav')

#Object names
Wall1 = WallOne()
Wall2 = WallTwo()
Wall3 = WallThree()
Wall4 = WallFour()
Wall5 = WallFive()
Stairs = Stair()
PlayerHealth = WizardHealth()
Sword = Weapon()
Player = Wizard()
Zombie1 = Zombie()
Zombie2 = Zombie()
Demon1 = Demon()
Demon2 = Demon()
Demonspawn1 = Demonspawn()
Demonspawn2 = Demonspawn()
Demonspawn3 = Demonspawn()
Demonspawn4 = Demonspawn()
Demonspawn5 = Demonspawn()
Demonspawn6 = Demonspawn()
Bat1 = Bat()
Bat2 = Bat()

#Animation lists
BatAlive = [
            Bat1.Anim1Frame0, Bat1.Anim1Frame0, Bat1.Anim1Frame0, Bat1.Anim1Frame0, Bat1.Anim1Frame0,
            Bat1.Anim1Frame0, Bat1.Anim1Frame0, Bat1.Anim1Frame0, Bat1.Anim1Frame0, Bat1.Anim1Frame0,
            Bat1.Anim1Frame1, Bat1.Anim1Frame1, Bat1.Anim1Frame1, Bat1.Anim1Frame1, Bat1.Anim1Frame1,
            Bat1.Anim1Frame1, Bat1.Anim1Frame1, Bat1.Anim1Frame1, Bat1.Anim1Frame1, Bat1.Anim1Frame1
            ]

BatHit = [
          Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0,
          Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0,
          Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0,
          Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0,
          Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0,
          Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0,
          Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0,
          Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0,
          Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0,
          Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0,
          Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0,
          Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0,
          Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0, Bat1.Anim2Frame0
          ]

BatDying = [
            Bat1.Anim3Frame0, Bat1.Anim3Frame0, Bat1.Anim3Frame0,
            Bat1.Anim3Frame0, Bat1.Anim3Frame0, Bat1.Anim3Frame0,
            Bat1.Anim3Frame1, Bat1.Anim3Frame1, Bat1.Anim3Frame1,
            Bat1.Anim3Frame1, Bat1.Anim3Frame1, Bat1.Anim3Frame1,
            Bat1.Anim3Frame2, Bat1.Anim3Frame2, Bat1.Anim3Frame2,
            Bat1.Anim3Frame2, Bat1.Anim3Frame2, Bat1.Anim3Frame2,
            Bat1.Anim3Frame3, Bat1.Anim3Frame3, Bat1.Anim3Frame3,
            Bat1.Anim3Frame3, Bat1.Anim3Frame3, Bat1.Anim3Frame3,
            Bat1.Anim3Frame4, Bat1.Anim3Frame4, Bat1.Anim3Frame4,
            Bat1.Anim3Frame4, Bat1.Anim3Frame4, Bat1.Anim3Frame4,
            ]

ZombieAlive = [Zombie1.Alive0, Zombie1.Alive0, Zombie1.Alive0]

ZombieDying = [
               Zombie1.Dying0, Zombie1.Dying0,
               Zombie1.Dying1, Zombie1.Dying1,
               Zombie1.Dying2, Zombie1.Dying2,
               Zombie1.Dying3, Zombie1.Dying3,
               Zombie1.Dying4, Zombie1.Dying4,
               ]

DemonAlive = [Demon1.Alive0, Demon1.Alive0, Demon1.Alive0]

DemonDying = [
              Demon1.Dying0, Demon1.Dying0, Demon1.Dying0, Demon1.Dying0,
              Demon1.Dying1, Demon1.Dying1, Demon1.Dying1, Demon1.Dying1,
              Demon1.Dying2, Demon1.Dying2, Demon1.Dying2, Demon1.Dying2,
              Demon1.Dying3, Demon1.Dying3, Demon1.Dying3, Demon1.Dying3,
              Demon1.Dying4, Demon1.Dying4, Demon1.Dying4, Demon1.Dying4
              ]

#Enable debug
if os.path.exists('./Debug'):
    Debug = True
    print("Debug controls:")
    print("O and P to change the current room")
    print("K to reset the players health counter")
    print("L to set the completion state of the room to 'Completed'")
else:
    Debug = False

#Game
async def Game():
    #Game variables
    Running = True
    RoomCompleted = False
    Room = 0
    Enemies = 0
    
    #Game loop
    while Running:
        #DeltaTime/FPS stuff
        DeltaTime = Clock.tick(60) / 1000
        
        FPS = round(Clock.get_fps())
        FPSStr = str(FPS)
        FPSText = MediumFont.render("FPS:" + FPSStr, False, (255, 255, 255))
        
        #Title screen
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
            Bat1.Alive = False
            Bat2.Alive = False
            RoomCompleted = False
            Player.Health = 3
            Player.DamageTimer = False
            Player.DamageTimerStart = 0
            Player.DamageTimerCurrent = 0
            Player.DamageTimerElapsed = 0
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                Player.X = 480
                Player.Y = 450
                Sword.X = 480
                Sword.Y = 375
                Sword.Rotation = 0
                Room = 1
                Enemies = 0

        #Game
        if not Room == 0:
            #Debug
            if Debug == True:
                if pygame.key.get_pressed()[pygame.K_o]:
                    Room += 1
                    time.sleep(0.025)
                elif pygame.key.get_pressed()[pygame.K_p]:
                    Room -= 1
                    time.sleep(0.025)
                if pygame.key.get_pressed()[pygame.K_l]:
                    Enemies = 0
                if pygame.key.get_pressed()[pygame.K_k]:
                    Player.Health = 3
            
            #Room management
            if RoomCompleted == True:
                if Room == 1:
                    Enemies = 1
                    Room = 2
                    Zombie1.X = 480
                    Zombie1.Y = 75
                    Zombie1.Alive = True
                elif Room == 2:
                    Enemies = 2
                    Room = 3
                    Zombie1.X = 305
                    Zombie1.Y = 100
                    Zombie2.X = 655
                    Zombie2.Y = 100
                    Zombie1.Alive = True
                    Zombie2.Alive = True
                elif Room == 3:
                    Enemies = 1
                    Room = 4
                    Zombie1.X = 100
                    Zombie1.Y = 475
                    Zombie1.Alive = True
                elif Room == 4:
                    Enemies = 2
                    Room = 5
                    Zombie1.X = 305
                    Zombie1.Y = 475
                    Zombie2.X = 655
                    Zombie2.Y = 475
                    Zombie1.Alive = True
                    Zombie2.Alive = True
                elif Room == 5:
                    Enemies = 1
                    Room = 6
                    Demon1.X = 480
                    Demon1.Y = 100
                    Demon1.Alive = True
                elif Room == 6:
                    Enemies = 3
                    Room = 7
                    Zombie1.X = 305
                    Zombie1.Y = 100
                    Zombie2.X = 655
                    Zombie2.Y = 100
                    Demon1.X = 480
                    Demon1.Y = 75
                    Zombie1.Alive = True
                    Zombie2.Alive = True
                    Demon1.Alive = True
                elif Room == 7:
                    Enemies = 3
                    Room = 8
                    Zombie1.X = 250
                    Zombie1.Y = 125
                    Zombie2.X = 250
                    Zombie2.Y = 250
                    Demon1.X = 100
                    Demon1.Y = 75
                    Zombie1.Alive = True
                    Zombie2.Alive = True
                    Demon1.Alive = True
                elif Room == 8:
                    Enemies = 3
                    Room = 9
                    Zombie1.X = 710
                    Zombie1.Y = 125
                    Zombie2.X = 710
                    Zombie2.Y = 250
                    Demon1.X = 860
                    Demon1.Y = 75
                    Zombie1.Alive = True
                    Zombie2.Alive = True
                    Demon1.Alive = True
                elif Room == 9:
                    Enemies = 4
                    Room = 10
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
                elif Room == 10:
                    Enemies = 1
                    Room = 11
                    Bat1.X = 480
                    Bat1.Y = 75
                    Bat1.Alive = True
                elif Room == 11:
                    Enemies = 3
                    Room = 12
                    Zombie1.X = 330
                    Zombie1.Y = 450
                    Zombie2.X = 630
                    Zombie2.Y = 450
                    Bat1.X = 480
                    Bat1.Y = 75
                    Zombie1.Alive = True
                    Zombie2.Alive = True
                    Bat1.Alive = True
                elif Room == 12:
                    Enemies = 3
                    Room = 13
                    Bat1.X = 330
                    Bat1.Y = 450
                    Bat2.X = 630
                    Bat2.Y = 450
                    Demon1.X = 480
                    Demon1.Y = 75
                    Bat1.Alive = True
                    Bat2.Alive = True
                    Demon1.Alive = True
                elif Room == 13:
                    Enemies = 3
                    Room = 14
                    Bat1.X = 250
                    Bat1.Y = 230
                    Bat2.X = 250
                    Bat2.Y = 310
                    Demon1.X = 150
                    Demon1.Y = 270
                    Bat1.Alive = True
                    Bat2.Alive = True
                    Demon1.Alive = True
                elif Room == 14:
                    Enemies = 3
                    Room = 15
                    Bat1.X = 710
                    Bat1.Y = 230
                    Bat2.X = 710
                    Bat2.Y = 310
                    Demon1.X = 810
                    Demon1.Y = 270
                    Bat1.Alive = True
                    Bat2.Alive = True
                    Demon1.Alive = True
                elif Room == 15:
                    Enemies = 4
                    Room = 16
                    Zombie1.X = 330
                    Zombie1.Y = 450
                    Zombie2.X = 610
                    Zombie2.Y = 450
                    Bat1.X = 330
                    Bat1.Y = 400
                    Bat2.X = 610
                    Bat2.Y = 400
                    Zombie1.Alive = True
                    Zombie2.Alive = True
                    Bat1.Alive = True
                    Bat2.Alive = True
                elif Room == 16:
                    Enemies = 5
                    Room = 17
                    Zombie1.X = 100
                    Zombie1.Y = 100
                    Zombie2.X = 860
                    Zombie2.Y = 100
                    Demon1.X = 100
                    Demon1.Y = 440
                    Demon2.X = 860
                    Demon2.Y = 440
                    Bat1.X = 480
                    Bat1.Y = 75
                    Zombie1.Alive = True
                    Zombie2.Alive = True
                    Demon1.Alive = True
                    Demon2.Alive = True
                    Bat1.Alive = True
                elif Room == 17:
                    Enemies = 4
                    Room = 18
                    Demon1.X = 100
                    Demon1.Y = 270
                    Zombie1.X = 860
                    Zombie1.Y = 250
                    Zombie2.X = 860
                    Zombie2.Y = 290
                    Bat1.X = 800
                    Bat1.Y = 270
                    Demon1.Alive = True
                    Zombie1.Alive = True
                    Zombie2.Alive = True
                    Bat1.Alive = True
                elif Room == 18:
                    Enemies = 4
                    Room = 19
                    Demon1.X = 860
                    Demon1.Y = 270
                    Zombie1.X = 100
                    Zombie1.Y = 250
                    Zombie2.X = 100
                    Zombie2.Y = 290
                    Bat1.X = 160
                    Bat1.Y = 270
                    Demon1.Alive = True
                    Zombie1.Alive = True
                    Zombie2.Alive = True
                    Bat1.Alive = True
                elif Room == 19:
                    Enemies = 0
                    Room = 20
                    if Player.Health < 3:
                        Player.Health += 1
                elif Room == 20:
                    Enemies = 6
                    Room = 21
                    Demon1.X = 280
                    Demon1.Y = 440
                    Demon2.X = 680
                    Demon2.Y = 440
                    Zombie1.X = 100
                    Zombie1.Y = 100
                    Zombie2.X = 860
                    Zombie2.Y = 100
                    Bat1.X = 75
                    Bat1.Y = 270
                    Bat2.X = 885
                    Bat2.Y = 270
                    Demon1.Alive = True
                    Demon2.Alive = True
                    Zombie1.Alive = True
                    Zombie2.Alive = True
                    Bat1.Alive = True
                    Bat2.Alive = True
                elif Room == 21:
                    Enemies = 4
                    Room = 22
                    Zombie1.X = 100
                    Zombie1.Y = 100
                    Zombie2.X = 100
                    Zombie2.Y = 440
                    Bat1.X = 860
                    Bat1.Y = 100
                    Bat2.X = 860
                    Bat2.Y = 440
                    Zombie1.Alive = True
                    Zombie2.Alive = True
                    Bat1.Alive = True
                    Bat2.Alive = True
                elif Room == 22:
                    Enemies = 6
                    Room = 23
                    Zombie1.X = 250
                    Zombie1.Y = 150
                    Zombie2.X = 250
                    Zombie2.Y = 390
                    Demon1.X = 100
                    Demon1.Y = 100
                    Demon2.X = 100
                    Demon2.Y = 440
                    Bat1.X = 175
                    Bat1.Y = 170
                    Bat2.X = 175
                    Bat2.Y = 370
                    Zombie1.Alive = True
                    Zombie2.Alive = True
                    Demon1.Alive = True
                    Demon2.Alive = True
                    Bat1.Alive = True
                    Bat2.Alive = True
                elif Room == 23:
                    Enemies = 6
                    Room = 24
                    Zombie1.X = 710
                    Zombie1.Y = 150
                    Zombie2.X = 710
                    Zombie2.Y = 390
                    Demon1.X = 860
                    Demon1.Y = 100
                    Demon2.X = 860
                    Demon2.Y = 440
                    Bat1.X = 785
                    Bat1.Y = 170
                    Bat2.X = 785
                    Bat2.Y = 370
                    Zombie1.Alive = True
                    Zombie2.Alive = True
                    Demon1.Alive = True
                    Demon2.Alive = True
                    Bat1.Alive = True
                    Bat2.Alive = True
                elif Room == 24:
                    Enemies = 6
                    Room = 25
                    Zombie1.X = 330
                    Zombie1.Y = 450
                    Zombie2.X = 610
                    Zombie2.Y = 450
                    Demon1.X = 100
                    Demon1.Y = 100
                    Demon2.X = 860
                    Demon2.Y = 100
                    Bat1.X = 250
                    Bat1.Y = 270
                    Bat2.X = 710
                    Bat2.Y = 270
                    Zombie1.Alive = True
                    Zombie2.Alive = True
                    Demon1.Alive = True
                    Demon2.Alive = True
                    Bat1.Alive = True
                    Bat2.Alive = True
                else:
                    Room = 0

                Player.X = 480
                Player.Y = 450
                Sword.X = 480
                Sword.Y = 375
                Sword.Rotation = 0
                RoomCompleted = False
            
            #Player movement / health management
            if Player.DamageTimer == False:
                Player.DamageTimer = True
                Player.DamageTimerStart = int(time.time())
                
            Player.DamageTimerCurrent = int(time.time())
            Player.DamageTimerElapsed = Player.DamageTimerCurrent - Player.DamageTimerStart
            
            if Player.Health < 0:
                Player.Health = 0
                
            if Player.Health == 0:
                Room = 0
            
            if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]:
                Player.Y -= int(500 * DeltaTime)
            if pygame.key.get_pressed()[pygame.K_s] or pygame.key.get_pressed()[pygame.K_DOWN]:
                Player.Y += int(500 * DeltaTime)
            
            if pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT]:
                if not pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]:
                    Player.X -= int(500 * DeltaTime)
                    Player.Flipped = True
            if pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]:
                if not pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT]:
                    Player.X += int(500 * DeltaTime)
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
                if not pygame.key.get_pressed()[pygame.K_s]:
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
                if not pygame.key.get_pressed()[pygame.K_w]:
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

            if pygame.key.get_pressed()[pygame.K_UP]:
                if not pygame.key.get_pressed()[pygame.K_DOWN]:
                    if pygame.key.get_pressed()[pygame.K_LEFT]:
                        Sword.X = Player.X - 99
                        Sword.Y = Player.Y - 75
                        Sword.Rotation = 45
                    elif pygame.key.get_pressed()[pygame.K_RIGHT]:
                        Sword.X = Player.X + 75
                        Sword.Y = Player.Y - 75
                        Sword.Rotation = 315
                    else:
                        Sword.X = Player.X
                        Sword.Y = Player.Y - 75
                        Sword.Rotation = 0

            if pygame.key.get_pressed()[pygame.K_DOWN]:
                if not pygame.key.get_pressed()[pygame.K_UP]:
                    if pygame.key.get_pressed()[pygame.K_LEFT]:
                        Sword.X = Player.X - 99
                        Sword.Y = Player.Y + 75
                        Sword.Rotation = 135
                    elif pygame.key.get_pressed()[pygame.K_RIGHT]:
                        Sword.X = Player.X + 75
                        Sword.Y = Player.Y + 75
                        Sword.Rotation = 225
                    else:
                        Sword.X = Player.X
                        Sword.Y = Player.Y + 75
                        Sword.Rotation = 180

            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                if not pygame.key.get_pressed()[pygame.K_LEFT]:
                    if not pygame.key.get_pressed()[pygame.K_UP]:
                        if not pygame.key.get_pressed()[pygame.K_DOWN]:
                            Sword.X = Player.X + 75
                            Sword.Y = Player.Y
                            Sword.Rotation = 270

            if pygame.key.get_pressed()[pygame.K_LEFT]:
                if not pygame.key.get_pressed()[pygame.K_RIGHT]:
                    if not pygame.key.get_pressed()[pygame.K_UP]:
                        if not pygame.key.get_pressed()[pygame.K_DOWN]:
                            Sword.X = Player.X - 99
                            Sword.Y = Player.Y
                            Sword.Rotation = 90

            #Enemy A.I.
            if Zombie1.Alive == True:
                Zombie1.AnimFrame += 1
                if Zombie1.Anim == 0:
                    if Zombie1.AnimFrame >= len(ZombieAlive):
                        Zombie1.AnimFrame = 0
                    else:
                        Zombie1.CurrentFrame = ZombieAlive[Zombie1.AnimFrame]
                elif Zombie1.Anim == 1:
                    if Zombie1.AnimFrame >= len(ZombieDying):
                        Zombie1.Alive = False
                        Enemies -= 1
                    else:
                        Zombie1.CurrentFrame = ZombieDying[Zombie1.AnimFrame]
                
                if Zombie1.Anim == 0:
                    if Zombie1.X < Player.X:
                        Zombie1.Flipped = False
                    else:
                        Zombie1.Flipped = True
                    
                    if Zombie1.X < Player.X - 10:
                        Zombie1.X += int(315 * DeltaTime)
                    elif Zombie1.X > Player.X + 10:
                        Zombie1.X -= int(315 * DeltaTime)

                    if Zombie1.Y < Player.Y - 10:
                        Zombie1.Y += int(315 * DeltaTime)
                    elif Zombie1.Y > Player.Y + 10:
                        Zombie1.Y -= int(315 * DeltaTime)
                    
                    if Zombie1.X < 52:
                        Zombie1.X = 52
                    elif Zombie1.X > 908:
                        Zombie1.X = 908
                    
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

                if Zombie1.Y > 492:
                    Zombie1.Y = 492

            if Zombie2.Alive == True:
                Zombie2.AnimFrame += 1
                if Zombie2.Anim == 0:
                    if Zombie2.AnimFrame >= len(ZombieAlive):
                        Zombie2.AnimFrame = 0
                    else:
                        Zombie2.CurrentFrame = ZombieAlive[Zombie2.AnimFrame]
                elif Zombie2.Anim == 1:
                    if Zombie2.AnimFrame >= len(ZombieDying):
                        Zombie2.Alive = False
                        Enemies -= 1
                    else:
                        Zombie2.CurrentFrame = ZombieDying[Zombie2.AnimFrame]
                
                if Zombie2.Anim == 0:
                    if Zombie2.X < Player.X:
                        Zombie2.Flipped = False
                    else:
                        Zombie2.Flipped = True
                    
                    if Zombie2.X < Player.X - 10:
                        Zombie2.X += int(315 * DeltaTime)
                    elif Zombie2.X > Player.X + 10:
                        Zombie2.X -= int(315 * DeltaTime)

                    if Zombie2.Y < Player.Y - 10:
                        Zombie2.Y += int(315 * DeltaTime)
                    elif Zombie2.Y > Player.Y + 10:
                        Zombie2.Y -= int(315 * DeltaTime)
                    
                    if Zombie2.X < 52:
                        Zombie2.X = 52
                    elif Zombie2.X > 908:
                        Zombie2.X = 908
                    
                if Zombie2.X < 400:
                    if Zombie2.Y < 40:
                        Zombie2.X = 400
                    elif Zombie2.Y < 68:
                        Zombie2.Y = 68
                elif Zombie2.X > 557:
                    if Zombie2.Y < 40:
                        Zombie2.X = 557
                    elif Zombie2.Y < 68:
                        Zombie2.Y = 68

                if Zombie2.Y > 492:
                    Zombie2.Y = 492

            if Demon1.Alive == True:
                Demon1.AnimFrame += 1
                if Demon1.Anim == 0:
                    if Demon1.AnimFrame >= len(DemonAlive):
                        Demon1.AnimFrame = 0
                    else:
                        Demon1.CurrentFrame = DemonAlive[Demon1.AnimFrame]
                elif Demon1.Anim == 1:
                    if Demon1.AnimFrame >= len(DemonDying):
                        Demon1.Alive = False
                        Enemies -= 1
                    else:
                        Demon1.CurrentFrame = DemonDying[Demon1.AnimFrame]
                
                if not Demon1.Anim == 1:
                    if Demon1.X > Player.X:
                        Demon1.Flipped = True
                    else:
                        Demon1.Flipped = False
                    
                    if Demon1.X < Player.X - 360:
                        Demon1.X += int(125 * DeltaTime)
                    elif Demon1.X > Player.X + 360:
                        Demon1.X -= int(125 * DeltaTime)

                    if Demon1.Y < Player.Y - 270:
                        Demon1.Y += int(125 * DeltaTime)
                    elif Demon1.Y > Player.Y + 270:
                        Demon1.Y -= int(125 * DeltaTime)
                
                    if Demon1.SpawnTimer == False:
                        Demon1.SpawnTimer = True
                        Demon1.SpawnTimerStart = int(time.time())
                
                    Demon1.SpawnTimerCurrent = int(time.time())
                
                    Demon1.SpawnTimerElapsed = Demon1.SpawnTimerCurrent - Demon1.SpawnTimerStart
                
                    if Demon1.SpawnTimerElapsed > 0.99:
                        Demon1.SpawnTimerStart = 0
                        Demon1.SpawnTimerCurrent = 0
                        Demon1.SpawnTimerElapsed = 0
                        Demon1.SpawnTimer = False
                        if Demon1.Spawn == 0:
                            Enemies += 1
                            Demon1.Spawn = 1
                            Demonspawn1.X = Demon1.X
                            Demonspawn1.Y = Demon1.Y
                            Demonspawn1.Alive = True
                        elif Demon1.Spawn == 1:
                            Enemies += 1
                            Demon1.Spawn = 2
                            Demonspawn2.X = Demon1.X
                            Demonspawn2.Y = Demon1.Y
                            Demonspawn2.Alive = True
                        elif Demon1.Spawn == 2:
                            Enemies += 1
                            Demon1.Spawn = 3
                            Demonspawn3.X = Demon1.X
                            Demonspawn3.Y = Demon1.Y
                            Demonspawn3.Alive = True

            if Demon2.Alive == True:
                Demon2.AnimFrame += 1
                if Demon2.Anim == 0:
                    if Demon2.AnimFrame >= len(DemonAlive):
                        Demon2.AnimFrame = 0
                    else:
                        Demon2.CurrentFrame = DemonAlive[Demon2.AnimFrame]
                elif Demon2.Anim == 1:
                    if Demon2.AnimFrame >= len(DemonDying):
                        Demon2.Alive = False
                        Enemies -= 1
                    else:
                        Demon2.CurrentFrame = DemonDying[Demon2.AnimFrame]
                
                if not Demon2.Anim == 1:
                    if Demon2.X > Player.X:
                        Demon2.Flipped = True
                    else:
                        Demon2.Flipped = False
                    
                    if Demon2.X < Player.X - 360:
                        Demon2.X += int(125 * DeltaTime)
                    elif Demon2.X > Player.X + 360:
                        Demon2.X -= int(125 * DeltaTime)

                    if Demon2.Y < Player.Y - 270:
                        Demon2.Y += int(125 * DeltaTime)
                    elif Demon2.Y > Player.Y + 270:
                        Demon2.Y -= int(125 * DeltaTime)
                
                    if Demon2.SpawnTimer == False:
                        Demon2.SpawnTimer = True
                        Demon2.SpawnTimerStart = int(time.time())
                
                    Demon2.SpawnTimerCurrent = int(time.time())
                
                    Demon2.SpawnTimerElapsed = Demon2.SpawnTimerCurrent - Demon2.SpawnTimerStart
                
                    if Demon2.SpawnTimerElapsed > 0.99:
                        Demon2.SpawnTimerStart = 0
                        Demon2.SpawnTimerCurrent = 0
                        Demon2.SpawnTimerElapsed = 0
                        Demon2.SpawnTimer = False
                        if Demon2.Spawn == 0:
                            Enemies += 1
                            Demon2.Spawn = 1
                            Demonspawn4.X = Demon2.X
                            Demonspawn4.Y = Demon2.Y
                            Demonspawn4.Alive = True
                        elif Demon2.Spawn == 1:
                            Enemies += 1
                            Demon2.Spawn = 2
                            Demonspawn5.X = Demon2.X
                            Demonspawn5.Y = Demon2.Y
                            Demonspawn5.Alive = True
                        elif Demon2.Spawn == 2:
                            Enemies += 1
                            Demon2.Spawn = 3
                            Demonspawn6.X = Demon2.X
                            Demonspawn6.Y = Demon2.Y
                            Demonspawn6.Alive = True

            if Demonspawn1.Alive == True:
                if Demonspawn1.X < Player.X:
                    Demonspawn1.Flipped = False
                else:
                    Demonspawn1.Flipped = True
                
                if Demonspawn1.X < Player.X - 10:
                    Demonspawn1.X += int(560 * DeltaTime)
                elif Demonspawn1.X > Player.X + 10:
                    Demonspawn1.X -= int(560 * DeltaTime)
                
                if Demonspawn1.Y < Player.Y - 10:
                    Demonspawn1.Y += int(560 * DeltaTime)
                elif Demonspawn1.Y > Player.Y + 10:
                    Demonspawn1.Y -= int(560 * DeltaTime)

            if Demonspawn2.Alive == True:
                if Demonspawn2.X < Player.X:
                    Demonspawn2.Flipped = False
                else:
                    Demonspawn2.Flipped = True
                
                if Demonspawn2.X < Player.X - 10:
                    Demonspawn2.X += int(560 * DeltaTime)
                elif Demonspawn2.X > Player.X + 10:
                    Demonspawn2.X -= int(560 * DeltaTime)
                
                if Demonspawn2.Y < Player.Y - 10:
                    Demonspawn2.Y += int(560 * DeltaTime)
                elif Demonspawn2.Y > Player.Y + 10:
                    Demonspawn2.Y -= int(560 * DeltaTime)

            if Demonspawn3.Alive == True:
                if Demonspawn3.X < Player.X:
                    Demonspawn3.Flipped = False
                else:
                    Demonspawn3.Flipped = True
                
                if Demonspawn3.X < Player.X - 10:
                    Demonspawn3.X += int(560 * DeltaTime)
                elif Demonspawn3.X > Player.X + 10:
                    Demonspawn3.X -= int(560 * DeltaTime)
                
                if Demonspawn3.Y < Player.Y - 10:
                    Demonspawn3.Y += int(560 * DeltaTime)
                elif Demonspawn3.Y > Player.Y + 10:
                    Demonspawn3.Y -= int(560 * DeltaTime)

            if Demonspawn4.Alive == True:
                if Demonspawn4.X < Player.X:
                    Demonspawn4.Flipped = False
                else:
                    Demonspawn4.Flipped = True
                
                if Demonspawn4.X < Player.X - 10:
                    Demonspawn4.X += int(560 * DeltaTime)
                elif Demonspawn4.X > Player.X + 10:
                    Demonspawn4.X -= int(560 * DeltaTime)
                
                if Demonspawn4.Y < Player.Y - 10:
                    Demonspawn4.Y += int(560 * DeltaTime)
                elif Demonspawn4.Y > Player.Y + 10:
                    Demonspawn4.Y -= int(560 * DeltaTime)

            if Demonspawn5.Alive == True:
                if Demonspawn5.X < Player.X:
                    Demonspawn5.Flipped = False
                else:
                    Demonspawn5.Flipped = True
                
                if Demonspawn5.X < Player.X - 10:
                    Demonspawn5.X += int(560 * DeltaTime)
                elif Demonspawn5.X > Player.X + 10:
                    Demonspawn5.X -= int(560 * DeltaTime)
                
                if Demonspawn5.Y < Player.Y - 10:
                    Demonspawn5.Y += int(560 * DeltaTime)
                elif Demonspawn5.Y > Player.Y + 10:
                    Demonspawn5.Y -= int(560 * DeltaTime)

            if Demonspawn6.Alive == True:
                if Demonspawn6.X < Player.X:
                    Demonspawn6.Flipped = False
                else:
                    Demonspawn6.Flipped = True
                
                if Demonspawn6.X < Player.X - 10:
                    Demonspawn6.X += int(560 * DeltaTime)
                elif Demonspawn6.X > Player.X + 10:
                    Demonspawn6.X -= int(560 * DeltaTime)
                
                if Demonspawn6.Y < Player.Y - 10:
                    Demonspawn6.Y += int(560 * DeltaTime)
                elif Demonspawn6.Y > Player.Y + 10:
                    Demonspawn6.Y -= int(560 * DeltaTime)
            
            if Bat1.Alive == True:
                Bat1.AnimFrame += 1
                if Bat1.Anim == 0:
                    if Bat1.AnimFrame >= len(BatAlive):
                        Bat1.AnimFrame = 0
                    else:
                        Bat1.CurrentFrame = BatAlive[Bat1.AnimFrame]
                elif Bat1.Anim == 1:
                    if Bat1.AnimFrame >= len(BatHit):
                        Bat1.Anim = 0
                    else:
                        Bat1.CurrentFrame = BatHit[Bat1.AnimFrame]
                elif Bat1.Anim == 2:
                    if Bat1.AnimFrame >= len(BatDying):
                        Bat1.Alive = False
                        Enemies -= 1
                    else:
                        Bat1.CurrentFrame = BatDying[Bat1.AnimFrame]
                
                if Bat1.Anim == 0:
                    if Bat1.X < Player.X:
                        Bat1.Flipped = True
                    elif Bat1.X > Player.X:
                        Bat1.Flipped = False
            
                    if Bat1.X < Player.X - 10:
                        Bat1.X += int(250 * DeltaTime)
                    elif Bat1.X > Player.X + 10:
                        Bat1.X -= int(250 * DeltaTime)
                
                    if Bat1.Y < Player.Y - 10:
                        Bat1.Y += int(250 * DeltaTime)
                    elif Bat1.Y > Player.Y + 10:
                        Bat1.Y -= int(250 * DeltaTime)

            if Bat2.Alive == True:
                Bat2.AnimFrame += 1
                if Bat2.Anim == 0:
                    if Bat2.AnimFrame >= len(BatAlive):
                        Bat2.AnimFrame = 0
                    else:
                        Bat2.CurrentFrame = BatAlive[Bat2.AnimFrame]
                elif Bat2.Anim == 1:
                    if Bat2.AnimFrame >= len(BatHit):
                        Bat2.Anim = 0
                    else:
                        Bat2.CurrentFrame = BatHit[Bat2.AnimFrame]
                elif Bat2.Anim == 2:
                    if Bat2.AnimFrame >= len(BatDying):
                        Bat2.Alive = False
                        Enemies -= 1
                    else:
                        Bat2.CurrentFrame = BatDying[Bat2.AnimFrame]
                
                if Bat2.Anim == 0:
                    if Bat2.X < Player.X:
                        Bat2.Flipped = True
                    elif Bat2.X > Player.X:
                        Bat2.Flipped = False
            
                    if Bat2.X < Player.X - 10:
                        Bat2.X += int(250 * DeltaTime)
                    elif Bat2.X > Player.X + 10:
                        Bat2.X -= int(250 * DeltaTime)
                
                    if Bat2.Y < Player.Y - 10:
                        Bat2.Y += int(250 * DeltaTime)
                    elif Bat2.Y > Player.Y + 10:
                        Bat2.Y -= int(250 * DeltaTime)

            #Mouse = pygame.mouse.get_pos()
            #print(Mouse)
            
            #Update enemy rects
            PlayerRect = Player.Image.get_rect(center=(Player.X, Player.Y))
            SwordRect = Sword.Image.get_rect(center=(Sword.X, Sword.Y))
            SwordRotated = pygame.transform.rotate(Sword.Image, Sword.Rotation)
            
            Zombie1Rect = Zombie1.CurrentFrame.get_rect(center=(Zombie1.X, Zombie1.Y))
            Zombie2Rect = Zombie2.CurrentFrame.get_rect(center=(Zombie2.X, Zombie2.Y))
            
            Demon1Rect = Demon1.CurrentFrame.get_rect(center=(Demon1.X, Demon1.Y))
            Demon2Rect = Demon2.CurrentFrame.get_rect(center=(Demon2.X, Demon2.Y))
            
            Demonspawn1Rect = Demonspawn1.Image.get_rect(center=(Demonspawn1.X, Demonspawn1.Y))
            Demonspawn2Rect = Demonspawn2.Image.get_rect(center=(Demonspawn2.X, Demonspawn2.Y))
            Demonspawn3Rect = Demonspawn3.Image.get_rect(center=(Demonspawn3.X, Demonspawn3.Y))
            Demonspawn4Rect = Demonspawn4.Image.get_rect(center=(Demonspawn4.X, Demonspawn4.Y))
            Demonspawn5Rect = Demonspawn5.Image.get_rect(center=(Demonspawn5.X, Demonspawn5.Y))
            Demonspawn6Rect = Demonspawn6.Image.get_rect(center=(Demonspawn6.X, Demonspawn6.Y))
            
            Bat1Rect = Bat1.CurrentFrame.get_rect(center=(Bat1.X, Bat1.Y))
            Bat2Rect = Bat2.CurrentFrame.get_rect(center=(Bat2.X, Bat2.Y))
            
            #Check for collisions
            if Zombie1.Alive == True:
                if Zombie1.Anim == 0:
                    if Zombie1Rect.colliderect(SwordRect):
                        Zombie1.Anim = 1
                        EnemyHurt.play()
                    elif Zombie1Rect.colliderect(PlayerRect):
                        if Player.DamageTimerElapsed > 1.99:
                            Player.DamageTimer = False
                            Player.DamageTimerElapsed = 0
                            Player.Health -= 1
                            PlayerHurt.play()

            if Zombie2.Alive == True:
                if Zombie2.Anim == 0:
                    if Zombie2Rect.colliderect(SwordRect):
                        Zombie2.Anim = 1
                        EnemyHurt.play()
                    elif Zombie2Rect.colliderect(PlayerRect):
                        if Player.DamageTimerElapsed > 1.99:
                            Player.DamageTimer = False
                            Player.DamageTimerElapsed = 0
                            Player.Health -= 1
                            PlayerHurt.play()

            if Demon1.Alive == True:
                if Demon1.Anim == 0:
                    if Demon1Rect.colliderect(SwordRect):
                        Demon1.Anim = 1
                        EnemyHurt.play()
                    elif Demon1Rect.colliderect(PlayerRect):
                        if Player.DamageTimerElapsed > 1.99:
                            Player.DamageTimer = False
                            Player.DamageTimerElapsed = 0
                            Player.Health -= 1
                            PlayerHurt.play()

            if Demon2.Alive == True:
                if Demon2.Anim == 0:
                    if Demon2Rect.colliderect(SwordRect):
                        Demon2.Anim = 1
                        EnemyHurt.play()
                    elif Demon2Rect.colliderect(PlayerRect):
                        if Player.DamageTimerElapsed > 1.99:
                            Player.DamageTimer = False
                            Player.DamageTimerElapsed = 0
                            Player.Health -= 1
                            PlayerHurt.play()

            if Demonspawn1.Alive == True:
                if Demonspawn1Rect.colliderect(SwordRect):
                    Demonspawn1.Alive = False
                    Enemies -= 1
                    EnemyHurt.play()
                elif Demonspawn1Rect.colliderect(PlayerRect):
                    if Player.DamageTimerElapsed > 1.99:
                        Player.DamageTimer = False
                        Player.DamageTimerElapsed = 0
                        Player.Health -= 1
                        Enemies -= 1
                        Demonspawn1.Alive = False
                        PlayerHurt.play()
                    else:
                        Enemies -= 1
                        Demonspawn1.Alive = False

            if Demonspawn2.Alive == True:
                if Demonspawn2Rect.colliderect(SwordRect):
                    Demonspawn2.Alive = False
                    Enemies -= 1
                    EnemyHurt.play()
                elif Demonspawn2Rect.colliderect(PlayerRect):
                    if Player.DamageTimerElapsed > 1.99:
                        Player.DamageTimer = False
                        Player.DamageTimerElapsed = 0
                        Player.Health -= 1
                        Enemies -= 1
                        Demonspawn2.Alive = False
                        PlayerHurt.play()
                    else:
                        Enemies -= 1
                        Demonspawn2.Alive = False

            if Demonspawn3.Alive == True:
                if Demonspawn3Rect.colliderect(SwordRect):
                    Demonspawn3.Alive = False
                    Enemies -= 1
                    EnemyHurt.play()
                elif Demonspawn3Rect.colliderect(PlayerRect):
                    if Player.DamageTimerElapsed > 1.99:
                        Player.DamageTimer = False
                        Player.DamageTimerElapsed = 0
                        Player.Health -= 1
                        Enemies -= 1
                        Demonspawn3.Alive = False
                        PlayerHurt.play()
                    else:
                        Enemies -= 1
                        Demonspawn3.Alive = False

            if Demonspawn4.Alive == True:
                if Demonspawn4Rect.colliderect(SwordRect):
                    Demonspawn4.Alive = False
                    Enemies -= 1
                    EnemyHurt.play()
                elif Demonspawn4Rect.colliderect(PlayerRect):
                    if Player.DamageTimerElapsed > 1.99:
                        Player.DamageTimer = False
                        Player.DamageTimerElapsed = 0
                        Player.Health -= 1
                        Enemies -= 1
                        Demonspawn4.Alive = False
                        PlayerHurt.play()
                    else:
                        Enemies -= 1
                        Demonspawn4.Alive = False

            if Demonspawn5.Alive == True:
                if Demonspawn5Rect.colliderect(SwordRect):
                    Demonspawn5.Alive = False
                    Enemies -= 1
                    EnemyHurt.play()
                elif Demonspawn5Rect.colliderect(PlayerRect):
                    if Player.DamageTimerElapsed > 1.99:
                        Player.DamageTimer = False
                        Player.DamageTimerElapsed = 0
                        Player.Health -= 1
                        Enemies -= 1
                        Demonspawn5.Alive = False
                        PlayerHurt.play()
                    else:
                        Enemies -= 1
                        Demonspawn5.Alive = False

            if Demonspawn6.Alive == True:
                if Demonspawn6Rect.colliderect(SwordRect):
                    Demonspawn6.Alive = False
                    Enemies -= 1
                    EnemyHurt.play()
                elif Demonspawn6Rect.colliderect(PlayerRect):
                    if Player.DamageTimerElapsed > 1.99:
                        Player.DamageTimer = False
                        Player.DamageTimerElapsed = 0
                        Player.Health -= 1
                        Enemies -= 1
                        Demonspawn6.Alive = False
                        PlayerHurt.play()
                    else:
                        Enemies -= 1
                        Demonspawn6.Alive = False
            
            if Bat1.Alive == True:
                if Bat1Rect.colliderect(SwordRect):
                    if Bat1.Anim == 0:
                        if not Bat1.Health == 0:
                            Bat1.Health -= 1
                            Bat1.Anim = 1
                        
                        if Bat1.Health == 0:
                            Bat1.AnimFrame = 0
                            Bat1.Anim = 2
                        EnemyHurt.play()
                elif Bat1Rect.colliderect(PlayerRect):
                    if Bat1.Anim == 0:
                        if Player.DamageTimerElapsed > 1.99:
                            Player.DamageTimer = False
                            Player.DamageTimerElapsed = 0
                            Player.Health -= 1
                            PlayerHurt.play()

            if Bat2.Alive == True:
                if Bat2Rect.colliderect(SwordRect):
                    if Bat2.Anim == 0:
                        if not Bat2.Health == 0:
                            Bat2.Health -= 1
                            Bat2.Anim = 1
                        
                        if Bat2.Health == 0:
                            Bat2.AnimFrame = 0
                            Bat2.Anim = 2
                        EnemyHurt.play()
                elif Bat2Rect.colliderect(PlayerRect):
                    if Bat2.Anim == 0:
                        if Player.DamageTimerElapsed > 1.99:
                            Player.DamageTimer = False
                            Player.DamageTimerElapsed = 0
                            Player.Health -= 1
                            PlayerHurt.play()

            #Update dead enemies
            if Zombie1.Alive == False:
                Zombie1.X = -100
                Zombie1.Y = -100
                Zombie1.Anim = 0
                Zombie1.AnimFrame = 0
                
            if Zombie2.Alive == False:
                Zombie2.X = -100
                Zombie2.Y = -100
                Zombie2.Anim = 0
                Zombie2.AnimFrame = 0

            if Demon1.Alive == False:
                Demon1.X = -100
                Demon1.Y = -100
                Demon1.Anim = 0
                Demon1.AnimFrame = 0
                Demon1.Spawn = 0
                Demon1.SpawnTimer = False
                Demon1.SpawnTimerStart = 0
                Demon1.SpawnTimerCurrent = 0
                Demon1.SpawnTimerElapsed = 0

            if Demon2.Alive == False:
                Demon2.X = -100
                Demon2.Y = -100
                Demon2.Anim = 0
                Demon2.AnimFrame = 0
                Demon2.Spawn = 0
                Demon2.SpawnTimer = False
                Demon2.SpawnTimerStart = 0
                Demon2.SpawnTimerCurrent = 0
                Demon2.SpawnTimerElapsed = 0

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
            
            if Bat1.Alive == False:
                Bat1.X = -100
                Bat1.Y = -100
                Bat1.Health = 3
                Bat1.Anim = 0
                Bat1.AnimFrame = 0

            if Bat2.Alive == False:
                Bat2.X = -100
                Bat2.Y = -100
                Bat2.Health = 3
                Bat2.Anim = 0
                Bat2.AnimFrame = 0
            
            #Flip objects
            if Player.Flipped == False:
                PlayerFlipped = pygame.transform.flip(Player.Image, False, False)
            
            elif Player.Flipped == True:
                PlayerFlipped = pygame.transform.flip(Player.Image, True, False)
            
            if Zombie1.Flipped == False:
                Zombie1Flipped = pygame.transform.flip(Zombie1.CurrentFrame, False, False)
            
            elif Zombie1.Flipped == True:
                Zombie1Flipped = pygame.transform.flip(Zombie1.CurrentFrame, True, False)
            
            if Zombie2.Flipped == False:
                Zombie2Flipped = pygame.transform.flip(Zombie2.CurrentFrame, False, False)
            
            elif Zombie2.Flipped == True:
                Zombie2Flipped = pygame.transform.flip(Zombie2.CurrentFrame, True, False)
            
            if Demon1.Flipped == False:
                Demon1Flipped = pygame.transform.flip(Demon1.CurrentFrame, False, False)
            
            elif Demon1.Flipped == True:
                Demon1Flipped = pygame.transform.flip(Demon1.CurrentFrame, True, False)
            
            if Demon2.Flipped == False:
                Demon2Flipped = pygame.transform.flip(Demon2.CurrentFrame, False, False)
            
            elif Demon2.Flipped == True:
                Demon2Flipped = pygame.transform.flip(Demon2.CurrentFrame, True, False)
            
            if Demonspawn1.Flipped == False:
                Demonspawn1Flipped = pygame.transform.flip(Demonspawn1.Image, False, False)
            
            elif Demonspawn1.Flipped == True:
                Demonspawn1Flipped = pygame.transform.flip(Demonspawn1.Image, True, False)
            
            if Demonspawn2.Flipped == False:
                Demonspawn2Flipped = pygame.transform.flip(Demonspawn2.Image, False, False)
            
            elif Demonspawn2.Flipped == True:
                Demonspawn2Flipped = pygame.transform.flip(Demonspawn2.Image, True, False)
            
            if Demonspawn3.Flipped == False:
                Demonspawn3Flipped = pygame.transform.flip(Demonspawn3.Image, False, False)
            
            elif Demonspawn3.Flipped == True:
                Demonspawn3Flipped = pygame.transform.flip(Demonspawn3.Image, True, False)
            
            if Demonspawn4.Flipped == False:
                Demonspawn4Flipped = pygame.transform.flip(Demonspawn4.Image, False, False)
            
            elif Demonspawn4.Flipped == True:
                Demonspawn4Flipped = pygame.transform.flip(Demonspawn4.Image, True, False)
            
            if Demonspawn5.Flipped == False:
                Demonspawn5Flipped = pygame.transform.flip(Demonspawn5.Image, False, False)
            
            elif Demonspawn5.Flipped == True:
                Demonspawn5Flipped = pygame.transform.flip(Demonspawn5.Image, True, False)
            
            if Demonspawn6.Flipped == False:
                Demonspawn6Flipped = pygame.transform.flip(Demonspawn6.Image, False, False)
            
            elif Demonspawn6.Flipped == True:
                Demonspawn6Flipped = pygame.transform.flip(Demonspawn6.Image, True, False)
            
            if Bat1.Flipped == False:
                Bat1Flipped = pygame.transform.flip(Bat1.CurrentFrame, False, False)
            
            elif Bat1.Flipped == True:
                Bat1Flipped = pygame.transform.flip(Bat1.CurrentFrame, True, False)
            
            if Bat2.Flipped == False:
                Bat2Flipped = pygame.transform.flip(Bat2.CurrentFrame, False, False)
            
            elif Bat2.Flipped == True:
                Bat2Flipped = pygame.transform.flip(Bat2.CurrentFrame, True, False)

        #Render changes
        Screen.fill((66, 40, 53))
        
        #Top walls
        Screen.blit(Wall1.Image, (0, 0))
        Screen.blit(Wall4.Image, (64, 0))
        Screen.blit(Wall1.Image, (128, 0))
        Screen.blit(Wall2.Image, (192, 0))
        Screen.blit(Wall1.Image, (256, 0))
        Screen.blit(Wall5.Image, (320, 0))
        Screen.blit(Stairs.Image, (384, -32))
        Screen.blit(Wall1.Image, (576, 0))
        Screen.blit(Wall4.Image, (640, 0))
        Screen.blit(Wall1.Image, (704, 0))
        Screen.blit(Wall3.Image, (768, 0))
        Screen.blit(Wall1.Image, (832, 0))
        Screen.blit(Wall5.Image, (896, 0))

        #Left walls
        Screen.blit(Wall4.Image, (896, 64))
        Screen.blit(Wall1.Image, (896, 128))
        Screen.blit(Wall1.Image, (896, 192))
        Screen.blit(Wall5.Image, (896, 256))
        Screen.blit(Wall1.Image, (896, 320))
        Screen.blit(Wall4.Image, (896, 384))
        Screen.blit(Wall4.Image, (896, 448))
        Screen.blit(Wall1.Image, (896, 518))
        
        #Right walls
        Screen.blit(Wall5.Image, (0, 64))
        Screen.blit(Wall4.Image, (0, 128))
        Screen.blit(Wall1.Image, (0, 192))
        Screen.blit(Wall1.Image, (0, 256))
        Screen.blit(Wall4.Image, (0, 320))
        Screen.blit(Wall4.Image, (0, 384))
        Screen.blit(Wall1.Image, (0, 448))
        Screen.blit(Wall5.Image, (0, 518))

        #Bottom walls
        Screen.blit(Wall1.Image, (64, 518))
        Screen.blit(Wall4.Image, (128, 518))
        Screen.blit(Wall4.Image, (192, 518))
        Screen.blit(Wall1.Image, (256, 518))
        Screen.blit(Wall5.Image, (320, 518))
        Screen.blit(Stairs.Image, (384, 518))
        Screen.blit(Wall5.Image, (576, 518))
        Screen.blit(Wall1.Image, (640, 518))
        Screen.blit(Wall4.Image, (704, 518))
        Screen.blit(Wall1.Image, (768, 518))
        Screen.blit(Wall1.Image, (832, 518))

        if Room == 0:
            Title = LargeFont.render('Crossrain', False, (255, 255, 255))
            StartPrompt = SmallFont.render('Enter to start', False, (255, 255, 255))
            MoveInstructions = SmallFont.render('WASD or arrow keys to move/aim', False, (255, 255, 255))
            Version = MediumFont.render('v0.2.1', False, (255, 255, 255))
            
            Screen.blit(Title, (260, 75))
            Screen.blit(StartPrompt, (370, 200))
            Screen.blit(MoveInstructions, (30, 500))
            Screen.blit(Version, (800, 500))
        else:
            CurrentRoom = MediumFont.render('Room:'+str(Room), False, (255, 255, 255))
            
            Screen.blit(PlayerFlipped, PlayerRect)
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
            
            if Bat1.Alive == True:
                Screen.blit(Bat1Flipped, (Bat1Rect))
            
            if Bat2.Alive == True:
                Screen.blit(Bat2Flipped, (Bat2Rect))
            
            if Player.Health > 2:
                Screen.blit(PlayerHealth.Image, (800, 450))
            
            if Player.Health > 1:
                Screen.blit(PlayerHealth.Image, (700, 450))
            
            if Player.Health > 0:
                Screen.blit(PlayerHealth.Image, (600, 450))
            
            Screen.blit(CurrentRoom, (750, 15))

        Screen.blit(FPSText, (25, 15))
        
        Window.blit(pygame.transform.scale(Screen, Window.get_rect().size), (0, 0))
        pygame.display.flip()
        
        #Game exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False

        if not Running:
            pygame.quit()
            return

        await asyncio.sleep(0)

asyncio.run(Game())
