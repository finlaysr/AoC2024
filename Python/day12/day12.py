from time import perf_counter
with open('day12_test.txt') as file:
    data = file.read().splitlines()

#print(data)
areas = []

def mover(kind: str, pos: list[int]):
    global prev
    prev.append([pos[0], pos[1]])
    done = True
    if pos[1] > 0 and [pos[0], pos[1]-1] not in prev and data[pos[1]-1][pos[0]] == kind:  #up
        mover(kind, [pos[0], pos[1]-1])
        done = False
    if pos[0] < len(data[0])-1 and [pos[0]+1, pos[1]] not in prev and data[pos[1]][pos[0]+1] == kind: #right
        mover(kind, [pos[0]+1, pos[1]])
        done = False
    if pos[1] < len(data)-1 and [pos[0], pos[1]+1] not in prev and data[pos[1]+1][pos[0]] == kind:  #down
        mover(kind, [pos[0], pos[1]+1])
        done = False
    if pos[0] > 0 and [pos[0]-1, pos[1]] not in prev and data[pos[1]][pos[0]-1] == kind: #left
        mover(kind, [pos[0]-1, pos[1]])
        done = False
    
    if done:
        return

start = perf_counter()
prevType = ''
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == prevType:
            continue
        prev = []

        mover(data[y][x], [x, y])
        if sorted(prev) not in areas:
            areas.append(sorted(prev))
        prevType = data[y][x]

end = perf_counter()

print(f'Time: {end-start}')

#print(areas)

pers = []
total = 0
for area in areas:
    temp = []
    per = 0
    for p in area:
        if [p[0], p[1]+1] not in area:
            per += 1
            temp.append(p)
        if [p[0], p[1]-1] not in area:
            per += 1
            temp.append(p)
        if [p[0]+1, p[1]] not in area:
            per += 1
            temp.append(p)
        if [p[0]-1, p[1]] not in area:
            per += 1
            temp.append(p)
    pers.append(temp)
    #print(f'{data[p[1]][p[0]]}: {len(area)} * {per} = {len(area) * per}')

    total += len(area) * per


from copy import deepcopy
template = [['.' for _ in range(len(data[0]))] for _ in range(len(data))]

for area in areas:
    tCopy = deepcopy(template)
    for a in area:
        tCopy[a[1]][a[0]] = data[a[1]][a[0]]
    
    for l in tCopy:
        print(''.join(l))
    print('')


print(total)