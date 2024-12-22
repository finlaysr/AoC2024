with open('test.txt') as file:
    stones = [int(i) for i in file.read().split(' ')]

print(stones)

for i in range(3):
    new = []
    for s in stones:
        if s == 0:
            new.append(1)
        elif len(str(s))%2 == 0:
            l = len(str(s))
            new.append()