#visual module

import pygame
from pygame.locals import *
from locals.py import *

class visual:
    def __init__(self, size):
        self.size = (size[0]*0.75, size[1]*0.7) 
        self.surf = pygame.Surface(self.size)

        #Rectangle visualization
        self.rects = []
        numOfRects = 5
        heightOfRects = int(self.size[1]/5)
        for i in range(numOfRects):
            self.rects.append(self.Rect((0, heightOfRects*(i+1)), (self.size[0], heightOfRects))

        #Draw rectangles onto surface object
        for i in self.rects:
            pygame.draw.rect(self.surf, pygame.Color("red"), i)
                              
##    def update(keydown, keyup, chordrec):



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

                            

    
