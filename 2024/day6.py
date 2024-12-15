from utils import site

rows = site.download_input(day=6)

dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def step(pos, d):
    return (pos[0] + d[0], pos[1] + d[1])


def turn(d, left=False):
    idx = dirs.index(d) + 1 - 2 * int(left)
    return dirs[idx % 4]


def valid(pos):
    return pos[0] in range(len(rows[0])) and pos[1] in range(len(rows))
    

dir = (0, -1)
spos = (0, 0)
barriers = set()

for y in range(len(rows)):
    for x in range(len(rows[y])):
        if rows[y][x] == '#':
            barriers.add((x, y))
        if rows[y][x] == '^':
            spos = (x, y)
  

def walk(pos, dir, maxiter=None):
    it = 0
    path = set()
    path.add(pos)
    while True:
        npos = step(pos, dir)
        if not valid(npos):
            return False, path 
        if npos in barriers:
            dir = turn(dir)
            continue 
        path.add(npos)
        pos = npos 
        it += 1
        if maxiter and it >= maxiter:
            return True, path 


_, path = walk(spos, dir)
print(len(path))

MAX_ITER = len(rows) * len(rows[0]) * 4
cloops = 0
for p in path:
    barriers.add(p)
    looped, _ = walk(spos, (0, -1), MAX_ITER)
    cloops += int(looped)
    barriers.remove(p)
print(cloops)
