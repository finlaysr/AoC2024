from copy import deepcopy

with open('input.txt') as file:
    dataOrig = [list(i) for i in file.read().split('\n')]
data = deepcopy(dataOrig)

for y in range(len(data)):
    if '^' in data[y]:
        posOrig = [data[y].index('^'), y]

def move(x, y):
    global done, pos, data, dirn, loop
    if x(pos[0]) < 0 or x(pos[0]) >= len(data[0]) or y(pos[1]) < 0 or y(pos[1]) >= len(data):
        done = True; return
    
    if data[y(pos[1])][x(pos[0])] == '#':
        dirn = dirn + 1 if dirn < 3 else 0
    else:
        data[pos[1]][pos[0]] = m[dirn]
        pos = [x(pos[0]), y(pos[1])]
        #Only for Part 2
        if dirn in prevPos[pos[1]][pos[0]]:
            loop = True
        else:
            prevPos[pos[1]][pos[0]].append(dirn)
        
    #print('\n'.join([''.join(i) for i in data]), end='\n\n')
    
dirn = 0
done = False
m = {0: '^', 1: '>', 2: 'v', 3:'<'}
prevPos = [[[] for _ in range(len(data[0]))] for _ in range(len(data))]
pos = posOrig.copy()
loop = False

rotation = [0, 1, 0, -1]
while not done:
    move(lambda l: l+rotation[dirn], lambda l: l+rotation[::-1][dirn])

#print('\n'.join([''.join(i) for i in data]))

total = 1
for d in data:
    total += d.count('^') + d.count('>') + d.count('v') + d.count('<')
print('Part 1:', total)

# --- Part 2 ---
loops = 0
for ver in range(len(data)*len(data[0])):
    prevPos = [[[] for _ in range(len(data[0]))] for _ in range(len(data))]
    y = ver//len(data); x = ver%len(data[0])
    data = deepcopy(dataOrig)
    pos = posOrig.copy()
    if pos[0] == x and pos[1] == y: #don't replace starting pos
        continue
    
    data[y][x] = '#'
    dirn = 0
    done = False
    loop = False
    prevPos[pos[1]][pos[0]].append(dirn)
    while not done and not loop:
        move(lambda l: l+rotation[dirn], lambda l: l+rotation[::-1][dirn])
    if loop:
        loops+=1
        
    if ver % 100 == 0:
        print(ver, loops)

print('Part 2:', loops)