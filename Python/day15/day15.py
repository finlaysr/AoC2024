from time import sleep
with open('day15_test.txt') as file:
    warehouse, moves = file.read().split('\n\n')

warehouse = [list(w) for w in warehouse.splitlines()]

print(warehouse, moves)

for y in range(len(warehouse)):
    if '@' in warehouse[y]:
        pos = [warehouse[y].index('@'), y]

print(pos)

def move(x, y):
    sleep(0.1)
    global pos, done, cursor
    print('\n'.join([''.join(i) for i in warehouse]))
    if warehouse[y(cursor[1])][x(cursor[0])] == '.'

    if warehouse[y(cursor[1])][x(cursor[0])] == '.':
        prev = warehouse[cursor[1]][cursor[0]]
        warehouse[cursor[1]][cursor[0]] = '.'
        cursor = [x(cursor[0]), y(cursor[1])]
        warehouse[cursor[1]][cursor[0]] = prev

    elif warehouse[y(cursor[1])][x(cursor[0])] == 'O':
        warehouse[cursor[1]][cursor[0]] = 'O'
        warehouse[y(cursor[1])][x(cursor[0])] = '.'

    elif warehouse[y(cursor[1])][x(cursor[0])] == '#':
        done = True

ds = [0, 1, 0, -1]
d = {'^': 0, '>': 1, 'v': 2, '<':3}
print('\n'.join([''.join(i) for i in warehouse]))

for m in moves:
    print(m)
    dirn = d[m]
    done = False
    cursor = pos.copy()
    while not done:
        move(lambda l: l+ds[dirn], lambda l: l+ds[::-1][dirn])
        
        
