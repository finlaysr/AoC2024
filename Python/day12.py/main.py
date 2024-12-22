with open('test.txt') as file:
    data = file.read().splitlines()

print(data)

areas = {}

for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] in areas:
            areas[data[y][x]].append([x,y])
        
        else:
            areas[data[y][x]] = [[x, y]]

print(areas)

for area in areas:
    print(area)
    print(len(areas[area]))
    points = areas[area]
    per = 0
    for p in points:
        if [p[0], p[1]+1] not in points:
            per += 1