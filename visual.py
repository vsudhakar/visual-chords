#visual module

import pygame
from pygame.locals import *
from locals import *
import random as R
class visual:
    def __init__(self):
        self.size = (WIDTH*0.75, HEIGHT*0.7)
        self.surf = pygame.Surface(self.size)
        self.frame=0
        self.bsurf=pygame.Surface(self.size)

        self.currentNotes = []

    def draw(self, notes):
        for x in xrange(len(notes)):
            r=pygame.Rect((0,(4-x)*self.size[1]/5), (self.size[0], self.size[1]/5))
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
            try:
                self.currentNotes.remove(x)
            except(ValueError):
                print "missed keydown?"
            drawnotes=True
        
        if drawnotes:
            self.surf.fill(pygame.Color("black"))
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
    
