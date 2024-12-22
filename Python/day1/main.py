with open('input.txt') as file:
    lines = [l.split() for l in file.read().split('\n')]
#print(lines)


line1 = []; line2 = []
for l in lines:
    line1.append(int(l[0]))
    line2.append(int(l[1]))

#print(line1, line2)

line1.sort()
line2.sort()

#print(line1, line2)

total = 0
for i, j in zip(line1, line2):
    total += abs(j-i)

print('Part 1:', total)
    
###Part 2 

total = 0
for i in line1:
    total += (line2.count(i) * i)

print('Part 2:', total)