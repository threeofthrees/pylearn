'''
Created on Sep 25, 2016

@author: Three
'''
import pygame
import sys
from pygame.locals import *

pygame.init()

FPS = 30  # frames per second setting
fpsClock = pygame.time.Clock()

# set up window

DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Cat Animation')

# colors
WHITE = (255, 255, 255)

catImage = pygame.image.load('cat.png')
catX = 10
catY = 10
direction = 'right'

while True: 
    DISPLAYSURF.fill(WHITE)
    
    if direction == 'right':
        catX += 5
        if catX == 280:
            direction = 'down'
    elif direction == 'down':
        catY += 5
        if catY == 220:
            direction = 'left'
    elif direction == 'left':
        catX -= 5
        if catX == 10:
            direction = 'up'
    elif direction == 'up':
        catY -= 5
        if catY == 10:
            direction = 'right'
    
    DISPLAYSURF.blit(catImage, (catX,catY))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
    
    fpsClock.tick(FPS)