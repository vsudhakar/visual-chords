from pygame.locals import *

class Keyboard:
    surf = new Surface(SCREEN_SIZE)
    def update(keyup, keydown):
        keyList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
        whiteList = [0, 2, 4, 5, 7, 9, 11, 12, 14, 16, 17, 19, 21, 23, 24] #15
        blackList = [1, 3, 6, 8, 10, 13, 15, 18, 20, 22] #10
        left = 0
        top = HEIGHT * .2
        top = HEIGHT - top
        for x in xrange keyList:
            if keyup.indexOf(x) = -1
                if whiteList.indexOf(x) != -1:
                    pygame.draw.rect(surf, COLOR(x), (left, top, (WIDTH * .75) / 15, HEIGHT * .2), width = 1)
                    left += (WIDTH * .75) / 15
                elif blackList.indexOf(x) != -1:
                    pygame.draw.rect(surf, COLOR(x), (left - (WIDTH * .75) / 30, top, (WIDTH * .75) / 15, HEIGHT * .1), width = 1)
            elif keyup.indexOf(x) != -1
                if whiteList.indexOf(x) != -1:
                    pygame.draw.rect(surf, (000, 000, 000), (left, top, (WIDTH * .75) / 15, HEIGHT * .2), width = 1)
                    left += (WIDTH * .75) / 15
                elif blackList.indexOf(x) != -1:
                    pygame.draw.rect(surf, (255, 255, 255), (left - (WIDTH * .75) / 30, top, (WIDTH * .75) / 15, HEIGHT * .1), width = 1)
            
