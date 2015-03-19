from locals import *
def parsechord(chord):


    interval=["Minor Second", "Major Second", "Minor Third", "Major Third", "Perfect Fourth", "Augmented Fourth", "Perfect Fifth", "Minor Sixth", "Major Sixth", "Minor Seventh", "Major Seventh", "Perfect Octave"]
    tonality=["Major", "Minor", "Diminished", "Augmented", "Major", "Major-Minor", "Minor-Major", "Minor", "Half-diminished", "Full diminished", "Augmented"]
    ctype=["Triad", "Seventh"]
    inversion=["First", "Second", "Third"]
    try:
        if chord==None:
            return ""
        elif len(chord)==1:
            return KEYOF(chord[0])
        elif len(chord)==2:
            return interval[chord[1]-1]+" above "+KEYOF(chord[0])
        elif len(chord)==4:
            s=KEYOF(chord[0])+" "+tonality[chord[1]]+" "+ctype[chord[2]]
            if chord[3]>0:
                s+=" "+inversion[chord[3]-1]+" Inversion"
            return s
    except:
        print "ERROR: ",
        print chord
        return "ERROR"
