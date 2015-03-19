# Get Input From File

f = open('goals.txt')

content = f.read().splitlines()

f.close()

#Content -> Alternating String/Tuple

goals = []
index = 0

while index + 1 < len(content):
    goalText = content[index]
    goalQualifier = content[index+1]
    if str(goalText)[0] != '#':
        if 'major third' in str(goalQualifier).lower():
            goals.append((str(goalText), (None, 4)))
        elif 'minor third' in str(goalQualifier).lower():
            goals.append((str(goalText), (None, 3)))
        elif 'major triad' in str(goalQualifier).lower():
            goals.append((str(goalText), (None, 0, 0, None)))
        elif 'f# minor diminished triad' in str(goalQualifier).lower():
            goals.append((str(goalText), (6, 2, 0, None)))
        elif 'minor triad' in str(goalQualifier).lower():
            goals.append((str(goalText), (None, 1, 0, None)))
        elif 'perfect fifth' in str(goalQualifier).lower():
            goals.append((str(goalText), (None, 7)))
        else:
            goals.append((str(goalText), (None, None, None, None)))
    index += 2


print goals
