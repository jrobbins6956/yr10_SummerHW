#paste code here


### TASK 1

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
            
            
            
            





### TASK 2


import pygame, sys

pygame.init() #initialising pygame

screen= pygame.display.set_mode([300, 200]) #sets screen size

r = pygame.Color("red") #set variable r to colour red in pygame
w = pygame.Color("white") #set variable w to colour white in pygame

frame1 = [                                  #array containing graphics
    [ w, w, w, w, r, r, r, r, w, w, w, w],
    [ w, r, r, r, r, r, r, r, r, r, r, w],
    [ r, r, r, r, r, r, r, r, r, r, r, r],
    [ r, r, r, w, w, r, r, w, w, r, r, r],
    [ r, r, r, r, r, r, r, r, r, r, r, r],
    [ w, w, w, r, r, w, w, r, r, w, w, w],
    [ w, w, r, r, w, r, r, w, r, r, w, w],
    [ r, r, w, w, w, w, w, w, w, w, r, r],
    ]

frame2 = [                                  #array containing graphics
    [ w, w, r, w, w, w, w, w, w, r, w, w],
    [ w, w, w, r, w, w, w, w, r, w, w, w],
    [ w, w, r, r, r, r, r, r, r, r, w, w],
    [ w, r, r, w, r, r, r, r, w, r, r, w],
    [ r, r, r, r, r, r, r, r, r, r, r, r],
    [ r, w, r, r, r, r, r, r, r, r, w, r],
    [ r, w, r, w, w, w, w, w, w, r, w, r],
    [ w, w, w, r, r, w, w, r, r, w, w, w],
    ]


def draw_frame(surface, data):
    for y, row in enumerate(data): #places coloured blocks in order from array
        for x, colour in enumerate(row):
            rect = pygame.Rect (x*25, y*25, 25, 25) #each square is 25 pixels by 25 pixels
            screen.fill(colour, rect=rect)

pygame.display.update() #refresh display

while True: #will always stay on screen
    for event in pygame.event.get(): #makes graphic appear on screen
        if event.type == pygame.QUIT: #allows user to exit
            sys.exit()
    draw_frame(screen, frame1) #displays frame1
    pygame.display.update() 
    pygame.time.wait(500) #wait 500
    draw_frame(screen, frame2) #display frame2
    pygame.display.update()
    pygame.time.wait(500) #wait 500











### TASK 3


import pygame, sys

pygame.init() #initialising pygame
import time #importing time function

screen= pygame.display.set_mode([580, 300]) #sets screen size

o = pygame.Color("orange") #set variable r to colour red in pygame
w = pygame.Color("white") #set variable w to colour white in pygame
g = pygame.Color("green") #set variable g to colour green in pygame
b = pygame.Color("blue") #set variable b to colour blue in pygame
d = pygame.Color("black") #set variable d to colour black in pygame

frame1 = [
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, d, d, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, o, o, o, d, d, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, o, o, o, o, o, o, b, b, b, b, b, b, b, b, g, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, o, o, o, o, o, b, b, b, b, b, b, b, b, g, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, o, o, o, o, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, o, o, o, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, o, o, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    ]
    

frame2 = [
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, d, d, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, o, o, o, d, d, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, g, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, g, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, o, o, o, o, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, o, o, o, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, o, o, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    ]

frame3 = [
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, d, d, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, o, o, o, d, d, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, o, o, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    ]

