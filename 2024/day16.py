from collections import deque

from utils import site 
from utils.ds import p2d 

rows = site.download_input(day=16)

start = None 
end = None 
for y in range(len(rows)):
    for x in range(len(rows[y])):
        if rows[y][x] == 'S':
            start = p2d(x, y)
        if rows[y][x] == 'E':
            end = p2d(x, y)


def turn(d, times=1):
    res = d 
    while times:
        if res == p2d(1, 0):
            res = p2d(0, 1) 
        elif res == p2d(0, 1):
            res = p2d(-1, 0) 
        elif res == p2d(-1, 0):
            res = p2d(0, -1)
        else:
            res = p2d(1, 0)
        times -= 1
    return res


def get_score(start, end, matrix): 
    paths = list()

    scores = {}
    d = p2d(1, 0)
    scores[(start, d)] = 0
    q = deque()
    q.append([(start, d, 0, set())])
    while q:
        path = q.popleft()
        p, d, s, v = path[-1]
        nv = set(v)
        nv.add((p, d))

        if p == end:
            paths.append(path)
        else:
            np = p + d 
            ns = s + 1 
            if matrix[np.y][np.x] != '#':
                if (np, d) not in scores or scores[(np, d)] >= ns:
                    scores[(np, d)] = ns 
                    q.append(list(path) + [(np, d, ns, nv)])
            
            nd = turn(d)
            np = p + nd
            ns = s + 1000 
            if matrix[np.y][np.x] != '#':
                if (np, nd) not in scores or scores[(np, nd)] >= ns:
                    scores[(np, nd)] = ns + 1
                    scores[(p, nd)] = ns
                    q.append(list(path) + [(np, nd, ns, nv)])

            nd = turn(d, times=3)
            np = p + nd
            ns = s + 1000 
            if matrix[np.y][np.x] != '#':
                if (np, nd) not in scores or scores[(np, nd)] >= ns:
                    scores[(np, nd)] = ns + 1
                    scores[(p, nd)] = ns
                    q.append(list(path) + [(np, nd, ns, nv)])

    s1 = scores.get((end, p2d(1, 0))) or 99999999999
    s2 = scores.get((end, p2d(-1, 0))) or 99999999999
    s3 = scores.get((end, p2d(0, 1))) or 99999999999
    s4 = scores.get((end, p2d(0, -1))) or 99999999999
    mscore = min([s1, s2, s3, s4])
    return [p for p in paths if p[-1][2] == mscore], mscore


paths, score = get_score(start, end, rows) 

print(score)
tiles = set()
for path in paths:
    for tile in path:
        tiles.add(tile[0])
print(len(tiles))