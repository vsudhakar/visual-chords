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
    goals.append((str(goalText), str(goalQualifier).lower()))
    index += 1


print goals
