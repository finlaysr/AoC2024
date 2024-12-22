with open('input.txt') as file:
    data = [list(i) for i in file.read().split('\n')]

positions: dict[list[int]] = {}

for line in range(len(data)):
    for char in range(len(data[0])):
        c = data[line][char]
        if c != '.':
            if c not in positions:
                positions[c] = [[char, line]]
            else:
                positions[c].append([char, line])

result = [['.' for _ in range(len(data[0]))] for _ in range(len(data))]

for char in positions:
    locs = positions[char]
    for first in range(len(locs)):
        for second in range(first+1, len(locs)):
            a = locs[first]; b = locs[second] 
            antinodes = [[a[0]-(b[0]-a[0]), a[1]-(b[1]-a[1])], [b[0]+(b[0]-a[0]), b[1]+(b[1]-a[1])]]

            for a in antinodes:
                if a[0] >= 0 and a[0] < len(result[1]) and a[1] >= 0 and a[1] < len(result):
                    result[a[1]][a[0]] = '#'

print('\n'.join([''.join(i) for i in result]))
total = sum(i.count('#') for i in result)
print('Part 1:', total)


# --- Part 2 ---
result = [['.' for _ in range(len(data[0]))] for _ in range(len(data))]

for char in positions:
    locs = positions[char]
    for first in range(len(locs)):
        for second in range(first+1, len(locs)):
            a = locs[first]; b = locs[second] 

            m = (b[1] - a[1]) / (b[0] - a[0])
            c = a[1] - (m*a[0])

            for y in range(len(data)):
                x = round((y - c)/m, 4)
                
                if x % 1 == 0 and x < len(result[0]) and x >= 0:
                    result[int(y)][int(x)] = '#'

print('\n'.join([''.join(i) for i in result]))
total = sum(i.count('#') for i in result)
print('Part 2:', total)