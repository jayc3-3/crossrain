import asyncio
import pygame
import math
from objects import Player
from objects import WoodenSword
from objects import ZombieOne
from objects import ZombieTwo
from objects import WallFront1

# Try explicitly to declare all your globals at once to facilitate compilation later.
player = Player()
wsword = WoodenSword()
zomb1 = ZombieOne()
zomb2 = ZombieTwo()
wf1 = WallFront1()

# Do init here and load any assets right now to avoid lag at runtime or network errors.

pygame.init()
bgc = (66, 40, 53)
actualscreen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
drawscreen = actualscreen.copy()
clock = pygame.time.Clock()
width = pygame.display.Info().current_w
height = pygame.display.Info().current_h
titlefont = pygame.font.Font('./PublicPixel.ttf', 75)
startfont = pygame.font.Font('./PublicPixel.ttf', 25)
roomfont = pygame.font.Font('./PublicPixel.ttf', 40)
fpsfont = pygame.font.Font('./PublicPixel.ttf', 35)
pygame.display.set_caption("Crossrain")
print("Game version: 0.1.0")
titlesurface = titlefont.render("Crossrain", True, (255, 255, 255))
startsurface = startfont.render("Start", True, (255, 255, 255))
startrect = startsurface.get_rect()
startrect.centerx = actualscreen.get_rect().centerx
startrect.centery = int(height/2.5)

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
    woodswordrotated = pygame.transform.rotate(wsword.image, wrotang)

    zombie1 = False
    zombie2 = False
    
    zombie1x = 0
    zombie1y = 0
    zombie2x = 0
    zombie2y = 0
    weaponx = 0
    weapony = 0
    
    while True:
        drawscreen.fill(bgc)
        mousex, mousey = pygame.mouse.get_pos()
        weaponx, weapony = mousex, mousey
        relx, rely = (mousex - playerx), (mousey - playery)
        clock.tick()
        fps = round(clock.get_fps())
        fpsstr = str(fps)
        fpstext = "FPS:" + fpsstr
        DeltaTime = clock.tick(60) / 1000
        roomtext = "Room:" + str(room)
        
        wrotang = int(math.degrees(math.atan2(-rely, relx)) - 90)

        fpssurface = fpsfont.render(fpstext, False, (255, 255, 255))
        roomsurface = roomfont.render(roomtext, False, (255, 255, 255))
        roomrect = roomsurface.get_rect()
        roomrect.centerx = int(width/1.15)
        roomrect.centery = int(height/25)

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
        wswordrect = wsword.image.get_rect(topleft=(weaponx, weapony))
        playerrect = player.image.get_rect(topleft=(playerx, playery))

        woodswordrotated = pygame.transform.rotate(wsword.image, wrotang)

        if room == 0:
            zombie1 = False
            zombie2 = False
            zombie1x = 0
            zombie1y = 0
            zombie2x = 0
            zombie2y = 0
            playerweapon = 0

        if roomcompleted == True:
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
                zombie1x = 100
                zombie1y = 150
                zombie2x = 1116
                zombie2y = 150
                zombie1 = True
                zombie2 = True
                
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if startrect.collidepoint((mousex, mousey)):
                    room = 1
        
        if not room == 0:
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
            if playerx < zombie1x-50:
                zombie1x -= 5
            elif playerx > zombie1x+50:
                zombie1x += 5
            if playery < zombie1y-50:
                zombie1y -=5
            elif playery > zombie1y+50:
                zombie1y += 5
            if zombie1rect.colliderect(wswordrect):
                enemies = enemies - 1
                zombie1 = False
            elif zombie1rect.colliderect(playerrect):
                enemies = 0
                room = 0
                playerx = 605
                playery = 325
                
        if zombie2 == True:
            if playerx < zombie2x-50:
                zombie2x -= 5
            elif playerx > zombie2x+50:
                zombie2x += 5
            if playery < zombie2y-50:
                zombie2y -=5
            elif playery > zombie2y+50:
                zombie2y += 5
            if zombie2rect.colliderect(wswordrect):
                enemies = enemies - 1
                zombie2 = False
            elif zombie2rect.colliderect(playerrect):
                enemies = 0
                room = 0
                playerx = 605
                playery = 325

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
        if not room == 0:
            drawscreen.blit(playerflipped, playerrect)
            drawscreen.blit(roomsurface, roomrect)
            if room > 1:
                if playerweapon == 1:
                    drawscreen.blit(woodswordrotated, (weaponx, weapony))
        else:
            drawscreen.blit(titlesurface, (300, 150))
            drawscreen.blit(startsurface, startrect)

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
