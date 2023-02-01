import asyncio
import pygame
import time
from objects import WindowIcon
from objects import Player
from objects import WoodenSword
from objects import ZombieOne
from objects import ZombieTwo
from objects import Demon
from objects import DemonTwo
from objects import DemonSpawnOne
from objects import DemonSpawnTwo
from objects import DemonSpawnThree
from objects import DemonSpawnFour
from objects import DemonSpawnFive
from objects import DemonSpawnSix
from objects import WallFront1

# Try explicitly to declare all your globals at once to facilitate compilation later.
player = Player()
wsword = WoodenSword()
zomb1 = ZombieOne()
zomb2 = ZombieTwo()
dem = Demon()
dem2 = DemonTwo()
dems1 = DemonSpawnOne()
dems2 = DemonSpawnTwo()
dems3 = DemonSpawnThree()
dems4 = DemonSpawnFour()
dems5 = DemonSpawnFive()
dems6 = DemonSpawnSix()
wf1 = WallFront1()

# Do init here and load any assets right now to avoid lag at runtime or network errors.

pygame.init()
width = pygame.display.Info().current_w
height = pygame.display.Info().current_h
bgc = (66, 40, 53)
pygame.display.set_icon(WindowIcon().image)
actualscreen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
drawscreen = actualscreen.copy()
clock = pygame.time.Clock()
titlefont = pygame.font.Font('./PublicPixel.ttf', 75)
startfont = pygame.font.Font('./PublicPixel.ttf', 25)
versionfont = pygame.font.Font('./PublicPixel.ttf', 20)
instructionfont = pygame.font.Font('./PublicPixel.ttf', 15)
roomfont = pygame.font.Font('./PublicPixel.ttf', 40)
fpsfont = pygame.font.Font('./PublicPixel.ttf', 35)
pygame.display.set_caption("Crossrain")
titlesurface = titlefont.render("Crossrain", False, (255, 255, 255))
startsurface = startfont.render("Start", False, (255, 255, 255))
selectsurface = startfont.render(">", False, (255, 255, 255))
instructionsurface = instructionfont.render("Enter to start, WASD to move/aim", False, (255, 255, 255))
versionsurface = versionfont.render("v0.1.2", False, (255, 255, 255))

