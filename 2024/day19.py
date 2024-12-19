from utils import site 

rows = site.download_input(day=19)

patterns = rows[0].split(', ')
designs = rows[2:]


def match(design, patterns):
    if design in cache:
        return cache[design]
    if not design:
        return 1
    res = 0
    for pattern in patterns:
        if design.startswith(pattern):
            ps = match(design[len(pattern):], patterns)
            res += ps
            cache[design[len(pattern):]] = ps
    return res 


cache = {} 
for p in patterns:
    cache[p] = match(p, patterns) 


possible = 0 
total = 0
for i, design in enumerate(designs):
    l = match(design, patterns)
    if l:
        possible += 1
    total += l
print(possible)
print(total)
