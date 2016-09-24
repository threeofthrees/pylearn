'''
Created on Sep 23, 2016

@author: Three
'''
import pygame, sys
from pygame.locals import *
'''
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World')

while True:  # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
'''

listOfCars = ['Aston Martin', 'Jeep', 'Honda Accord', 'Range Rover', 'BMW 7 Series']
listOfSchools = ['Wake Forest', 'SUNY Downstate', 'NYCOM', 'PCOM']
listOfFootballers = ['Frank Lampard', 'Gareth Bale', 'Cristiano Ronaldo', 'Didier Drogba', 'John Terry']
listOfNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

listOfLists = [listOfCars, listOfSchools, listOfFootballers]

print(listOfLists[1])
print(len(listOfCars))
