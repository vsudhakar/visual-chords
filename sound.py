import pygame
import pygame.midi

class Sound:
    def __init__(self):
        pygame.midi.init()
        self.player=pygame.midi.Output(0)
        self.player.set_instrument(0,1)
        
    def update(self, keydown, keyup):
        for x in keydown:
            self.player.note_on(x+72, 127, 1)
        for x in keyup:
            self.player.note_off(x+72, 127, 1)
