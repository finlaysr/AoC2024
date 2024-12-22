with open('day11_test.txt') as file:
    stones = [int(i) for i in file.read().split(' ')]

print(stones)

keyVals = [1, 1, 2, 4, 4, 7, 14, 16, 20, 39, 62, 81, 110, 200, 328, 418, 667, 1059, 1546, 2377, 3572, 5602, 8268, 12343, 19778, 29165, 43726, 67724, 102131, 156451, 234511, 357632, 549949, 819967, 1258125, 1916299, 2886408, 4414216, 6669768, 10174278]

for i in range(75):
    new = []
    for s in stones:
        if s == 0:
            new.append(1) 
        elif len(str(s))%2 == 0:
            ss = str(s)
            l = len(ss)
            new.append(int(ss[:l//2]))
            new.append(int(ss[l//2:])) 
        else:
            new.append(s*2024)
    stones = new.copy()
    print(i)#, end=': ') 
    print(len(stones), max(stones))

    #print((stones.count(0)+stones.count(1))/len(stones)*100, '%')
    keyVals.append(len(stones))

'''
iteration = 1
while iteration < 1:
    index = 0
    while index < len(stones):
        s = stones[index]
        if s == 0:
            stones[index] = 1
        elif len(str(s))%2 == 0:
            ss = str(s)
            l = len(ss)
            stones[index] = int(ss[:l//2])
            index += 1
            stones.insert(index, int(ss[l//2:]))
        else:
            stones[index] = s*2024
        
        index += 1
    
    iteration += 1

    print(stones)
'''
print(keyVals)