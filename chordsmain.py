import pygame
from pygame.locals import *
#import keyboard, scale, visual, chordbox, chordrec, sound, midicontrol, goals
#from keyboard import Keyboard
#from scale import Scale







pygame.init()
screen=pygame.display.set

keyboard=Keyboard()
scale=Scale()

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
    keyboard.update(keydown, keyup)
    scale.update(keydown, keyup)
    screen.blit(scale.get_surf())
    screen.blit(keyboard.get_surf())
    
