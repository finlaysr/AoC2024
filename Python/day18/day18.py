with open('day18_test.txt') as file:
    coords = [[int(j) for j in i.split(',')] for i in file.read().splitlines()]

size = 70+1
falling = 1024
coords = coords[:falling]
shortest = size**2-falling

#board = [['.' for _ in range(size)] for _ in range(size)]
#for i in coords: board[i[1]][i[0]] = '#' 
#print('\n'.join([''.join(i) for i in board]))

d = ((0, -1), (1, 0), (0, 1), (-1, 0))
amount = 1

def mover(pos: list, prev:list, dist:int):
    global coords, shortest, amount, d, size
    #print(f'{indent}{pos}')
    if pos[0] == size - 1 and pos[1] == size -1:
        if dist < shortest:
            shortest = dist
            print(shortest)
        return

    newPrev = prev.copy()
    newPrev.append(pos)

    for dx, dy in d:
        new = [pos[0]+dx, pos[1]+dy]

        if new not in prev and new[0] >= 0 and new[0] < size and new[1] >= 0 and new[1] < size and dist+1 <= 566:
            if new not in coords:
                amount += 1
                mover(new, newPrev, dist+1)
    if amount%1000 == 0:
        print(amount)

mover([0,0], [], 0)

print(shortest)