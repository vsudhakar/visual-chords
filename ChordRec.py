import copy
class ChordRec(object):
    def __init__(self):
        self.currentNotes=[]
        self.chorddata=None
        self.chordstring=""

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
        if key:
            if len(self.currentNotes)==0:
                self.chorddata=None
                self.chordstring=""
            else:
                self.chorddata=self.makedata(self.currentNotes, [])
                self.chordstring=self.makestring(self.currentNotes, [])

    def makedata(self,currentNodes,keysUp):
        keysDown=copy.deepcopy(currentNodes)
        intervals=[]
        note=[]
        chord=[]
        root=0
        #Chord intervals
        library={(4, 3): 0, (3, 4): 1, (3, 3): 2, (4, 4): 3, (4, 3, 4): 4, (4, 3, 3): 5, (3, 4, 4): 6, (3, 4, 3): 7, (3, 3, 4): 8, (3, 3, 3): 9, (4, 4, 4): 10}
        #put all the chords in the same octave
        for x in range(len(keysDown)):
            chord.append(keysDown[x])
        for x in range(len(chord)-1):
            for y in range(len(chord)-1):
                if chord[y]>chord[y+1]:
                    temp=chord[y+1]
                    chord[y+1]=chord[y]
                    chord[y]=temp
        root=keysDown[0]
        for x in range(len(chord)):
            if chord[x]>12:
                chord[x]=chord[x]-12
        if root>12:
            root-=12
        for x in range(len(chord)-1):
            if chord[x+1]-chord[x]!=3 and chord[x+1]-chord[x]!=4:
                chord[x]+=12
                keysDown[x]+=12
                root+=12
                #sort after 
            for z in range(len(chord)-1):
                for y in range(len(chord)-1):
                    if chord[y]>chord[y+1]:
                        temp=chord[y+1]
                        chord[y+1]=chord[y]
                        chord[y]=temp
                        temp=keysDown[y+1]
                        keysDown[y+1]=keysDown[y]
                        keysDown[y]=temp
            intervals.append(chord[x+1]-chord[x])
        tone=""
        cType=0
        if len(intervals)==1:
            tone=None
            output=None
        if len(intervals)==2:
            chord_makeup=(intervals[0],intervals[1])
            try:
                tone=library[chord_makeup]
            except:
                return None
            cType=0
        elif len(intervals)==3:
            chord_makeup=(intervals[0],intervals[1],intervals[2])
            try:
                tone=library[chord_makeup]
            except:
                return None
            cType=1
        #Inversion
        inver=0
        if chord[0]!=root and tone!=None:
            if chord[1]==root:
                inver=1
            elif chord[2]==root:
                inver=2
            try:
                if chord[3]==root: 
                    inver=3
            except:
                pass
        if tone!=None:
            output=(root,tone,cType,inver)
        return output
    def makestring(self,currentNodes,keysUp):
        keysDown=copy.deepcopy(currentNodes)
        outp=""
        intervals=[]
        note=["""order of notes in relation to keysDown"""]
        chord=[]
        #Chord intervals
        library={(4, 3): 'major', (3, 4): 'minor', (3, 3): 'diminished', (4, 4): 'augmented', (4, 3, 4): 'major 7th', (4, 3, 3): 'major-minor 7th', (3, 4, 4): 'minor-major 7th', (3, 4, 3): 'minor 7th', (3, 3, 4): 'half-diminished 7th', (3, 3, 3): 'full diminished 7th', (4, 4, 4): 'augmented 7th'}
        #put all the chords in the same octave
        root=keysDown[0]
        for x in range(len(keysDown)):
            if keysDown[x]>12:
                chord.append(keysDown[x]-12)
            else:
                chord.append(keysDown[x])
        if root>12:
            root-=12
        #sort first time
        for x in range(len(chord)-1):
            for y in range(len(chord)-1):
                if chord[y]>chord[y+1]:
                    temp=chord[y+1]
                    chord[y+1]=chord[y]
                    chord[y]=temp
        for x in range(len(chord)-1):
            if chord[x+1]-chord[x]!=3 and chord[x+1]-chord[x]!=4:
                chord[x]+=12
                keysDown[x]+=12
                root+=12
                #sort after 
                for z in range(len(chord)-1):
                    for y in range(len(chord)-1):
                        if chord[y]>chord[y+1]:
                            temp=chord[y+1]
                            chord[y+1]=chord[y]
                            chord[y]=temp
                            temp=keysDown[y+1]
                            keysDown[y+1]=keysDown[y]
                            keysDown[y]=temp
            intervals.append(chord[x+1]-chord[x])
        if len(intervals)==1:
            outp=""
        if len(intervals)==2:
            chord_makeup=(intervals[0],intervals[1])
            try:
                outp=library[chord_makeup]
            except:
                outp=""
        elif len(intervals)==3:
            chord_makeup=(intervals[0],intervals[1],intervals[2])
            try:
                outp=library[chord_makeup]
            except:
                outp=""
        #Inversion
        if chord[0]!=root and len(chord)>2:
            if chord[1]==root:
                outp+=' First Inversion'
            elif chord[2]==root:
                outp+=' Second Inversion'
            try:
                if chord[3]==root: 
                    outp+=' Third Inversion'
            except:
                pass
        if outp!="":
            outp+=' Key: '+str(root)
        return outp
