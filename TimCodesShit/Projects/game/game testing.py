import pygame
from pygame.locals import *

spriteFolder = "TimCodesShit/Projects/game/sprites/"

pygame.init()
clock = pygame.time.Clock()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('GAME')
loop = True

class Player:
    def __init__(self):
        self.x = 200
        self.y = 300
        self.xvel = 2
        self.yvel = 15
        self.jumping = False
        self.jumpCount = 10
        self.falling = True

        self.spriteRight = pygame.image.load(spriteFolder + 'personFacingRight.png')
        self.spriteLeft = pygame.image.load(spriteFolder + "personFacingLeft.png")
        self.activeSprite = self.spriteRight

class Floor:
    def __init__(self):
        self.y = height - 100
        self.x = 0
        self.height = 150   
        self.floor = pygame.draw.rect(screen, (150, 0, 150), (self.x , self.y, 1000, self.height))

floor = Floor()
player = Player() 

while loop:
    pygame.time.delay(25)

    distance = floor.y - floor.height/2 - player.y
    if distance >= 7 and player.jumping != True:
        player.y += player.yvel
        player.falling = True
    else:
        player.falling = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]: 
        player.x -= player.xvel
        player.activeSprite = player.spriteLeft

    if keys[pygame.K_RIGHT]:  
        player.x += player.xvel
        player.activeSprite = player.spriteRight
        
    if not(player.falling):
        distance = floor.y - floor.height/2 - player.y
        if distance >= 7 and player.jumping != True:
            player.y += player.yvel
            player.falling = True

        if not(player.jumping): 
            if keys[pygame.K_UP]:
                player.jumping = True
        else:
            if player.jumping == True:
                if player.jumpCount >= 0:
                    player.y -= player.yvel
                    player.jumpCount -= 1
                else:
                    player.jumpCount = 10
                    player.jumping = False
            else: 
                player.jumpCount = 10
                player.jumping = False

    screen.fill((0,0,0))
    floor.floor = pygame.draw.rect(screen, (150, 0, 150), (floor.x, floor.y, 1000, floor.height))    
    screen.blit(player.activeSprite, (player.x, player.y))
    pygame.display.flip() 
    clock.tick(100)

pygame.quit()
