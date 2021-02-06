import pygame, sys
from pygame.locals import *
pygame.init()

windowWidth, windowHeight = 700, 700
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Game")

class Player:
    def __init__(self):
        self.x = 50
        self.y = 50
        self.width = 40
        self.height = 60
        self.vel = 5

red = Player()

loop = True
while loop:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and red.x > red.vel:
        red.x -= red.vel
    if keys[pygame.K_RIGHT] and red.x < windowWidth - red.width - red.vel:
        red.x += red.vel
    if keys[pygame.K_UP] and red.y > red.vel:
        red.y -= red.vel
    if keys[pygame.K_DOWN] and red.y < windowHeight - red.height - red.vel:
        red.y += red.vel

    pygame.draw.rect(window, (255,0,0), (red.x, red.y, red.width, red.height))
    
    pygame.display.update()
    window.fill((0,0,0))    

pygame.quit()