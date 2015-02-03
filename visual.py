#visual module

import pygame
from pygame.locals import *
from locals import *

class visual:
    def __init__(self, size):
##        self.size = (WIDTH*0.75, HEIGHT*0.7)
        self.size = size
        self.surf = pygame.Surface(self.size)

        #Rectangle visualization
        self.rects = []
        numOfRects = 5
        heightOfRects = int(self.size[1]/5)

        self.currentNotes = []

    def draw(self, notes):
        for x in xrange(len(notes)):
            h=(x+1)*(self.size[1]/5)
            r=pygame.Rect((0,h-self.size[1]/5), (self.size[0], self.size[1]/5))
            self.surf.fill(COLOR(notes[x]), r)
        self.currentNotes = notes
            
    def update(self, keydown, keyup, chordrec):
        if chordrec==None:
            notes = self.currentNotes
            for i in keydown:
                notes.pop()
                notes.insert(0, i)
            print notes
            self.draw(keydown)
            self.currentNotes = notes





##DEBUGGING
pygame.init()
size = (512, 510)
screen=pygame.display.set_mode(size)
vis = visual(size)

FPS = 60
clock=pygame.time.Clock()
n = [0, 1, 2, 3, 4]
vis.draw(n)s
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
                print pygame.key.name(event.key)
                keydown.append(KEYS["K_"+str(pygame.key.name(event.key))])
            elif event.type==KEYUP:
                keyup.append(KEYS["K_"+str(pygame.key.name(event.key))])
    vis.update(keydown, keyup, None)
    vis.draw(n)
    screen.blit(vis.surf, (0, 0))
    pygame.display.flip()

                            

    
