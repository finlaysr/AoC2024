with open("day9_input.txt") as file:
    diskMap = file.read()

disk = []
fileMode = False; ID = -1
for char in diskMap:
    fileMode = not fileMode
    if fileMode:
        ID += 1
    for _ in range(int(char)):
        disk.append(ID if fileMode else -1)

while disk.count(-1) > 0:
    if disk[-1] != -1:
        disk[disk.index(-1)] = disk[-1]
    disk.pop(-1)

checksum = 0
for i in range(len(disk)):
    checksum += disk[i]*i
print('Part 1:', checksum)

# --- Part 2 ---
disk = []
fileMode = False; ID = -1
for char in diskMap:
    fileMode = not fileMode
    if fileMode:
        ID += 1
    if int(char) != 0:
        disk.append([ID if fileMode else -1 for _ in range(int(char))])

ID = max(disk, key=lambda l:l[0])[0]
while ID > 0:
    for i in range(len(disk)):
        if disk[i][0] == ID:
            size = len(disk[i])
            loc = i
            break
    
    for i in range(len(disk)):
        if disk[i][0] == -1 and len(disk[i]) >= size and i < loc:
            disk[loc] = [-1 for _ in range(size)]
            disk[i] = disk[i][size:]
            if len(disk[i]) == 0: 
                disk.pop(i)
            disk.insert(i, [ID for _ in range(size)])
            break
    ID -= 1

checksum = 0
index = 0
for d in disk:
    for c in d:
        if c != -1:
            checksum += index*c
        index += 1

print('Part 2:', checksum)