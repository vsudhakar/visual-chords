# Get Input From File

f = open('goalInput.txt')

content = f.read().splitlines()

f.close()

#Content -> Alternating String/Tuple

goals = []
index = 0

while index + 1 < len(content):
    str = content[index]
    tup = content[index+1]
    goals.append((eval(str), eval(tup)))
    index += 1


for goal in goals:
    print goal
