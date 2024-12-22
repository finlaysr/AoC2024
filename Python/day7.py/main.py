with open('day7_test.txt') as file:
    data = [i.split(': ') for i in file.read().split('\n')]
data = [[int(i), [int(k) for k in j.split(' ')]] for i, j in data]

print(data)

for d in data:
    for c in 

for i in range(16):
    #print(bin(i))
    print(f'{i:04b}')

