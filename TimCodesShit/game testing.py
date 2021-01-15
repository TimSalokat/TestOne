import pygame
from pygame.locals import *

spriteFolder = "TimCodesShit/sprites/"

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
        self.vel = 2
        self.jumping = False
        self.jumpCount = 8

        self.spriteRight = pygame.image.load(spriteFolder + 'personFacingRight.png')
        self.spriteLeft = pygame.image.load(spriteFolder + "personFacingLeft.png")
        self.activeSprite = self.spriteRight

class Floor:
    def __init__(self):
        self.y = height - 100
        self.x = 0   
        self.floor = pygame.draw.rect(screen, (150, 0, 150), (self.x , self.y, 1000, 150))

floor = Floor()
player = Player()

while loop:
    pygame.time.delay(25)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]: 
        player.x -= player.vel
        player.activeSprite = player.spriteLeft

    if keys[pygame.K_RIGHT]:  
        player.x += player.vel
        player.activeSprite = player.spriteRight
        
    if not(player.jumping): 
        if keys[pygame.K_UP]:
            player.jumping = True
    else:
        nextCollide = floor.floor.collidepoint(player.x, player.y) 
        print(nextCollide)
        if nextCollide != 1:
            player.jumpCount -= 1
        else: 
            player.jumpCount = 8
            player.jumping = False
    
    screen.fill((0,0,0))
    floor.floor = pygame.draw.rect(screen, (150, 0, 150), (floor.x, floor.y, 1000, 150))    
    screen.blit(player.activeSprite, (player.x, player.y))
    pygame.display.flip() 
    clock.tick(100)

pygame.quit()
