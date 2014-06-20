#paste code here
import pygame, sys

pygame.init() #initialising pygame

screen= pygame.display.set_mode([300, 200]) #sets screen size

r = pygame.Color("red") #set variable r to colour red in pygame
w = pygame.Color("white") #set variable w to colour white in pygame

data = [                                  #array containing graphics
    [ w, w, w, w, r, r, r, r, w, w, w, w],
    [ w, r, r, r, r, r, r, r, r, r, r, w],
    [ r, r, r, r, r, r, r, r, r, r, r, r],
    [ r, r, r, w, w, r, r, w, w, r, r, r],
    [ r, r, r, r, r, r, r, r, r, r, r, r],
    [ w, w, w, r, r, w, w, r, r, w, w, w],
    [ w, w, r, r, w, r, r, w, r, r, w, w],
    [ r, r, w, w, w, w, w, w, w, w, r, r],
    ]

for y, row in enumerate(data): #places coloured blocks in order from array
    for x, colour in enumerate(row):
        rect = pygame.Rect (x*25, y*25, 25, 25) #each square is 25 pixels by 25 pixels
        screen.fill(colour, rect=rect)

pygame.display.update() #updating display

while True: #will always stay on screen
    for event in pygame.event.get(): #makes graphic appear on screen
        if event.type == pygame.QUIT: #allows user to exit
            sys.exit()
