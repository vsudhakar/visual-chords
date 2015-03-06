from locals import *
import pygame
from pygame.locals import *

class Keyboard:
    def __init__(self):
        W=SCREEN_SIZE[0]*.75
        H=SCREEN_SIZE[1]*.2
        self.keyverticies=[
            [(0,       0),(0,H),         (1*W/12,  H),  (1*W/12,  H/2),(4*W/72, H/2),(4*W/72, 0)                            ],#0:C
            [(4*W/72,  0),(4*W/72,  H/2),(7*W/72,  H/2),(7*W/72,  0)                                                        ],#1:C#
            [(7*W/72,  0),(7*W/72,  H/2),(W/12,    H/2),(W/12,    H),  (2*W/12, H),  (2*W/12, H/2),(11*W/72,H/2),(11*W/72,0)],#2:D
            [(11*W/72, 0),(11*W/72, H/2),(14*W/72, H/2),(14*W/72, 0)                                                        ],#3:D#
            [(14*W/72, 0),(14*W/72, H/2),(2*W/12,  H/2),(2*W/12,  H),  (3*W/12, H),  (3*W/12, 0)                            ],#4:E
            [(3*W/12,  0),(3*W/12 , H),  (4*W/12,  H),  (4*W/12,  H/2),(22*W/72,H/2),(22*W/72,0)                            ],#5:F
            [(22*W/72, 0),(22*W/72, H/2),(25*W/72, H/2),(25*W/72, 0)                                                        ],#6:F#
            [(25*W/72, 0),(25*W/72, H/2),( 4*W/12, H/2),( 4*W/12, H),  ( 5*W/12,H),  ( 5*W/12,H/2),(28*W/72,H/2),(28*W/72,0)],#7:G
            [(28*W/72, 0),(28*W/72, H/2),(31*W/72, H/2),(31*W/72, 0)                                                        ],#8:G#
            [(31*W/72, 0),(31*W/72, H/2),( 5*W/12, H/2),( 5*W/12, H),  ( 6*W/12,H),  ( 6*W/12,H/2),(34*W/72,H/2),(34*W/72,0)],#9:A
            [(34*W/72, 0),(34*W/72, H/2),(37*W/72, H/2),(37*W/72, 0)                                                        ],#10:A#
            [(37*W/72, 0),(37*W/72, H/2),(06*W/12, H/2),(06*W/12, H),  ( 7*W/12,H),  ( 7*W/12,0)                            ],#11:B
            [( 7*W/12, 0),( 7*W/12, H),  ( 8*W/12, H),  ( 8*W/12, H/2),(47*W/72,H/2),(47*W/72,0)                            ],#12:C
            [(47*W/72, 0),(47*W/72, H/2),(50*W/72, H/2),(50*W/72, 0)                                                        ],#13:C#
            [(50*W/72, 0),(50*W/72, H/2),( 8*W/12, H/2),( 8*W/12, H),  ( 9*W/12,H),  ( 9*W/12,H/2),(53*W/72,H/2),(53*W/72,0)],#14:D
            [(53*W/72, 0),(53*W/72, H/2),(56*W/72, H/2),(56*W/72, 0)                                                        ],#15:D#
            [(56*W/72, 0),(56*W/72, H/2),( 9*W/12, H/2),( 9*W/12, H),  (10*W/12,H),  (10*W/12,0)                            ],#16:E
            [(10*W/12, 0),(10*W/12, H),  (11*W/12, H),  (11*W/12, H/2),(65*W/72,H/2),(65*W/72,0)                            ],#17:F
            [(65*W/72, 0),(65*W/72, H/2),(68*W/72, H/2),(68*W/72, 0)                                                        ],#18:F#
            [(68*W/72, 0),(68*W/72, H/2),(11*W/12, H/2),(11*W/12, H),  (W,      H),  (W,      0)                            ] #19:G
        ]

        self.surf=pygame.Surface((W,H))
        self.surf.fill((255,255,255))
        for vert in self.keyverticies:
            if len(vert)==4:
                pygame.draw.polygon(self.surf, (64,64,64), vert)
            pygame.draw.polygon(self.surf, (0,0,0), vert, 2)


    def update(self, keydn, keyup):
        for x in keydn:
            pygame.draw.polygon(self.surf, COLOR(x), self.keyverticies[x])
            pygame.draw.polygon(self.surf, (0,0,0), self.keyverticies[x], 2)
        for x in keyup:
            if len(self.keyverticies[x])==4:
                pygame.draw.polygon(self.surf, (64,64,64), self.keyverticies[x])
            else:
                pygame.draw.polygon(self.surf, (255,255,255), self.keyverticies[x])
            pygame.draw.polygon(self.surf, (0,0,0), self.keyverticies[x], 2)




'''
##DEBUGGING
pygame.init()
size = (800, 600)
screen=pygame.display.set_mode(size)
SCREEN_SIZE=size
k = Keyboard()

FPS = 60
clock=pygame.time.Clock()
screen.blit(k.surf, (0, 0))

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
                print event.key
                try:
                    keydown.append(KEYS[event.key])
                except:
                    pass
            elif event.type==KEYUP:
                try:
                    keyup.append(KEYS[event.key])
                except:
                    pass
    
    k.update(keydown, keyup)
    screen.blit(k.surf, (0, 0))
    pygame.display.flip()
'''
