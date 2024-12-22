with open('input.txt') as file:
    data = file.read().split('\n')

total = 0; l = 4

def check(x, y, series):
    global l, total
    curr = ''
    for i in range(l):
        curr += series(x, y, i)
    if curr == 'XMAS' or curr == 'SAMX':
        total += 1

for y in range(len(data)):
    for x in range(len(data[y])):
        if y>=l-1 and x>=l-1: #1
            check(x, y, lambda x, y, i: data[y-i][x-i])  # 1 2 3  
        if y>=l-1: #2                                    # . x 4  
            check(x, y, lambda x, y, i: data[y-i][x])    # . . .
        if y>=l-1 and x<=len(data[y])-l: #3 
            check(x, y, lambda x, y, i: data[y-i][x+i])
        if x<=len(data[y])-l: #4
            check(x, y, lambda x, y, i: data[y][x+i])

print('Part 1:', total)

### ---Part 2 ---
corrects = [['M.M', '.A.', 'S.S'], 
            ['M.S', '.A.', 'M.S'],
            ['S.M', '.A.', 'S.M'],
            ['S.S', '.A.', 'M.M']]

total = 0; l = 3

for y in range(len(data)-l+1):
    for x in range(len(data[y])-l+1):
        curr = [i[x:x+l] for i in data[y:y+l]]
        for correct in corrects:
            valid = True
            for cu, co in zip(curr, correct): 
                for i, j in zip(cu, co):
                    if not(j == "." or i == j):
                        valid = False
            if valid:
                total += 1

print('Part 2:', total)
            
            