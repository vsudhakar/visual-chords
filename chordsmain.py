import pygame
from pygame.locals import *
from locals.py import *
#import keyboard, scale, visual, chordbox, chordrec, sound, midicontrol, goals
#from keyboard import Keyboard
#from scale import Scale







pygame.init()
screen=pygame.display.set_mode(SCREEN_SIZE, pygame.OPENGL | pygame.DOUBLEBUF | pygame.HWSURFACE)

keyboard=Keyboard()
scale=Scale()

#Main Game Loop:
FPS=60
clock=pygame.time.Clock()



#initialisations
keyboard=Keyboard()
scale=Scale()
goals=Goals()
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

    #Run Modules
    keyboard.update(keydown, keyup)
    scale.update(keydown, keyup)
    #goals.update(???)
    chordrec.update(keydown, keyup)
    visual.update(keydown, keyup, chordrec.data)
    chordbox.update(chordrec.chordstring)
    sound.update(keydown, keyup)

    #Draw Surfaces
    screen.blit(keyboard.surf, (0,HEIGHT*.2))
    screen.blit(scale.surf, (WIDTH*.75,HEIGHT*.25))
    screen.blit(goals.surf, (WIDTH*.75,0))
    screen.blit(visual.surf, (0, HEIGHT*.10))
    screen.blit(chordbox.surf, (WIDTH*.1875,0))
    
    

    
    pygame.display.flip()

    