async def main():
    running = True
    playerx = 605
    playery = 325
    wrotang = 0
    wrotang = int(wrotang)
    room = 0
    roomcompleted = False
    enemies = 0
    playerweapon = 0
    playerflipped = pygame.transform.flip(player.image, False, False)
    zombie1flipped = pygame.transform.flip(zomb1.image, False, False)
    zombie2flipped = pygame.transform.flip(zomb2.image, False, False)
    demflipped = pygame.transform.flip(dem.image, False, False)
    dem2flipped = pygame.transform.flip(dem2.image, False, False)
    ds1flipped = pygame.transform.flip(dems1.image, False, False)
    ds2flipped = pygame.transform.flip(dems2.image, False, False)
    ds3flipped = pygame.transform.flip(dems3.image, False, False)
    ds4flipped = pygame.transform.flip(dems4.image, False, False)
    ds5flipped = pygame.transform.flip(dems5.image, False, False)
    ds6flipped = pygame.transform.flip(dems6.image, False, False)
    
    zombie1 = False
    zombie2 = False
    demon = False
    demon2 = False
    demonspawn1 = False
    demonspawn2 = False
    demonspawn3 = False
    demonspawn4 = False
    demonspawn5 = False
    demonspawn6 = False
    
    zombie1x = 0
    zombie1y = 0
    zombie2x = 0
    zombie2y = 0
    demonx = 0
    demony = 0
    demon2x = 0
    demon2y = 0
    ds1x = 0
    ds1y = 0
    ds2x = 0
    ds2y = 0
    ds3x = 0
    ds3y = 0
    ds4x = 0
    ds4y = 0
    ds5x = 0
    ds5y = 0
    ds6x = 0
    ds6y = 0
    weaponx = 0
    weapony = 0
    selector = 1
    do_once = 0
    do_once2 = 0
    demonspawn = 0
    demon2spawn = 0
    start = 0
    current = 0
    elapsed = 0
    start2 = 0
    current2 = 0
    elapsed2 = 0
    
    while True:
        drawscreen.fill(bgc)
        #mousex, mousey = pygame.mouse.get_pos()
        #weaponx, weapony = mousex, mousey
        #relx, rely = (mousex - playerx), (mousey - playery)
        clock.tick()
        fps = round(clock.get_fps())
        fpsstr = str(fps)
        fpstext = "FPS:" + fpsstr
        DeltaTime = clock.tick(60) / 1000
        roomtext = "Room:" + str(room)

        #wrotang = int(math.degrees(math.atan2(-rely, relx)) - 90)

        fpssurface = fpsfont.render(fpstext, False, (255, 255, 255))
        roomsurface = roomfont.render(roomtext, False, (255, 255, 255))

        #if pygame.key.get_pressed()[pygame.K_w]:
            #Selector stuff here
        
        if room == 0:
            if selector == 1:
                selectx = 550
                selecty = 295
                if pygame.key.get_pressed()[pygame.K_RETURN]:
                    enemies = 0
                    room = 1
            zombie1 = False
            zombie2 = False
            demon = False
            demon2 = False
            demonspawn1 = False
            demonspawn2 = False
            demonspawn3 = False
            demonspawn4 = False
            demonspawn5 = False
            demonspawn6 = False
            zombie1x = 0
            zombie1y = 0
            zombie2x = 0
            zombie2y = 0
            demonx = 0
            demony = 0
            demon2x = 0
            demon2y = 0
            ds1x = 0
            ds1y = 0
            ds2x = 0
            ds2y = 0
            ds3x = 0
            ds3y = 0
            ds4x = 0
            ds4y = 0
            ds5x = 0
            ds5y = 0
            ds6x = 0
            ds6y = 0
            enemies = 0
            playerweapon = 0
            do_once = 0
            do_once2 = 0
            start = 0
            current = 0
            elapsed = 0
            start2 = 0
            current2 = 0
            elapsed2 = 0
            
            

        if weaponx < playerx-82:
            weaponx = playerx-82
        elif weaponx > playerx+82:
            weaponx = playerx+82
        
        if weapony < playery-82:
            weapony = playery-82
        elif weapony > playery+82:
            weapony = playery+82

        zombie1rect = zomb1.image.get_rect(topleft=(zombie1x, zombie1y))
        zombie2rect = zomb2.image.get_rect(topleft=(zombie2x, zombie2y))
        demonrect = dem.image.get_rect(topleft=(demonx, demony))
        demon2rect = dem2.image.get_rect(topleft=(demon2x, demon2y))
        ds1rect = dems1.image.get_rect(topleft=(ds1x, ds1y))
        ds2rect = dems2.image.get_rect(topleft=(ds2x, ds2y))
        ds3rect = dems3.image.get_rect(topleft=(ds3x, ds3y))
        ds4rect = dems4.image.get_rect(topleft=(ds4x, ds4y))
        ds5rect = dems5.image.get_rect(topleft=(ds5x, ds5y))
        ds6rect = dems6.image.get_rect(topleft=(ds6x, ds6y))
        wswordrect = wsword.image.get_rect(topleft=(weaponx, weapony))
        playerrect = player.image.get_rect(topleft=(playerx, playery))

        woodswordrotated = pygame.transform.rotate(wsword.image, wrotang)

        if roomcompleted == True:
            do_once = 0
            do_once2 = 0
            start = 0
            start2 = 0
            current = 0
            current2 = 0
            elapsed = 0
            elapsed2 = 0
            if room == 1:
                roomcompleted = False
                room = 2
                enemies = 1
                playerweapon = 1
                zombie1x = 605
                zombie1y = 100
                zombie1 = True
            elif room == 2:
                roomcompleted = False
                room = 3
                enemies = 2
                playerweapon = 1
                zombie1x = 400
                zombie1y = 100
                zombie2x = 800
                zombie2y = 100
                zombie1 = True
                zombie2 = True
            elif room == 3:
                roomcompleted = False
                room = 4
                enemies = 1
                playerweapon = 1
                zombie1x = 100
                zombie1y = 600
                zombie1 = True
            elif room == 4:
                roomcompleted = False
                room = 5
                enemies = 2
                playerweapon = 1
                zombie1x = 400
                zombie1y = 600
                zombie2x = 800
                zombie2y = 600
                zombie1 = True
                zombie2 = True
            elif room == 5:
                roomcompleted = False
                room = 6
                enemies = 1
                playerweapon = 1
                demonx = 570
                demony = 100
                demonspawn = 0
                demon = True
            elif room == 6:
                roomcompleted = False
                room = 7
                enemies = 3
                playerweapon = 1
                demonx = 570
                demony = 100
                zombie1x = 400
                zombie1y = 600
                zombie2x = 800
                zombie2y = 600
                demonspawn = 0
                demon = True
                zombie1 = True
                zombie2 = True
            elif room == 7:
                enemies = 3
                playerweapon = 1
                demonx = 50
                demony = 75
                zombie1x = 50
                zombie1y = 600
                zombie2x = 1100
                zombie2y = 75
                demonspawn = 0
                room = 8
                time.sleep(0.05)
                roomcompleted = False
                demon = True
                demonspawn1 = False
                demonspawn2 = False
                demonspawn3 = False
                zombie1 = True
                zombie2 = True
            elif room == 8:
                enemies = 3
                playerweapon = 1
                demonx = 1100
                demony = 200
                zombie1x = 1000
                zombie1y = 600
                zombie2x = 950
                zombie2y = 650
                demonspawn = 0
                room = 9
                time.sleep(0.05)
                roomcompleted = False
                demon = True
                demonspawn1 = False
                demonspawn2 = False
                demonspawn3 = False
                zombie1 = True
                zombie2 = True
            elif room == 9:
                enemies = 4
                playerweapon = 1
                demonx = 50
                demony = 100
                demon2x = 1100
                demon2y = 100
                zombie1x = 150
                zombie1y = 600
                zombie2x = 1000
                zombie2y = 650
                demonspawn = 0
                demon2spawn = 0
                room = 10
                time.sleep(0.05)
                roomcompleted = False
                demon = True
                demon2 = True
                demonspawn1 = False
                demonspawn2 = False
                demonspawn3 = False
                demonspawn4 = False
                demonspawn5 = False
                demonspawn6 = False
                zombie1 = True
                zombie2 = True
            elif room == 10:
                room = 0

        elif roomcompleted == False:
            if enemies == 0:
                if playerx > 495:
                    if playerx < 725:
                        if playery < 0:
                            playerx = 605
                            playery = 625
                            roomcompleted = True
            elif not enemies == 0:
                if playery < 0:
                    playery = 0

        if zombie1 == False:
            zombie1x = 0
            zombie1y = 0
        if zombie2 == False:
            zombie2x = 0
            zombie2y = 0
        if demon == False:
            demonx = 0
            demony = 0
        if demon2 == False:
            demon2x = 0
            demon2y = 0
        if demonspawn1 == False:
            ds1x = 0
            ds1y = 0
        if demonspawn2 == False:
            ds2x = 0
            ds2y = 0
        if demonspawn3 == False:
            ds3x = 0
            ds3y = 0
        if demonspawn4 == False:
            ds4x = 0
            ds4y = 0
        if demonspawn5 == False:
            ds5x = 0
            ds5y = 0
        if demonspawn6 == False:
            ds6x = 0
            ds6y = 0

        if playerx > 710:
            if playery < 80:
                playerx = 710
            elif playery < 100:
                playery = 100
        elif playerx < 510:
            if playery < 80:
                playerx = 510
            elif playery < 100:
                playery = 100
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if not room == 0:
            if pygame.key.get_pressed()[pygame.K_w]:
                if pygame.key.get_pressed()[pygame.K_a]:
                    wrotang = 45
                    weaponx, weapony = ((playerx - 100), (playery - 100))
                elif pygame.key.get_pressed()[pygame.K_d]:
                    wrotang = -45
                    weaponx, weapony = ((playerx + 100), (playery - 100))
                else:
                    wrotang = 0
                    weaponx, weapony = (playerx, (playery - 100))
            elif pygame.key.get_pressed()[pygame.K_s]:
                if pygame.key.get_pressed()[pygame.K_a]:
                    wrotang = 180-45
                    weaponx, weapony = ((playerx - 100), (playery + 100))
                elif pygame.key.get_pressed()[pygame.K_d]:
                    wrotang = 180+45
                    weaponx, weapony = ((playerx + 100), (playery + 100))
                else:
                    wrotang = 180
                    weaponx, weapony = (playerx, (playery + 100))
            elif pygame.key.get_pressed()[pygame.K_a]:
                if pygame.key.get_pressed()[pygame.K_w]:
                    wrotang = 45
                    weaponx, weapony = ((playerx - 100), (playery - 100))
                elif pygame.key.get_pressed()[pygame.K_s]:
                    wrotang = 180-45
                    weaponx, weapony = ((playerx - 100), (playery + 100))
                else:
                    wrotang = 90
                    weaponx, weapony = ((playerx - 100), (playery))
            elif pygame.key.get_pressed()[pygame.K_d]:
                if pygame.key.get_pressed()[pygame.K_w]:
                    wrotang = 45
                    weaponx, weapony = ((playerx + 100), (playery - 100))
                elif pygame.key.get_pressed()[pygame.K_s]:
                    wrotang = 180+45
                    weaponx, weapony = ((playerx + 100), (playery + 100))
                else:
                    wrotang = 270
                    weaponx, weapony = ((playerx + 100), (playery))
            woodswordrotated = pygame.transform.rotate(wsword.image, wrotang)
            
            if pygame.key.get_pressed()[pygame.K_w]:
                playery -= int(750 * DeltaTime)
        
            elif pygame.key.get_pressed()[pygame.K_s]:
                playery += int(750 * DeltaTime)
        
            if pygame.key.get_pressed()[pygame.K_a]:
                playerx -= int(750 * DeltaTime)
                playerflipped = pygame.transform.flip(player.image, True, False)
        
            elif pygame.key.get_pressed()[pygame.K_d]:
                playerx += int(750 * DeltaTime)
                playerflipped = pygame.transform.flip(player.image, False, False)
        
        if zombie1 == True:
            if playerx < zombie1x-25:
                zombie1x -= int(315 * DeltaTime)
            elif playerx > zombie1x+25:
                zombie1x += int(315 * DeltaTime)
            if playery < zombie1y-25:
                zombie1y -= int(315 * DeltaTime)
            elif playery > zombie1y+25:
                zombie1y += int(315 * DeltaTime)
            if zombie1rect.colliderect(wswordrect):
                enemies = enemies - 1
                zombie1 = False
            elif zombie1rect.colliderect(playerrect):
                enemies = 0
                room = 0
                playerx = 605
                playery = 325
                
        if zombie2 == True:
            if playerx < zombie2x-25:
                zombie2x -= int(315 * DeltaTime)
            elif playerx > zombie2x+25:
                zombie2x += int(315 * DeltaTime)
            if playery < zombie2y-25:
                zombie2y -= int(315 * DeltaTime)
            elif playery > zombie2y+25:
                zombie2y += int(315 * DeltaTime)
            if zombie2rect.colliderect(wswordrect):
                enemies = enemies - 1
                zombie2 = False
            elif zombie2rect.colliderect(playerrect):
                enemies = 0
                room = 0
                playerx = 605
                playery = 325

        if demonspawn1 == True:
            if playerx < ds1x-25:
                ds1x -= int(625 * DeltaTime)
            elif playerx > ds1x+25:
                ds1x += int(625 * DeltaTime)
            if playery < ds1y-25:
                ds1y -= int(625 * DeltaTime)
            elif playery > ds1y+25:
                ds1y += int(625 * DeltaTime)
            if ds1rect.colliderect(wswordrect):
                enemies = enemies - 1
                demonspawn1 = False
            elif ds1rect.colliderect(playerrect):
                enemies = 0
                room = 0
                playerx = 605
                playery = 325
        if demonspawn2 == True:
            if playerx < ds2x-25:
                ds2x -= int(625 * DeltaTime)
            elif playerx > ds2x+25:
                ds2x += int(625 * DeltaTime)
            if playery < ds2y-25:
                ds2y -= int(625 * DeltaTime)
            elif playery > ds2y+25:
                ds2y += int(625 * DeltaTime)
            if ds2rect.colliderect(wswordrect):
                enemies = enemies - 1
                demonspawn2 = False
            elif ds2rect.colliderect(playerrect):
                enemies = 0
                room = 0
                playerx = 605
                playery = 325
        if demonspawn3 == True:
            if playerx < ds3x-25:
                ds3x -= int(625 * DeltaTime)
            elif playerx > ds3x+25:
                ds3x += int(625 * DeltaTime)
            if playery < ds3y-25:
                ds3y -= int(625 * DeltaTime)
            elif playery > ds3y+25:
                ds3y += int(625 * DeltaTime)
            if ds3rect.colliderect(wswordrect):
                enemies = enemies - 1
                demonspawn3 = False
            elif ds3rect.colliderect(playerrect):
                enemies = 0
                room = 0
                playerx = 605
                playery = 325
        if demonspawn4 == True:
            if playerx < ds4x-25:
                ds4x -= int(625 * DeltaTime)
            elif playerx > ds4x+25:
                ds4x += int(625 * DeltaTime)
            if playery < ds4y-25:
                ds4y -= int(625 * DeltaTime)
            elif playery > ds4y+25:
                ds4y += int(625 * DeltaTime)
            if ds4rect.colliderect(wswordrect):
                enemies = enemies - 1
                demonspawn4 = False
            elif ds4rect.colliderect(playerrect):
                enemies = 0
                room = 0
                playerx = 605
                playery = 325
        if demonspawn5 == True:
            if playerx < ds5x-25:
                ds5x -= int(625 * DeltaTime)
            elif playerx > ds5x+25:
                ds5x += int(625 * DeltaTime)
            if playery < ds5y-25:
                ds2y -= int(625 * DeltaTime)
            elif playery > ds5y+25:
                ds5y += int(625 * DeltaTime)
            if ds5rect.colliderect(wswordrect):
                enemies = enemies - 1
                demonspawn5 = False
            elif ds5rect.colliderect(playerrect):
                enemies = 0
                room = 0
                playerx = 605
                playery = 325
        if demonspawn6 == True:
            if playerx < ds6x-25:
                ds6x -= int(625 * DeltaTime)
            elif playerx > ds6x+25:
                ds6x += int(625 * DeltaTime)
            if playery < ds6y-25:
                ds6y -= int(625 * DeltaTime)
            elif playery > ds6y+25:
                ds6y += int(625 * DeltaTime)
            if ds6rect.colliderect(wswordrect):
                enemies = enemies - 1
                demonspawn6 = False
            elif ds6rect.colliderect(playerrect):
                enemies = 0
                room = 0
                playerx = 605
                playery = 325
        
        if demon == True:
            if demonspawn < 3:
                if elapsed > 1:
                    elapsed = 0
                    enemies = enemies+1
                    if demonspawn == 0:
                        ds1x = demonx + 32
                        ds1y = demony + 32
                        demonspawn = 1
                        demonspawn1 = True
                    elif demonspawn == 1:
                        ds2x = demonx + 32
                        ds2y = demony + 32
                        demonspawn = 2
                        demonspawn2 = True
                    elif demonspawn == 2:
                        ds3x = demonx + 32
                        ds3y = demony + 32
                        demonspawn3 = True
                        demonspawn = 3
                    do_once = 0
                if do_once == 0:
                    do_once = 1
                    start = time.time()
                current = time.time()
                elapsed = (current - start)
            if demonrect.colliderect(wswordrect):
                enemies = enemies-1
                demon = False
            elif demonrect.colliderect(playerrect):
                enemies = 0
                room = 0
                playerx = 605
                playery = 325

            if demonx < playerx - 350:
                demonx += int(190 * DeltaTime)
            elif demonx > playerx + 350:
                demonx -= int(190 * DeltaTime)
            
            if demony < playery - 350:
                demony += int(190 * DeltaTime)
            elif demony > playery + 350:
                demony -= int(190 * DeltaTime)
                
        if demon2 == True:
            if demon2spawn < 3:
                if elapsed2 > 1:
                    elapsed2 = 0
                    enemies = enemies+1
                    if demon2spawn == 0:
                        ds4x = demon2x + 32
                        ds4y = demon2y + 32
                        demon2spawn = 1
                        demonspawn4 = True
                    elif demon2spawn == 1:
                        ds5x = demon2x + 32
                        ds5y = demon2y + 32
                        demon2spawn = 2
                        demonspawn5 = True
                    elif demon2spawn == 2:
                        ds6x = demon2x + 32
                        ds6y = demon2y + 32
                        demonspawn6 = True
                        demon2spawn = 3
                    do_once2 = 0
                if do_once2 == 0:
                    do_once2 = 1
                    start2 = time.time()
                current2 = time.time()
                elapsed2 = (current2 - start2)
            if demon2rect.colliderect(wswordrect):
                enemies = enemies-1
                demon2 = False
            elif demon2rect.colliderect(playerrect):
                enemies = 0
                room = 0
                playerx = 605
                playery = 325

            if demon2x < playerx - 350:
                demon2x += int(190 * DeltaTime)
            elif demon2x > playerx + 350:
                demon2x -= int(190 * DeltaTime)
            
            if demon2y < playery - 350:
                demon2y += int(190 * DeltaTime)
            elif demon2y > playery + 350:
                demon2y -= int(190 * DeltaTime)

        drawscreen.blit(wf1.image, (0, 0))
        drawscreen.blit(wf1.image, (128, 0))
        drawscreen.blit(wf1.image, (256, 0))
        drawscreen.blit(wf1.image, (384, 0))
        drawscreen.blit(wf1.image, (768, 0))
        drawscreen.blit(wf1.image, (896, 0))
        drawscreen.blit(wf1.image, (1024, 0))
        drawscreen.blit(wf1.image, (1152, 0))
        if zombie1 == True:
            if playerx > zombie1x:
                zombie1flipped = pygame.transform.flip(zomb1.image, False, False)
            else:
                zombie1flipped = pygame.transform.flip(zomb1.image, True, False)
            drawscreen.blit(zombie1flipped, zombie1rect)
        if zombie2 == True:
            if playerx > zombie2x:
                zombie2flipped = pygame.transform.flip(zomb2.image, False, False)
            else:
                zombie2flipped = pygame.transform.flip(zomb2.image, True, False)
            drawscreen.blit(zombie2flipped, zombie2rect)
        if demonspawn1 == True:
            if playerx > ds1x:
                ds1flipped = pygame.transform.flip(dems1.image, False, False)
            else:
                ds1flipped = pygame.transform.flip(dems1.image, True, False)
            drawscreen.blit(ds1flipped, ds1rect)
        if demonspawn2 == True:
            if playerx > ds2x:
                ds2flipped = pygame.transform.flip(dems2.image, False, False)
            else:
                ds2flipped = pygame.transform.flip(dems2.image, True, False)
            drawscreen.blit(ds2flipped, ds2rect)
        if demonspawn3 == True:
            if playerx > ds3x:
                ds3flipped = pygame.transform.flip(dems3.image, False, False)
            else:
                ds3flipped = pygame.transform.flip(dems3.image, True, False)
            drawscreen.blit(ds3flipped, ds3rect)
        if demonspawn4 == True:
            if playerx > ds4x:
                ds4flipped = pygame.transform.flip(dems4.image, False, False)
            else:
                ds4flipped = pygame.transform.flip(dems4.image, True, False)
            drawscreen.blit(ds4flipped, ds4rect)
        if demonspawn5 == True:
            if playerx > ds5x:
                ds5flipped = pygame.transform.flip(dems5.image, False, False)
            else:
                ds5flipped = pygame.transform.flip(dems5.image, True, False)
            drawscreen.blit(ds5flipped, ds5rect)
        if demonspawn6 == True:
            if playerx > ds6x:
                ds6flipped = pygame.transform.flip(dems6.image, False, False)
            else:
                ds6flipped = pygame.transform.flip(dems6.image, True, False)
            drawscreen.blit(ds6flipped, ds6rect)
        if demon == True:
            if playerx > demonx:
                demflipped = pygame.transform.flip(dem.image, False, False)
            else:
                demflipped = pygame.transform.flip(dem.image, True, False)
            drawscreen.blit(demflipped, demonrect)
        if demon2 == True:
            if playerx > demon2x:
                dem2flipped = pygame.transform.flip(dem2.image, False, False)
            else:
                dem2flipped = pygame.transform.flip(dem2.image, True, False)
            drawscreen.blit(dem2flipped, demon2rect)
        if not room == 0:
            drawscreen.blit(playerflipped, playerrect)
            if room > 1:
                if playerweapon == 1:
                    drawscreen.blit(woodswordrotated, (weaponx, weapony))
            drawscreen.blit(roomsurface, (950, 15))
        else:
            drawscreen.blit(titlesurface, (300, 125))
            drawscreen.blit(startsurface, ((640-60), 300))
            drawscreen.blit(selectsurface, (selectx, selecty))
            drawscreen.blit(instructionsurface, (50, 675))
            drawscreen.blit(versionsurface, (1100, 675))

        drawscreen.blit(fpssurface, (35, 15))
        actualscreen.blit(pygame.transform.scale(drawscreen, actualscreen.get_rect().size), (0, 0))
        pygame.display.flip()

        if not running:
            pygame.quit()
            return

        await asyncio.sleep(0)  # Very important, and keep it 0

# This is the program entry point:
asyncio.run(main())
pygame.quit()

# Do not add anything from here
# asyncio.run is non-blocking on pygame-wasm
