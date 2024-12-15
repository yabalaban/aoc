from utils import p2d, p3d
import utils 

rows = utils.download_input(day=15)


d = { "^": p2d(0, -1), "v": p2d(0, 1), "<": p2d(-1, 0), ">": p2d(1, 0) }


def parse_input(rows):
    walls = set()
    boxes = set()
    pos = None 

    split = rows.index('')
    size = p2d(len(rows[0]), len(rows[:split]))
    for y, row in enumerate(rows[:split]):
        for x, c in enumerate(row):
            if c == '#':
                walls.add(p2d(x, y))
            if c == 'O':
                boxes.add(p2d(x, y))     
            if c == '@':
                pos = p2d(x, y)
    moves = ''.join(rows[split + 1:])
    return walls, boxes, pos, moves, size 


def update(pos, move, walls, boxes):
    npos = pos + d[move]
    if npos in walls:
        return pos
    elif npos in boxes: # simple case
        tpos = npos + d[move]
        rpos = None 
        while True:
            if tpos in walls:
                break 
            elif tpos in boxes:
                tpos = tpos + d[move]
            else:
                rpos = tpos 
                break
        if rpos:
            boxes.remove(npos)
            boxes.add(rpos)
            return npos 
        else:
            return pos 
    elif p3d(npos.x, npos.y, 0) in boxes or p3d(npos.x, npos.y, 1) in boxes: # extended case
        tpos = [npos + d[move]] 
        isv = move in {'^', 'v'} 
        if isv:
            dx = 1 if p3d(npos.x, npos.y, 0) in boxes else -1 
            tpos.append(npos + d[move] + p2d(dx, 0))

        clear = False 
        mbox = set()
        mbox.add(npos)

        while True:
            if any([p in walls for p in tpos]):
                break 

            ntpos = []
            for p in tpos:
                if p3d(p.x, p.y, 0) in boxes or p3d(p.x, p.y, 1) in boxes:
                    ntpos.append(p + d[move])
                    if isv:
                        dx = 1 if p3d(p.x, p.y, 0) in boxes else -1
                        ntpos.append(p + p2d(dx, 0) + d[move])
                    mbox.add(p)

            if not ntpos:
                clear = True
                break
            tpos = ntpos

        if clear:
            abox = set()
            rbox = set()
            for p in mbox:
                dx = 0 if  p3d(p.x, p.y, 0) in boxes else -1
                rbox.add(p3d(p.x + dx, p.y, 0))
                rbox.add(p3d(p.x + 1 + dx, p.y, 1))
                n = p + d[move] 
                abox.add(p3d(n.x + dx, n.y, 0))
                abox.add(p3d(n.x + 1 + dx, n.y, 1))
            boxes.difference_update(rbox)
            boxes.update(abox)
            return npos  
        else:
            return pos
    else:
        return npos 


def score(walls, boxes, pos, moves):
    for move in moves:
        pos = update(pos, move, walls, boxes)
    return sum([box.x + 100 * box.y for box in boxes if type(box) is p2d or box.z == 0])


def pprint(size, walls, boxes, pos):
    for y in range(size.y):
        for x in range(size.x):
            if p2d(x, y) in walls:
                print('#', end='')
            elif p2d(x, y) in boxes:
                print('O', end='')
            elif p3d(x, y, 0) in boxes:
                print('[', end='')
            elif p3d(x, y, 1) in boxes:
                print(']', end='')
            elif p2d(x, y) == pos:
                print('@', end='')
            else:
                print('.', end='')
        print('')


def part1():
    walls, boxes, pos, moves, _ = parse_input(rows)
    print(score(walls, boxes, pos, moves))


def extend(walls, boxes, pos, moves, size):
    nwalls = set()
    for w in walls:
        nwalls.add(p2d(2 * w.x, w.y))
        nwalls.add(p2d(2 * w.x + 1, w.y))
    nboxes = set()
    for b in boxes:
        nboxes.add(p3d(2 * b.x, b.y, 0))
        nboxes.add(p3d(2 * b.x + 1, b.y, 1))
    pos = p2d(pos.x * 2, pos.y)
    size = p2d(size.x * 2, size.y)
    return nwalls, nboxes, pos, moves, size


def part2():
    walls, boxes, pos, moves, size = parse_input(rows)
    walls, boxes, pos, moves, _ = extend(walls, boxes, pos, moves, size)
    print(score(walls, boxes, pos, moves))


part1()
part2()