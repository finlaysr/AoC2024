import re
with open("input.txt") as file:
    data = file.read()

## --- Part 1 ----
matches = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", data)
total = 0

for m in matches:
    n = [int(i) for i in m[m.index("(") + 1 : m.find(")")].split(",")]
    total += n[0] * n[1]

print('Part 1:', total)


## --- Part 2 ---
matches = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)|(?:don't)|do", data)
total = 0; do = True

for m in matches:
    if m == "do":
        do = True
    elif m == "don't":
        do = False
    else:
        if do:
            n = [int(i) for i in m[m.index("(") + 1 : m.find(")")].split(",")]
            total += n[0] * n[1]

print('Part 2:', total)
