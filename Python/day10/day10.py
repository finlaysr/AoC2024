with open('day10_input.txt') as file:
    data = [[int(i) for i in list(f)] for f in file.read().splitlines()]

starts = []
for y in range(len(data)):
    for x in range(len(data)):
        if data[y][x] == 0:
            starts.append([x, y])

def mover(pos: list[int], prev:list):
    if data[pos[1]][pos[0]] == 9:
        if pos not in heads: #remove this condition for part 2
            heads.append(pos)
        return
    
    newPrev = prev.copy()
    newPrev.append(pos)
    if pos[1] > 0 and [pos[0], pos[1]-1] not in prev and data[pos[1]-1][pos[0]] - data[pos[1]][pos[0]] == 1:  #up
        mover([pos[0], pos[1]-1], newPrev)
    if pos[0] < len(data[0])-1 and [pos[0]+1, pos[1]] not in prev and data[pos[1]][pos[0]+1] - data[pos[1]][pos[0]] == 1: #right
        mover([pos[0]+1, pos[1]], newPrev)
    if pos[1] < len(data)-1 and [pos[0], pos[1]+1] not in prev and data[pos[1]+1][pos[0]] - data[pos[1]][pos[0]] == 1:  #down
        mover([pos[0], pos[1]+1], newPrev)
    if pos[0] > 0 and [pos[0]-1, pos[1]] not in prev and data[pos[1]][pos[0]-1] - data[pos[1]][pos[0]] == 1: #left
        mover([pos[0]-1, pos[1]], newPrev)

total = 0
for s in starts:
    heads = []
    mover(s, [].copy())
    total += len(heads)

print(total)