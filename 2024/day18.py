from collections import deque

from utils import site 
from utils.ds import p2d 

rows = site.download_input(day=18)

d = [p2d(1, 0), p2d(-1, 0), p2d(0, 1), p2d(0, -1)]
bytes_ = [p2d(int(x[0]), int(x[1])) for x in [x.split(',') for x in rows]]


def shortest_path(start, end, size, bs):
    scores = {}
    scores[start] = ([start], 0)
    
    q = deque()
    q.append(start)
    while q:
        pos = q.popleft() 
        path, score = scores[pos]
        npos = [pos + d_ for d_ in d]
        npos = [pos for pos in npos if pos not in bs]
        npos = [pos for pos in npos if pos.x in range(size) and pos.y in range(size)]
        npos = [pos for pos in npos if pos not in scores or score + 1 < scores[pos][1]]
        for pos in npos:
            scores[pos] = path + [pos], score + 1
            q.append(pos)
    return scores.get(end)

spath = shortest_path(p2d(0, 0), p2d(70, 70), 71, bytes_[:1024])
print(spath[1])

while True:
    spos = set(spath[0])
    for i in range(1024, len(bytes_)):
        if bytes_[i] in spos:
            spath = shortest_path(p2d(0, 0), p2d(70, 70), 71, bytes_[:i])
            if spath == None:
                print(i, bytes_[i - 1])
                break 
            spos = set(spath[0])
        
