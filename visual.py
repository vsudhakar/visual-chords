#visual module

import pygame
from pygame.locals import *
from locals import *
class visual:
    def __init__(self):
        self.size = (WIDTH*0.75, HEIGHT*0.7)
        self.surf = pygame.Surface(self.size)
        self.surf.set_alpha(255)
        self.burstframes=0
        self.burstsurf=pygame.Surface(self.size)
        self.burstsurf.set_alpha(0)
        self.currentNotes = []

    def draw(self, notes):
        self.surf.fill((0,0,0))
        for x in xrange(len(notes)):
            r=pygame.Rect((0,(4-x)*self.size[1]/5), (self.size[0], self.size[1]/5))
            self.surf.fill(COLOR(notes[x]), r)
                      
    def burst(self, n):
        self.burstsurf.fill(COLOR(n))
        self.burstsurf.set_alpha(255)
        self.burstframes=51

    def onframe(self):
        print self.burstframes
        if self.burstframes>0:
            self.burstframes-=1
            self.burstsurf.set_alpha(self.burstframes*5)
        self.surf.blit(self.burstsurf, (0,0))
        
    def update(self, keydown, keyup, chordrec):

        #notes
        
        key=False
        for x in keydown:
            self.currentNotes.append(x)
            key=True
        
        for x in keyup:
            try:
                self.currentNotes.remove(x)
            except(ValueError):
                print "missed keydown?"
            key=True
        
        if key:
            if chordrec!=None:
                if len(chordrec)==4:
                    print chordrec
                    self.burst(chordrec[0])

        self.draw(self.currentNotes)
        self.onframe()
        
        


    
