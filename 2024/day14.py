from collections import defaultdict
from functools import reduce
from utils import site 

rows = site.download_input(day=14)

robots = [] 
for row in rows:
    items = row.split()
    p = [int(c) for c in items[0][2:].split(",")]
    v = [int(c) for c in items[1][2:].split(",")]
    robots.append((tuple(p), tuple(v)))


def sym_score(state, space):
    mstate = [(s[0] - (space[0] // 2), s[1]) for s in state]
    symm = [int((-s[0], s[1]) in mstate) for s in mstate]
    return sum(symm) / len(symm)


def safety_factor(sec, space, robots, pprint=False):
    quads = {
        (0, 0): 0, 
        (0, 1): 0,
        (1, 0): 0, 
        (1, 1): 0
    }
    state = defaultdict(int)
    for (p, v) in robots: 
        dx, dy = sec * v[0], sec * v[1]
        npx, npy = p[0] + dx, p[1] + dy 
        # tx, ty = npx // space[0], npy // space[1]
        npx, npy = npx % space[0], npy % space[1]
        state[(npx, npy)] += 1
        if npx != space[0] // 2 and npy != space[1] // 2:
            qx, qy = npx > space[0] // 2, npy > space[1] // 2
            quads[(int(qx), int(qy))] += 1

    if pprint:
        for x in range(space[0]):
            for y in range(space[1]):
                print(state.get((x, y)) or '.', end='')
            print('')
    return reduce(lambda a, x : a * x, quads.values(), 1), sym_score(state, space)


factor, _ = safety_factor(100, (101, 103), robots)
print(factor)

for i in range(10000):
    _, sscore = safety_factor(i, (101, 103), robots)
    if sscore > 0.1:
        print(i, sscore)
