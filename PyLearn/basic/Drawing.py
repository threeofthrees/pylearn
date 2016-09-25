'''
Created on Sep 24, 2016

@author: Three
'''
import pygame
import sys
from pygame.locals import *

pygame.init()

# set up the display window
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Drawing')


# set up the colors
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)


# draw on the surface object
DISPLAYSURF.fill(WHITE)
# polygon (pentagon)
pygame.draw.polygon(DISPLAYSURF, GREEN, ((100, 0), (150, 0), (200, 50), (150, 100), (100, 100), (50, 50)))

# lines
pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120), 4)
pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)

# circles
pygame.draw.circle(DISPLAYSURF, RED, (200, 100), 50, 10)

# ellipses
pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 70, 40), 10)

# rectangle
pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))


pixObject = pygame.PixelArray(DISPLAYSURF)
pixObject[480][380] = BLACK
pixObject[482][382] = BLACK
pixObject[484][384] = BLACK
pixObject[486][386] = BLACK
pixObject[488][388] = BLACK

del pixObject

# main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
