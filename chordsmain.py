import pygame
from pygame.locals import *
#import keyboard, scale, visual, chordbox, chordrec, sound, midicontrol, goals
#from keyboard import Keyboard
#from scale import Scale
#


#constants

SCREEN_SIZE=(1280,720)
KEYS={
    "K_q":0,
    "K_2":1,
    "K_w":2,
    "K_3":3,
    "K_e":4,
    "K_r":5,
    "K_5":6,
    "K_t":7,
    "K_6":8,
    "K_y":9,
    "K_7":10,
    "K_u":11,
    "K_i":12,
    "K_9":13,
    "K_o":14,
    "K_0":15,
    "K_p":16,
    "K_LEFTBRACKET":17,
    "K_EQUALS":18,
    "K_RIGHTBRACKET":19
}





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
    
