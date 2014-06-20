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


def draw_frame(surface, data):
    for y, row in enumerate(data): #places coloured blocks in order from array
        for x, colour in enumerate(row):
            rect = pygame.Rect (x*10, y*10, 10, 10) #each square is 10 pixels by 10 pixels
            screen.fill(colour, rect=rect)

pygame.display.update()

while True: #will always stay on screen
    for event in pygame.event.get(): #makes graphic appear on screen
        if event.type == pygame.QUIT: #allows user to exit
            sys.exit()
    draw_frame(screen, frame1) #displays frame1
    pygame.display.update() 
    pygame.time.wait(500) #wait 300
    draw_frame(screen, frame2) #display frame2
    pygame.display.update()
    pygame.time.wait(500) #wait 300
    draw_frame(screen, frame3) #displays frame3
    pygame.display.update() 
    pygame.time.wait(500) #wait 300
    draw_frame(screen, frame4) #display frame4
    pygame.display.update()
    pygame.time.wait(500) #wait 300
    draw_frame(screen, frame5) #displays frame5
    pygame.display.update() 
    pygame.time.wait(500) #wait 300
    draw_frame(screen, frame6) #display frame6
    pygame.display.update()
    pygame.time.wait(500) #wait 300
    draw_frame(screen, frame7) #displays frame7
    pygame.display.update() 
    pygame.time.wait(500) #wait 300
    draw_frame(screen, frame8) #display frame8
    pygame.display.update()
    pygame.time.wait(500) #wait 300
    draw_frame(screen, frame9) #display frame9
    pygame.display.update()
    pygame.time.wait(500) #wait 300




