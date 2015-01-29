import pygame
from pygame.locals import *
#import keyboard, scale, visual, chordbox, chordrec, sound, midicontrol, goals
#from keyboard import Keyboard
#from scale import Scale

pygame.init()
screen=pygame.display.set

keyboard=Keyboard()
scale=Scale()

#Module surface positions
#Destination for blit of each surface onto main game surface
scaleSurfDest = (x,y)       #Upper left corner of surface
keyboardSurfDest = (x,y)

#Main Game Loop:
FPS=60
clock=pygame.time.Clock()
while True:
    keydown=[]
    keyup=[]
    for event in pygane.event.get():
        if event.type==KEYDOWN:
            keydown.append(KEYS[event.key])
        elif event.type==KEYUP:
            keyup.append(KEYS[event.key])

    #Call update function for each module - updates local surface object
    keyboard.update(keydown, keyup)
    scale.update(keydown, keyup)

    #Blit local surface object from each module
    screen.blit(scale.surf, scaleSurfDest)
    screen.blit(keyboard.surf, keyboardSurfDest)
    
