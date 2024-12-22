from time import sleep
with open('day15_test.txt') as file:
    warehouse, moves = file.read().split('\n\n')
warehouse = [list(w) for w in warehouse.splitlines()]
'''
for y in range(len(warehouse)):
    if '@' in warehouse[y]:
        pos = [warehouse[y].index('@'), y]

print(pos)

def move(x:int, y:int):
    global new, pos
    nextPos = new([x, y])

    if warehouse[nextPos[1]][nextPos[0]] == '.':
        if warehouse[y][x] == '@':
            pos = nextPos.copy()
        warehouse[nextPos[1]][nextPos[0]], warehouse[y][x] = warehouse[y][x], warehouse[nextPos[1]][nextPos[0]]
         
    
    elif warehouse[nextPos[1]][nextPos[0]] == 'O':
        move(nextPos[0], nextPos[1])
        if warehouse[nextPos[1]][nextPos[0]] == '.':
            move(x, y)


ds = [0, 1, 0, -1]
d = {'^': 0, '>': 1, 'v': 2, '<':3}

for m in moves:
    if m == '\n':
        continue
    dirn = d[m]
    new = lambda l: [l[0]+ds[dirn], l[1]+ds[::-1][dirn]]
    move(pos[0], pos[1])

print('\n'.join([''.join(i) for i in warehouse]))

total = 0
for y in range(len(warehouse)):
    for x in range(len(warehouse[y])):
        if warehouse[y][x] == 'O':
            total += 100 * y + x

print('Part 1:', total)
'''


# --- Part 2 ---
with open('day15_test.txt') as file:
    temp, moves = file.read().split('\n\n')
temp = [list(w) for w in temp.splitlines()]

warehouse = [[]for _ in range(len(temp))]

r = {'#': '##', 'O': '[]', '.': '..', '@': '@.'}

for i, t in enumerate(temp):
    for c in t:
        warehouse[i] += list(r[c])


print('\n'.join([''.join(i) for i in warehouse]))

pos = []
for y in range(len(warehouse)):
    if '@' in warehouse[y]:
        pos = [warehouse[y].index('@'), y]

print(pos)

def move(x:int, y:int):
    #print('\n'.join([''.join(i) for i in warehouse]))
    global new, pos, canMove
    nextPos = new([x, y])
    print(f'New Move at {x}, {y}')

    if x == nextPos[0] and warehouse[y][x] in ('[', ']'):
        print('1')
        offset = 1 if warehouse[y][x] == '[' else -1
        print(offset)
        
        if warehouse[nextPos[1]][nextPos[0]] == '.' and warehouse[nextPos[1]][nextPos[0] + offset] == '.':
            print('1a')
            warehouse[nextPos[1]][nextPos[0]], warehouse[y][x] = warehouse[y][x], warehouse[nextPos[1]][nextPos[0]]
            warehouse[nextPos[1]][nextPos[0] + offset], warehouse[y][x+offset] = warehouse[y][x+offset], warehouse[nextPos[1]][nextPos[0] + offset]

        elif warehouse[nextPos[1]][nextPos[0]] in ('[', ']'):
            print('1b')
            print(warehouse[nextPos[1]][nextPos[0]],  warehouse[y][x])
            if canMove: 
                move(nextPos[0], nextPos[1])
            if canMove and (warehouse[nextPos[1]][nextPos[0]] != warehouse[y][x] or warehouse[nextPos[1]][nextPos[0]] != '.'):
                move(nextPos[0]+offset, nextPos[1])
            
            if warehouse[nextPos[1]][nextPos[0]] == '.' and warehouse[nextPos[1]][nextPos[0] + offset] == '.':
                move(x, y)

        elif warehouse[nextPos[1]][nextPos[0]+offset] in ('[', ']'):
            print('1c')
            print(warehouse[nextPos[1]][nextPos[0]],  warehouse[y][x])
            if canMove: 
                move(nextPos[0], nextPos[1])
            if canMove and (warehouse[nextPos[1]][nextPos[0]] != warehouse[y][x] or warehouse[nextPos[1]][nextPos[0]] != '.'):
                move(nextPos[0]+offset, nextPos[1])
            
            if warehouse[nextPos[1]][nextPos[0]] == '.' and warehouse[nextPos[1]][nextPos[0] + offset] == '.':
                move(x, y)
        
        else:
            print('1d')
            canMove = False

    else:
        print('2')
        if warehouse[nextPos[1]][nextPos[0]] == '.':
            print('2a')
            if warehouse[y][x] == '@':
                pos = nextPos.copy()
            warehouse[nextPos[1]][nextPos[0]], warehouse[y][x] = warehouse[y][x], warehouse[nextPos[1]][nextPos[0]]
            
        
        elif warehouse[nextPos[1]][nextPos[0]] in ('[', ']'):
            print('2b')
            move(nextPos[0], nextPos[1])
            if warehouse[nextPos[1]][nextPos[0]] == '.':
                move(x, y)
    



ds = [0, 1, 0, -1]
d = {'^': 0, '>': 1, 'v': 2, '<':3}
w = {'w':'^', 'a': '<', 's':'v', 'd':'>'}

while True:
    m = w[input('Move: ')]
    if m == '\n':
        continue

    
    
    dirn = d[m]
    canMove = True
    new = lambda l: [l[0]+ds[dirn], l[1]+ds[::-1][dirn]]
    move(pos[0], pos[1])
    print('\n'.join([''.join([j if j != '@' else m for j in i ]) for i in warehouse]))
    print(m)
    #sleep(0.5)

total = 0
for y in range(len(warehouse)):
    for x in range(len(warehouse[y])):
        if warehouse[y][x] == 'O':
            total += 100 * y + x

print('Part 2:', total)