
program = [2,4,1,2,7,5,4,5,0,3,1,7,5,5,3,0]
target = '2,4,1,2,7,5,4,5,0,3,1,7,5,5,3,0,'


def combo(num):
    global regs
    if num >= 0 and num <= 3:
        return num
    elif num == 4:
        return regs['A']
    elif num == 5:
        return regs['B']
    elif num == 6:
        return regs['C']
    elif num == 7:
        raise 'Invalid Combo Number'
    

def instruction(code, num):
    #print(f'{code=}, {num=}')
    global regs, index, output
    if code == 0:
        regs['A'] = int(regs['A'] / (2 ** (combo(num))))
    elif code == 1:
        regs['B'] = regs['B'] ^ num
    elif code == 2:
        regs['B'] = combo(num) % 8
    elif code == 3:
        if regs['A'] != 0:
            index = num - 2
    elif code == 4:
        regs['B'] = regs['B'] ^ regs['C']
    elif code == 5:
        output += str(combo(num) % 8) + ','
    elif code == 6:
        regs['B'] = int(regs['A'] / (2 ** (combo(num))))
    elif code == 7:
        regs['C'] = int(regs['A'] / (2 ** (combo(num))))
    index += 2

print(program)
i = 0 #2717100000 searched up to
output = ''
while output != target:
    index = 0
    output = ''
    regs = {'A': i, 'B': 0, 'C': 0}
    while index < len(program):
        #print(index)
        instruction(program[index], program[index+1])
    if i % 100000 == 0:
        print(i)
    i += 1

#print(f'{regs}, {output=}')
print(output)
print(i-1)
