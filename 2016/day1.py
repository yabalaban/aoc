from utils import site 


rows = site.download_input(day=1, year=2016)

rules = {'R': 0 - 1j, 'L': 0 + 1j}
dir = 0 + 1j
pos = 0 + 0j
visited = set()
visited.add(pos)

dvisit = None
for cmd in rows[0].split(', '):
    dir *= rules[cmd[0]]
    step = int(cmd[1:])
    while step:
        pos += dir 
        if pos in visited and not dvisit:
            dvisit = pos 
        visited.add(pos)
        step -= 1

print(abs(pos.real) + abs(pos.imag))
print(abs(dvisit.real) + abs(dvisit.imag))