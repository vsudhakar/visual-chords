import pygame
from pygame.locals import *
from locals import *
'''
from keyboard import Keyboard
from scale import Scale
from visual import Visual
from chordbox import Chordbox
'''
#import keyboard, scale, visual, chordbox, chordrec, sound, midicontrol, goals
#from keyboard import Keyboard
#from scale import Scale
#from visual import visual







pygame.init()
screen=pygame.display.set_mode(SCREEN_SIZE, pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.FULLSCREEN)

##keyboard=Keyboard()
##scale=Scale()

#Main Game Loop:
FPS=60
clock=pygame.time.Clock()



#initialisations
##keyboard=Keyboard()
##scale=Scale()
##goals=Goals()
##visual=visual()
##chordbox=Chordbox()
##chordrec=Chordrec()
##sound=Sound()


screen.fill((255,255,255))
pygame.draw.rect(screen, (0,0,0), pygame.Rect(0,HEIGHT*.8, WIDTH*.75, HEIGHT*.2), 2)
pygame.draw.rect(screen, (0,0,0), pygame.Rect(WIDTH*.75,HEIGHT*.75, WIDTH*.25, HEIGHT*.25), 2)
pygame.draw.rect(screen, (0,0,0), pygame.Rect(WIDTH*.75,0, WIDTH*.25, HEIGHT*.75), 2)
pygame.draw.rect(screen, (0,0,0), pygame.Rect(0,HEIGHT*.1, WIDTH*.75, HEIGHT*.7), 2)
pygame.draw.rect(screen, (0,0,0), pygame.Rect(WIDTH*.15,0, WIDTH*.5, HEIGHT*.1), 2)

while True:
    keydown=[]
    keyup=[]
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            try:
                keydown.append(KEYS[event.key])
            except:
                pass
        elif event.type==KEYUP:
            try:
                keyup.append(KEYS[event.key])
            except:
                pass
            ##    keyboard.update(keydown, keyup)
            ##    scale.update(keydown, keyup)
            ##    chordrec.update(keydown, keyup)
            ##    goals.update(keydown, keyup, chordrec.data)
            ##    visual.update(keydown, keyup, None)        # For now 'None' is passed, it should be chordrec.data

            ##    chordbox.update(chordrec.chordstring)
            ##    sound.update(keydown, keyup)

                #Draw Surfaces
            ##    screen.blit(keyboard.surf, (0,HEIGHT*.8))
            ##    screen.blit(scale.surf, (WIDTH*.75,HEIGHT*.25))
            ##    screen.blit(goals.surf, (WIDTH*.75,0))
             ##   screen.blit(visual.surf, (0, HEIGHT*.10))
            ##    screen.blit(chordbox.surf, (WIDTH*.1875,0))
            


    
    pygame.display.flip()
