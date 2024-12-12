from collections import defaultdict, deque
from itertools import product
import utils 

rows = utils.download_input(day=12)
nx, ny = len(rows[0]), len(rows)


def valid(x, y):
    return y in range(ny) and x in range(nx)
    

def check(x, y, c, uid):
    if not valid(x, y):
        return False
    return rows[y][x] + f'_{uid}' == c
 
d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
area = defaultdict(int)
sides = defaultdict(set)
uid = 0
visited = set() 

for xy in product(range(nx), range(ny)):
    if xy in visited:
        continue 

    region = deque() 
    plot = rows[xy[1]][xy[0]] + f'_{uid}'
    region.append(xy)
    while region:
        xy = region.popleft()
        if xy in visited:
            continue 

        visited.add(xy)
        area[plot] += 1 
        for dxy in d: 
            nxy = (xy[0] + dxy[0], xy[1] + dxy[1])
            if check(nxy[0], nxy[1], plot, uid):
                region.append(nxy)
            else:
                sides[plot].add((xy, dxy))
    uid += 1

res1 = 0 
assert len(sides) == len(area)
for plot in area:
    res1 += area[plot] * len(sides[plot])
print(res1)


def count_sides(s):
    sides = defaultdict(set)
    for xy, d in s:
        idx = 0 if d[1] == 0 else 1
        sides[(xy[idx], d[idx], idx)].add(xy[(idx + 1) % 2])
      
    c = 0
    for _, idxs in sides.items():
        idxs = sorted(idxs)
        c += 1
        for pi, i in zip(idxs, idxs[1:]):
            if i - pi > 1:
                c += 1 
    return c

res2 = 0 
assert len(sides) == len(sides)
for plot in area:
    cs = count_sides(sides[plot])
    res2 += area[plot] * cs
print(res2)