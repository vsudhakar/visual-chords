import pygame
from pygame.locals import *
from locals import *
import goalFileInput

class Goals(object):
    class GoalSurf(object):
        def __init__(self, string, qualifier, size, pos):
            self.W=size[0]
            self.H=size[1]
            self.surf=pygame.Surface(size)
            self.completed=False
            font=pygame.font.SysFont('Arial', int(self.H*.16))
            textrect=pygame.Rect(int(self.W*.15), 0, int(self.W*.8), int(self.H*.75))
            self.drawText(self.surf, string, (255,255,255), pygame.Rect(int(self.W*.15)+2, 0, int(self.W*.8), int(self.H*.75)), font, bkg=(0,0,0))
            pygame.draw.rect(self.surf, (255,255,255), textrect, 1)
            self.checkbox(False)
            self.position=pos
            self.qualifier = tuple(qualifier)

        #Update with chordrec and trip the completed if necessary
        def update(self, data, chordstr):
            if data != None and len(data) == len(self.qualifier):
                tripped = False
                valMatch = 0
                valCount = 0
                for i in range(len(self.qualifier)):
                    if self.qualifier[i] != None:
                        valCount += 1
                        if self.qualifier[i] == data[i]:
                            valMatch += 1

                if valCount == valMatch and valCount + valMatch != 0:
                    tripped = True

                if tripped:
                    self.complete()
                    print "TRIPPED"
                    print self.qualifier
                    print data

        ###drawText function credit to pygame.org--------
        def drawText(self, surface, text, color, rect, font, aa=False, bkg=None):
            rect=pygame.Rect(rect)
            y = rect.top
            lineSpacing = -2
            fontHeight = font.size("Tg")[1]
            while text:
                i = 1
                if y + fontHeight > rect.bottom:
                    break
                while font.size(text[:i])[0] < rect.width and i < len(text):
                    i += 1
                if i < len(text):
                    i = text.rfind(" ", 0, i) + 1
                if bkg:
                    image = font.render(text[:i], 1, color, bkg)
                    image.set_colorkey(bkg)
                else:
                    image = font.render(text[:i], aa, color)
                surface.blit(image, (rect.left, y))
                y += fontHeight + lineSpacing
                text = text[i:]

        ###drawText--------------------------------------

        def checkbox(self, status):
            bl=int(self.W*.05)
            offset=((.75*self.H)-bl)/2
            pygame.draw.rect(self.surf, (255,255,255), (bl, offset, bl, bl), 1)
            if status:
                pygame.draw.aaline(self.surf, (255,255,255), (bl, offset),(bl+bl, offset+bl))
                pygame.draw.aaline(self.surf, (255,255,255), (bl+bl,offset),(bl, offset+bl))
                self.surf.set_alpha(127)


        def complete(self):
            self.completed=True
            self.checkbox(True)

        def draw(self, dest):
            dest.fill((0,0,0), (0, self.H*self.position, self.W, self.H))
            dest.blit(self.surf, (0, self.H*self.position))










    def __init__(self):
        pygame.font.init()
        self.W=int(WIDTH*.25)
        print WIDTH
        self.H=int(HEIGHT*.75)
        self.surf=pygame.Surface((self.W, self.H))
        # self.goalstrings=[
        #     "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ut gravida nisi. Pellentesque eget elit nulla. Ut porttitor nulla tellus, vel sodales ante posuere rutrum. Integer libero risus, tincidunt eu eleifend sed, pharetra at odio. Nunc pulvinar purus nisi, sit amet aliquet dolor pharetra non.",
        #     "Proin tincidunt venenatis egestas. Vivamus ornare cursus mi. Fusce magna ipsum, semper non nunc non, condimentum tincidunt metus. Vivamus dignissim arcu quis metus semper fermentum.",
        #     "Vestibulum ac quam ultrices, rhoncus arcu sit amet, egestas tortor. Curabitur fermentum enim varius nunc tempor, in rhoncus risus pretium. Nunc a pellentesque felis, id molestie mauris. In suscipit, urna eget imperdiet pellentesque, ex leo finibus dui, at dignissim risus eros vitae odio.",
        #     "Etiam mollis pellentesque vehicula. Pellentesque pellentesque ligula ipsum, in tempor ligula tincidunt a. Fusce eu diam lacinia, lobortis arcu egestas, congue ex. Aliquam consectetur leo urna, id condimentum erat vulputate sed. Praesent a ante odio. Etiam ut lacinia erat, id viverra felis",
        #     "Etiam ut lacinia erat, id viverra felis."
        # ]

        self.goalstrings = [('Play a major third.', (None, 4)), ('Play a minor third.', (None, 3)), ('Play a perfect fifth.', (None, 7)), ('Play any major triad.', (None, 0, 0, None)), ('Play any minor triad.', (None, 1, 0, None)), ('Play the following triad: F# minor diminished', (6, 2, 0, None)), ('Play a major seventh.', (None, None, None, None)), ('Play a minor seventh.', (None, None, None, None)), ('Play any major seventh chord.', (None, None, None, None)), ('Play any minor seventh chord.', (None, None, None, None)), ('Play any half-diminished seventh chord.', (None, None, None, None)), ('Play the following seventh chord: B major-minor', (None, None, None, None)), ('Play any major chord in first inversion.', (None, None, None, None)), ('Play any major chord in second inversion.', (None, None, None, None)), ('Play the following chord: D flat minor first inversion.', (None, None, None, None)), ('Play any major-minor seventh chord in first inversion.', (None, None, None, None)), ('Play any full-diminished seventh chord in second inversion.', (None, None, None, None))]

        self.goalsurf=pygame.Surface((self.W, self.H*.2*len(self.goalstrings)))
        self.scroll=0
        self.MAXSCROLL=self.goalsurf.get_height()-self.H*.75

        titlefont=pygame.font.SysFont('Arial', int(self.H/20))
        title=titlefont.render("G O A L S", True, (255,0,0), (0,0,0))
        self.surf.blit(title, ((self.W-title.get_width())/2, 0))
        self.drawarrows()

        self.goalsurfs=[]
        for x in xrange(len(self.goalstrings)):
            s=self.GoalSurf(self.goalstrings[x][0], self.goalstrings[x][1], (self.W, int(self.H*.2)), x)
            print s.surf
            s.draw(self.goalsurf)
            self.goalsurfs.append(s)


        self.surf.blit(self.goalsurf, (0, self.H*.1), (0,0,self.goalsurf.get_width(), self.H*.85))
        self.drawarrows()


    def drawarrows(self):
        if self.scroll==0:
            pygame.draw.polygon(self.surf, (127,127,127), [(self.W*.4, self.H*.08), (self.W*.5, self.H*.05), (self.W*.6, self.H*.08)])
        else:
            pygame.draw.polygon(self.surf, (255,255,255), [(self.W*.4, self.H*.08), (self.W*.5, self.H*.05), (self.W*.6, self.H*.08)])
        if self.scroll==self.MAXSCROLL:
            pygame.draw.polygon(self.surf, (127,127,127), [(self.W*.4, self.H*.97), (self.W*.5, self.H), (self.W*.6, self.H*.97)])
        else:
            pygame.draw.polygon(self.surf, (255,255,255), [(self.W*.4, self.H*.97), (self.W*.5, self.H), (self.W*.6, self.H*.97)])



    def update(self, chorddata, chordstring, s):
        if s!=0:
            self.drawarrows()
            self.scroll+=s*5
            self.clamp()
            print self.scroll

        for goal in self.goalsurfs:
            goal.update(chorddata, chordstring)
            goal.draw(self.goalsurf)
        self.surf.blit(self.goalsurf, (0, self.H*.1), (0,self.scroll,self.goalsurf.get_width(), self.H*.85))




    def clamp(self):
        if self.scroll<0:
            self.scroll=0
        if self.scroll>self.MAXSCROLL:
            self.scroll=self.MAXSCROLL





'''
screen=pygame.display.set_mode(SCREEN_SIZE)

g=Goals()
while True:
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            g.update(None, 1)
            print event.key
    g.update(None, 0)
    screen.blit(g.surf, (0,0))
    #screen.blit(g.goalsurf("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus condimentum sapien et libero condimentum, eget lacinia odio condimentum. Nulla consectetur ex lectus, vitae aliquet dolor volutpat malesuada. Nulla vulputate vel elit at efficitur. Etiam eu justo ac elit suscipit semper a ut sem. Maecenas ullamcorper ultricies porttitor. Maecenas varius, tortor."), (0,0))
    pygame.display.flip()
'''
