from time import sleep
with open('day14.txt') as file:
    robots = [[[int(k) for k in j[2:].split(',')] for j in i.split(' ')] for i in file.read().splitlines()]

#print(robots)
dims = [101, 103]

def overlapAdd(curr:int, add:int, limit:int) -> int:
    if curr + add >= limit:
        return curr + add - limit
    elif curr + add < 0:
         return limit + (curr+add)
    else:
        return curr + add



for i in range(999999):
    board = [['.' for _ in range(dims[0])] for _ in range(dims[1])]
    for r in robots:
        r[0] = [overlapAdd(r[0][0], r[1][0], dims[0]), overlapAdd(r[0][1], r[1][1], dims[1])]
        board[r[0][1]][r[0][0]] = '#'
    for b in board:
        if '#######' in ''.join(b):
            print('\n'.join([''.join(i) for i in board]))
            input(i+1)
            break
    #print(i,end='\n\n')
    if i % 1000 == 0:
        print(i)


quadrants = [0,0,0,0]
for r in robots:
    if r[0][0] <= dims[0]//2 -1 and r[0][1] <= dims[1]//2 -1:
        quadrants[0] += 1
    elif r[0][0] >= dims[0] - dims[0]//2 and r[0][1] <= dims[1]//2 -1:
        quadrants[1] += 1
    elif r[0][0] <= dims[0]//2 -1 and r[0][1] >= dims[1] - dims[1]//2:
        quadrants[2] += 1
    elif r[0][0] >= dims[0] - dims[0]//2 and r[0][1] >= dims[1] - dims[1]//2:
        quadrants[3] += 1

print(quadrants)
total = 1
for q in quadrants:
    total *= q
print(total)