frame4 = [
    [ b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, d, d, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, w, b, o, o, o, d, d, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    ]

frame5 = [
    [ b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, w, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, d, d, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, w, b, o, o, o, d, d, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    ]

frame6 = [
    [ b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, w, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, w, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, o, o, o, d, d, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, w, b, o, o, o, d, d, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    ]

frame7 = [
    [ b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, w, b, b, b, b, b, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, w, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, w, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, o, o, o, d, d, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, w, b, o, o, o, d, d, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    ]

frame8 = [
    [ b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, w, b, b, b, b, b, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, w, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, w, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, o, o, o, d, d, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, w, b, o, o, o, d, d, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    ]

frame9 = [
    [ b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, w, b, b, b, b, b, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, w, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, w, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, o, o, o, d, d, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, w, b, o, o, o, d, d, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, g, g, b],
    [ b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    ]

frame10 = [
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, o, o, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, o, o, o, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, o, o, o, o, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, o, o, o, o, o, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, o, o, o, o, o, o, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, d, d, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, d, d, o, o, o, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, o, o, o, o, o, o, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, g, g, b],
    [ b, b, b, b, b, b, o, o, o, o, o, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, g, g, b],
    [ b, b, b, b, b, b, o, o, o, o, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, o, o, o, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, o, o, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    ]

frame11 = [
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, o, o, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, o, o, o, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, o, o, o, o, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, o, o, o, o, o, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, o, o, o, o, o, o, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, d, d, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, d, d, o, o, o, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, o, o, o, o, o, o, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, o, o, o, o, o, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, o, o, o, o, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, o, o, o, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, o, o, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    ]

frame12 = [
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, o, o, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, o, o, o, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, o, o, o, o, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, d, d, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, d, d, o, o, o, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, o, o, o, o, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, o, o, o, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, o, o, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    ]

frame13 = [
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, o, o, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, d, d, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, d, d, o, o, o, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, o, o, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    ]

frame14 = [
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, d, d, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, d, d, o, o, o, b, w, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    ]

frame15 = [
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, d, d, o, o, o, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, d, d, o, o, o, b, w, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    ]

frame16 = [
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, d, d, o, o, o, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, d, d, o, o, o, b, w, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    ]

frame17 = [
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, w, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, w, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, d, d, o, o, o, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, d, d, o, o, o, b, w, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, g, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, g, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    ]


frame18 = [
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, w, b, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, w, b, b, b, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, d, d, o, o, o, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, d, d, o, o, o, b, w, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, g, b, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, g, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, o, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, g, b, b, b, g, g, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, o, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, o, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, o, b, b, b, b, b, b, b, b, b, o, o, o, o, o, o, o, o, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, o, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, b, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b],
    [ b, b,  b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, g, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    [ b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, g, g, g, g, b, b, b],
    ]


def draw_frame(surface, data):
    for y, row in enumerate(data): #places coloured blocks in order from array
        for x, colour in enumerate(row):
            rect = pygame.Rect (x*10, y*10, 10, 10) #each square is 10 pixels by 10 pixels
            screen.fill(colour, rect=rect)

pygame.display.update()


while True:
    print("you area about to see an animated fish")#user outputs
    time.sleep(2) #time break
    print ("what speed would you like the fish to go")
    print ("25) FAST")
    print ("100) CASUAL SPEED")
    print ("300) SLOW")
    time.sleep(1) #time break

    ask = input("please make a choice (type in corresponding number) >>>")  #user input for speed    
    if ask == 25 or ask == 100 or ask ==300: #if ask is one of given values... (will help guide user if they type wrong thing
        while True: #will always stay on screen
            for event in pygame.event.get(): #makes graphic appear on screen
                if event.type == pygame.QUIT: #allows user to exit
                    sys.exit()
            draw_frame(screen, frame1) #displays frame1
            pygame.display.update() 
            pygame.time.wait(ask) #wait given time
            draw_frame(screen, frame2) #display frame2
            pygame.display.update()
            pygame.time.wait(ask) #wait given time
            draw_frame(screen, frame3) #displays frame3
            pygame.display.update() 
            pygame.time.wait(ask) #wait given time
            draw_frame(screen, frame4) #display frame4
            pygame.display.update()
            pygame.time.wait(ask) #wait given time
            draw_frame(screen, frame5) #displays frame5
            pygame.display.update() 
            pygame.time.wait(ask) #wait given time
            draw_frame(screen, frame6) #display frame6
            pygame.display.update()
            pygame.time.wait(ask) #wait given time
            draw_frame(screen, frame7) #displays frame7
            pygame.display.update() 
            pygame.time.wait(ask) #wait given time
            draw_frame(screen, frame8) #display frame8
            pygame.display.update()
            pygame.time.wait(ask) #wait given time
            draw_frame(screen, frame9) #display frame9
            pygame.display.update()
            pygame.time.wait(ask) #wait given time
            draw_frame(screen, frame10) #display frame10
            pygame.display.update()
            pygame.time.wait(ask) #wait given time
            draw_frame(screen, frame11) #display frame11
            pygame.display.update()
            pygame.time.wait(ask) #wait given time
            draw_frame(screen, frame12) #display frame12
            pygame.display.update()
            pygame.time.wait(ask) #wait given time
            draw_frame(screen, frame13) #display frame13
            pygame.display.update()
            pygame.time.wait(ask) #wait given time
            draw_frame(screen, frame14) #display frame14
            pygame.display.update()
            pygame.time.wait(ask) #wait given time
            draw_frame(screen, frame15) #display frame15
            pygame.display.update()
            pygame.time.wait(ask) #wait given time
            draw_frame(screen, frame16) #display frame16
            pygame.display.update()
            pygame.time.wait(ask) #wait given time
            draw_frame(screen, frame17) #display frame17
            pygame.display.update()
            pygame.time.wait(ask) #wait given time
            draw_frame(screen, frame18) #display frame18
            pygame.display.update()
            pygame.time.wait(ask) #wait given time
    else:
           print("I do not recognise that answere please try again")



