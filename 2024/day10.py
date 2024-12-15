from collections import defaultdict, deque
from utils import site 

rows = site.download_input(day=10)
rows = [[int(x) for x in row] for row in rows]

dir = [(0, -1), (0, 1), (-1, 0), (1, 0)]
trailheads = set()

for y in range(len(rows)):
    for x in range(len(rows[y])):
        rows[y][x] = int(rows[y][x])
        if rows[y][x] == 0:
            trailheads.add((x, y))

res1 = 0
res2 = 0
for trailhead in trailheads:
    trails = deque() 
    trails.append(trailhead)
    nines = defaultdict(int) 
    while trails:
        p = trails.popleft()
        if rows[p[1]][p[0]] == 9:
            nines[p] += 1 
            continue 
        cand = [(p[0] + d[0], p[1] + d[1]) for d in dir]
        cand = [c for c in cand if c[0] in range(len(rows[y])) and c[1] in range(len(rows))]
        cand = [c for c in cand if rows[c[1]][c[0]] - rows[p[1]][p[0]] == 1]
        trails.extend(cand)
    res1 += len(nines.keys())
    res2 += sum(nines.values())

print(res1)
print(res2)