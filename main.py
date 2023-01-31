import asyncio
import pygame
from objects import Player
from objects import WallFront1

# Try explicitly to declare all your globals at once to facilitate compilation later.
player = Player()
wf1 = WallFront1()

# Do init here and load any assets right now to avoid lag at runtime or network errors.

pygame.init()
bgc = (66, 40, 53)
actualscreen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
drawscreen = actualscreen.copy()
clock = pygame.time.Clock()
fpsfont = pygame.font.Font('./PublicPixel.ttf', 35)
pygame.display.set_caption("Crossrain")
print("Game version: 0.1.0")

async def main():
    running = True
    playerx = 605
    playery = 325
    
    while True:
        drawscreen.fill(bgc)
        clock.tick()
        fps = round(clock.get_fps())
        fpsstr = str(fps)
        fpstext = "FPS:" + fpsstr
        DeltaTime = clock.tick(60) / 1000
        print(DeltaTime)
        
        fpssurface = fpsfont.render(fpstext, False, (255, 255, 255))
        
        if playerx > 710:
            if playery < 80:
                playerx = 710
            elif playery < 100:
                playery = 100
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if pygame.key.get_pressed()[pygame.K_w]:
            playery -= int(750 * DeltaTime)
        
        elif pygame.key.get_pressed()[pygame.K_s]:
            playery += int(750 * DeltaTime)
        
        if pygame.key.get_pressed()[pygame.K_a]:
            playerx -= int(750 * DeltaTime)
        
        elif pygame.key.get_pressed()[pygame.K_d]:
            playerx += int(750 * DeltaTime)
        print(playerx)
        print(playery)
        
        drawscreen.blit(wf1.image, (0, 0))
        drawscreen.blit(wf1.image, (128, 0))
        drawscreen.blit(wf1.image, (256, 0))
        drawscreen.blit(wf1.image, (384, 0))
        drawscreen.blit(wf1.image, (768, 0))
        drawscreen.blit(wf1.image, (896, 0))
        drawscreen.blit(wf1.image, (1024, 0))
        drawscreen.blit(wf1.image, (1152, 0))
        drawscreen.blit(player.image, (playerx, playery))
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