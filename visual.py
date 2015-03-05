#visual module

import pygame
from pygame.locals import *
from locals import *
import random as R
class visual:
    def __init__(self, size):
##        self.size = (WIDTH*0.75, HEIGHT*0.7)
        self.size = size
        self.surf = pygame.Surface(self.size)
        self.frame=0
        self.bsurf=pygame.Surface(self.size)
        

        #Rectangle visualization
        self.rects = []
        numOfRects = 5
        heightOfRects = int(self.size[1]/5)

        self.currentNotes = []

    def draw(self, notes):
        for x in xrange(len(notes)):
            h=(x+1)*(self.size[1]/5)
            r=pygame.Rect((0,x*self.size[1]/5), (self.size[0], self.size[1]/5))
            self.surf.fill(COLOR(notes[x]), r)

    def burst(self, n):
        self.bsurf.fill(COLOR(n))
        self.frame=51
        
    def update(self, keydown, keyup, chordrec):

        #notes
        drawnotes=False
        for x in keydown:
            self.currentNotes.append(x)
            drawnotes=True
        for x in keyup:
            self.currentNotes.remove(x)
            drawnotes=True

        print self.currentNotes
        if drawnotes:
            self.surf.fill(pygame.Color("white"))
            self.draw(self.currentNotes)


        

        #increment animation
        if self.frame>0:
            self.chordburst()
            self.frame-=1
        else:
            if chordrec!=None:
                self.burst(chordrec[0])
        
            
          ''' 
        if chordrec==None:
            notes = self.currentNotes
            for i in keydown:
                notes.pop()
                notes.insert(0, i)
            self.draw(keydown)
            self.currentNotes = notes
        else:
            if self.frame==0:
                bsurf.fill(COLOR(chordrec.data[root]))
                self.frame=51
        '''
        

    def chordburst(self):
        self.bsurf.set_alpha(self.frame*5)
        self.surf.blit(self.bsurf, (0,0))
        


##DEBUGGING
pygame.init()
size = (512, 510)
screen=pygame.display.set_mode(size)
vis = visual(size)

FPS = 60
clock=pygame.time.Clock()
screen.blit(vis.surf, (0, 0))

pygame.display.flip()


while True:
    clock.tick(60)
    keydown = []
    keyup = []
    for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
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
    
    vis.update(keydown, keyup, None)
    screen.blit(vis.surf, (0, 0))
    pygame.display.flip()

                            

    
