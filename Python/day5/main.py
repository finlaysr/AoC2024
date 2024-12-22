with open("input.txt") as file:
    rules, pages = file.read().split('\n\n')
rules = [[int(i) for i in r.split('|')] for r in rules.split('\n')]
pages = [[int(i) for i in p.split(',')] for p in pages.split('\n')]


total = 0
invalids = []

for page in pages:
    valid = True
    for p in page:
        for rule in rules:
            
            if p == rule[0] and rule[1] in page:
                if page.index(p) > page.index(rule[1]):
                    valid = False
                    if page not in invalids: invalids.append(page)
                    
            elif p == rule[1] and rule[0] in page:
                if page.index(p) < page.index(rule[0]):
                    valid = False
                    if page not in invalids: invalids.append(page)
                    
            
    if valid:
        total += page[(len(page)-1)//2]
        
print('Part 1:', total)

## --- Part 2 ---
total = 0
for _ in range(2): #Run it twice and it works
    for i in range(len(invalids)):
        inv = invalids[i]
        for p in inv:
            for rule in rules:
                if p == rule[0] and rule[1] in inv:
                    if inv.index(p) > inv.index(rule[1]):
                        invalids[i].insert(inv.index(rule[1]), invalids[i].pop(inv.index(p)))
                
                elif p == rule[1] and rule[0] in inv:
                    if inv.index(p) < inv.index(rule[0]):
                        invalids[i].insert(inv.index(p), invalids[i].pop(inv.index(rule[0])))

for inv in invalids:
    total += inv[(len(inv)-1)//2]
print('Part 2:', total)

#Just for checking all have been corrected
trues = 0
for page in invalids:
    valid = True
    for p in page:
        for rule in rules:
            if p == rule[0] and rule[1] in page:
                if page.index(p) > page.index(rule[1]):
                    valid = False

            elif p == rule[1] and rule[0] in page:
                if page.index(p) < page.index(rule[0]):
                    valid = False

    if valid: 
        trues += 1

print("Corrected:",trues, "/", len(invalids))
