import pygame
from pygame.locals import *
from locals import *

class Scale(object):
    def __init__(self):
        self.H=HEIGHT/4
        self.W=WIDTH/4
        self.surf=pygame.Surface((self.W, self.H))
        self.csize=self.H/14-1

        self.sharp=[1,3,6,8,10,13,15,18]
        self.space=[2,5,9,12,16,19]
        self.nheight={
            0:self.H*6/7,
            2:self.H*11/14,
            4:self.H*5/7,
            5:self.H*9/14,
            7:self.H*4/7,
            9:self.H*9/14,
            11:self.H*3/7,
            12:self.H*5/14,
            14:self.H*2/7,
            16:self.H*3/14,
            17:self.H/7,
            19:self.H/14
        }
        self.cleff=pygame.image.load("treble.png").convert_alpha()
        self.cleff=pygame.transform.scale(self.cleff, (int(self.H*.3796), self.H))
        self.currentNotes=[]
        self.drawboard()
            
    def update(self, keydown, keyup):
    
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
        
        "called"
        self.drawboard()
        for x in self.currentNotes:
            self.drawnote(x)
        
            



    def drawboard(self):
        print "drawn"
        self.surf.fill((255,255,255))
        self.surf.blit(self.cleff, (0,0))
        pygame.draw.line(self.surf, (0,0,0), (0, self.H/7), (self.W, self.H/7))
        pygame.draw.line(self.surf, (0,0,0), (0, self.H*2/7), (self.W, self.H*2/7))
        pygame.draw.line(self.surf, (0,0,0), (0, self.H*3/7), (self.W, self.H*3/7))
        pygame.draw.line(self.surf, (0,0,0), (0, self.H*4/7), (self.W, self.H*4/7))
        pygame.draw.line(self.surf, (0,0,0), (0, self.H*5/7), (self.W, self.H*5/7))


    

    def drawnote(self, note):
        sharp=False
        space=0
        n2=note
        if note in self.sharp:
            sharp=True
            n2-=1
        if n2 in self.space:
            space=self.W/14
        if n2==0:
            pygame.draw.line(self.surf, (0,0,0), (self.W/2-self.csize*3/2, self.H*6/7), (self.W/2+self.csize*3/2, self.H*6/7))
        pygame.draw.circle(self.surf, COLOR(note), (self.W/2+space, self.nheight[n2]), self.csize)
'''        
pygame.init()


screen=pygame.display.set_mode(SCREEN_SIZE)
s=Scale()
while True:
    screen.blit(s.surf, (0,0))
    pygame.display.flip()
'''
