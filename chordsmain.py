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
from visual import visual







pygame.init()
screen=pygame.display.set_mode(SCREEN_SIZE, pygame.OPENGL | pygame.DOUBLEBUF | pygame.HWSURFACE)

##keyboard=Keyboard()
##scale=Scale()

#Main Game Loop:
FPS=60
clock=pygame.time.Clock()



#initialisations
##keyboard=Keyboard()
##scale=Scale()
##goals=Goals()
visual=visual()
##chordbox=Chordbox()
##chordrec=Chordrec()
##sound=Sound()





while True:
    keydown=[]
    keyup=[]
    for event in pygane.event.get():
        if event.type==KEYDOWN:
            try:
                keydown.append(KEYS["K_"+str(pygame.key.name(event.key))])
            except:
                pass
        elif event.type==KEYUP:
            try:
                keyup.append(KEYS["K_"+str(pygame.key.name(event.key))])
            except:
                pass

    #Run Modules
##    keyboard.update(keydown, keyup)
##    scale.update(keydown, keyup)
##    chordrec.update(keydown, keyup)
##    goals.update(keydown, keyup, chordrec.data)
    visual.update(keydown, keyup, None)        # For now 'None' is passed, it should be chordrec.data

##    chordbox.update(chordrec.chordstring)
##    sound.update(keydown, keyup)

    #Draw Surfaces
##    screen.blit(keyboard.surf, (0,HEIGHT*.2))
##    screen.blit(scale.surf, (WIDTH*.75,HEIGHT*.25))
##    screen.blit(goals.surf, (WIDTH*.75,0))
    screen.blit(visual.surf, (0, HEIGHT*.10))
##    screen.blit(chordbox.surf, (WIDTH*.1875,0))
    
    
    

    
    pygame.display.flip()
