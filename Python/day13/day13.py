from numpy import array, linalg

with open('day13_test.txt') as file:
    machines = [f.split('\n') for f in file.read().split('\n\n')]
machines = [[ [m[0][m[0].index(':')+2: ].split(', '), m[1][m[1].index(':')+2: ].split(', ')], m[2][m[2].index(': ')+2:].split(', ')] for m in machines]

total = 0
for m in machines:
    xs = [int(m[0][0][0][2:]), int(m[0][1][0][2:])]
    ys = [int(m[0][0][1][2:]), int(m[0][1][1][2:])]
    targets = [int(i[2:])+10000000000000 for i in m[1]] #Remove 10000000000000 for part 1

    xys = array([[*xs], [*ys]])
    targets = array([*targets])

    answer = linalg.solve(xys, targets)
    if round(answer[0], 2) % 1 == 0 and round(answer[1], 4) % 1 == 0:
        total += answer[0]*3+answer[1]

print(int(total))