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



#initialisations
keyboard=Keyboard()
scale=Scale()
visual=Visualisation()
chordbox=Chordbox()
chordrec=Chordrec()
sound=Sound()




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
    screen.blit(scale.surf)
    screen.blit(keyboard.surf)
