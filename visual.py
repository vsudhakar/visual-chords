#visual module

import pygame
from pygame.locals import *
from locals.py import *

class visual:
    def __init__(self, size):
        self.size = (WIDTH*0.75, HEIGHT*0.7) 
        self.surf = pygame.Surface(self.size)

        #Rectangle visualization
        self.rects = []
        numOfRects = 5
        heightOfRects = int(self.size[1]/5)
        for i in range(numOfRects):
            self.rects.append(self.Rect((0, heightOfRects*(i+1)), (self.size[0], heightOfRects))

        #Draw rectangles onto surface object
        for i in self.rects:
            pygame.draw.rect(self.surf, pygame.Color("red"), i))



    def draw(notes):
        for x in xrange(len(notes)):
            h=(x+1)*(self.size[1]/5)
            r=Pygame.Rect((0,h), self.size[0], h)
            self.surf.fill(COLOR(notes[x]), r)
            
    def update(keydown, keyup, chordrec):
        if chordrec==None:
            
                              





##DEBUGGING

##pygame.init()
##screen=pygame.display.set_mode((100, 100))
##
##vis = visual((100, 100))
##
##FPS = 60
##clock=pygame.time.Clock()
##
##screen.blit(vis.surf)

                            

    
