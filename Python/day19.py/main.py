import re
with open('test.txt') as file:
    patterns, rugs = file.read().split('\n\n')
patterns = patterns.split(', ')
rugs = rugs.splitlines()


def check(rug, indent=''):
    global patterns, done
    if done: 
        return

    #print(f'{indent}{rug=}')
    for pattern in patterns:
        if not pattern in rug:
            continue

        locs = [m.start() for m in re.finditer(f'(?={pattern})', rug)]
        valids = [rug[:loc] + ',' + rug[loc+len(pattern):] for loc in locs]
        
        #if len(valids) > 0 and False: print(f'{indent}_{pattern=}\n{indent}__{valids=}')

        for v in valids:
            if all(c==',' for c in v):
                done = True
                return
            check(v, indent=indent+'.')

total = 0
for r in rugs:

    done = False
    check(r)
    print(done, r)
    if done:
        total += 1

print(total)
    