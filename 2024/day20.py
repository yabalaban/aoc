from collections import defaultdict, deque

from utils import site 
from utils.ds import p2d 

rows = site.download_input(day=20)

d = [p2d(1, 0), p2d(-1, 0), p2d(0, 1), p2d(0, -1)]
size = p2d(len(rows[0]), len(rows))
start, end = None, None 
walls = set() 
for y in range(len(rows)):
    for x in range(len(rows[y])):
        if rows[y][x] == '#':
            walls.add(p2d(x, y))
        if rows[y][x] == 'S': 
            start = p2d(x, y)
        if rows[y][x] == 'E': 
            end = p2d(x, y)


def shortest_path(start, walls):
    scores = {}
    scores[start] = 0
    q = deque()
    q.append(start)
    while q:
        pos = q.popleft() 
        score = scores[pos]
        npos = [pos + d_ for d_ in d]
        npos = [pos for pos in npos if pos not in walls]
        npos = [pos for pos in npos if pos not in scores or score + 1 < scores[pos]]
        for pos in npos:
            scores[pos] = score + 1
            q.append(pos)
    return scores


def cheat(scores, ct):
    res = defaultdict(set)
    score_ = {}
    for path, minscore in scores.items():
        for d_ in d:
            cscores = []
            for dx in range(-ct, ct + 1):
                for dy in range(-ct + abs(dx), ct - abs(dx) + 1):
                    npos = p2d(dx, dy) + path + d_
                    cscores.append((npos, scores.get(npos), abs(dx) + abs(dy) + 1))
           
            cscores = list(filter(lambda x: x[1] is not None and x[1] >= minscore, cscores))
            if len(cscores) < 2:
                continue
            for cscore in cscores:
                if cscore[1] < minscore:
                    continue
                nscore = cscore[1] - minscore - cscore[2]
                key = (path, cscore[0])
                if key in score_:
                    if score_[key] <= nscore:
                        res[score_[key]].remove(key)
                    else:
                        continue
                res[nscore].add(key)
                score_[key] = nscore
    return res


scores = shortest_path(start, walls)
savings = cheat(scores, 1)
print(sum([len(v) for k, v in savings.items() if k >= 100]))
savings = cheat(scores, 19)
print(sum([len(v) for k, v in savings.items() if k >= 100]))