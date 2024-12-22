from copy import deepcopy
from time import sleep
import sys
sys.setrecursionlimit(10**6)

with open('day16_test.txt') as file:
    maze = file.read().splitlines()

for y in range(len(maze)):
    if 'S' in maze[y]:
        start = [maze[y].index('S'), y]
    if 'E' in maze[y]: 
        end = [maze[y].index('E'), y]

#print('\n'.join([''.join(i) for i in maze]))
print(f'Start: {start}, end: {end}')

amount = 0
def mover(pos: list, facing:int, prev:list, score:int):
    #sleep(0.1)
    #print(pos)
    global scores, shortestPath, amount
    amount += 1
    if maze[pos[1]][pos[0]] == 'E':
        scores.append(score)
        print(min(scores))
        if score <= min(scores):
            shortestPath = prev
        return
    
    if score >= min(scores):
        return
    
    newPrev = prev.copy()
    newPrev.append(pos)
    
    for dx, dy, i in ((0, -1, 0), (1, 0, 1), (0, 1, 2), (-1, 0, 3)):  #up, right, down, left
        new = [pos[0]+dx, pos[1]+dy]
        if new not in prev and new[0] >= 0 and new[0] < len(maze[0]) and new[1] >= 0 and new[1] < len(maze):
            if maze[new[1]][new[0]] != '#':
                mover(new.copy(), i, newPrev, score+add[abs(i-facing)])
                
    if amount % 1000 == 0:
        print(amount)

add = {0: 1, 1: 1001, 2: 2001, 3:1001}

total = 0
scores = [len(maze) * len(maze) * 2001]
shortestPath = []

mover(start, 1, [].copy(), 0)

shortest = min(scores)
print(shortest)
print(shortestPath)
print('here')


temp = [list(i) for i in maze]
for s in shortestPath:
    temp[s[1]][s[0]] = 'o'
print('\n'.join([''.join(t) for t in temp]))
print('here2')