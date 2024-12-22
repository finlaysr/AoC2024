with open('day7_input.txt') as file:
    data = [i.split(': ') for i in file.read().split('\n')]
data = [[int(i), [int(k) for k in j.split(' ')]] for i, j in data]

total = 0
for d in data:
    l = len(d[1])-1
    combs = [f'{i:0{l}b}' for i in range(2**l)]
    valid = False
    for comb in combs:
        t = d[1][0]
        for c in range(len(comb)):
            if comb[c] == '0':
                t += d[1][c+1]
            else:
                t *= d[1][c+1]
        if t == d[0]:
            valid = True
            total += t
            break

print('Part 1:', total)


##Part 2
from numpy import base_repr
total = 0
for d in data:
    l = len(d[1])-1
    combs = [f'{int(base_repr(i, 3)):0{l}}' for i in range(3**l)]
    valid = False
    for comb in combs:
        t = d[1][0]
        for c in range(len(comb)):
            if comb[c] == '0':
                t += d[1][c+1]
            elif comb[c] == '1':
                t *= d[1][c+1]
            else:
                t = str(t)
                t += str(d[1][c+1])
                t = int(t)
        
        if t == d[0]:
            valid = True
            total += t
            break

print('Part 2:', total)
