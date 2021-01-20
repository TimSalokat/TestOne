
import pyautogui
import pygame
import os
import time

from pygame.locals import *
from termcolor import colored

#---defining functions---

#its just shorter than os.system()
def com(command):
    os.system(command)

#fast way to clear the screen
def clear():
    com("clear")

#just a void function for else statements
def void():
    return 0

#stuff in color
def debug(message = "Working", color = "green"):
    print(colored(message, color))

#---pre code aka defining shit---
mouseData = False
screenX = 720
screenY = 480

pygame.init()
screen = pygame.display.set_mode((screenX, screenY))

#---cool code---

#loop till you quit
while True:

    #wait a moment. For less impact on cpu and ram
    time.sleep(0.001)

    #fill screen with black, update the screen, define event, set caption, define rect
    event = pygame.event.poll()
    pygame.display.set_caption("Mouse tracker")

    #draw lines    if mouseData == True:
    screen.fill((1,1,1))
    if mouseData == True:
        pygame.draw.rect(screen,(255,0,0),(int(positionStrX),0,0,screenY)) #off left,off top, len right, len top
        pygame.draw.rect(screen,(0,0,255),(0,int(positionStrY),screenX,0))

    #check if event is quit
    if event.type == pygame.QUIT:
        break
    #check if event is mouse motion
    elif event.type == pygame.MOUSEMOTION:
        if mouseData == False:
            mouseData = True

        mousePosition = "%d %d" % event.pos
        mousePosition = mousePosition.split()
        positionStrX = mousePosition[0]
        positionStrY = mousePosition[1]
        positionStr = str("X: " + positionStrX + ", Y: " + positionStrY)
        clear()
        debug(positionStr, "blue")
    pygame.display.update()