with open('input.txt') as file:
    reports = [[int(j) for j in i.split()] for i in file.read().split('\n')]

def check(array:list) -> bool:
    ascending = True if array[1] > array[0] else False
    
    for level in range(len(array)-1):
        diff = array[level+1] - array[level]
        if not((ascending and diff>0 and diff <= 3) or (not ascending and diff<0 and diff >= -3)):
            return False
    
    return True

total = 0
invalids = []
for r in reports:
    if check(r): 
        total += 1
    else:
        invalids.append(r.copy())

print('Part 1:', total)


for r in invalids:
    for i in range(len(r)):
        curr = r.copy(); curr.pop(i)
        if check(curr): 
            total += 1
            break

print('Part 2:', total)