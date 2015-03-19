import pygame
from pygame.locals import *
from locals import *

class Chordbox:
    def __init__(self):
        self.W=int(SCREEN_SIZE[0]*.5)
        self.H=int(SCREEN_SIZE[1]*.1)
        self.surf=pygame.Surface((self.W,self.H))
        self.surf.fill((0,0,0))
        self.font=pygame.font.SysFont('Arial', self.H/2)
        self.text=""
    def update(self, cdata, cstring):
        if cstring!=self.text:
            self.text=cstring
            # self.text=str(cdata)  # Debugging mode
            rtext=self.font.render(self.text, True, (255,0,0), (0,0,0))
            self.surf.fill((0,0,0))
            self.surf.blit(rtext, ((self.W-rtext.get_width())/2, (self.H-rtext.get_height())/2))
