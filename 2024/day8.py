from collections import defaultdict
import math
from utils import site 

rows = site.download_input(day=8)

antennas = defaultdict(set)

for y in range(len(rows)):
    for x in range(len(rows[y])):
        if rows[y][x].isalnum():
            antennas[rows[y][x]].add((x, y))


def valid(pos):
    return pos[0] in range(len(rows[0])) and pos[1] in range(len(rows))


def find_antinodes(all=False):
    antinodes = set()
    for _, v in antennas.items():
        lv = list(v)
        for i, a1 in enumerate(lv):
            for a2 in lv[i + 1:]:
                dx, dy = a2[0] - a1[0], a2[1] - a1[1]
                if all:
                    gcd = math.gcd(dx, dy)
                    dx, dy = dx / gcd, dy / gcd
                    p = a1 
                    antinodes.add(a1)
                    while True:
                        p = (p[0] - dx, p[1] - dy)
                        if p == a2:
                            continue 
                        if not valid(p):
                            break 
                        antinodes.add(p)
                    p = a2
                    antinodes.add(a2)
                    while True:
                        p = (p[0] + dx, p[1] + dy)
                        if p == a2:
                            continue 
                        if not valid(p):
                            break 
                        antinodes.add(p)
                else:
                    p1 = a1[0] - dx, a1[1] - dy 
                    p2 = a2[0] + dx, a2[1] + dy 
                    
                    antinodes.add(p1)
                    antinodes.add(p2)
    return antinodes


def print_an(antinodes):
    for y in range(len(rows)):
        for x in range(len(rows[y])):
            if (x, y) in antinodes:
                print("#", end='')
            else:
                print(rows[y][x], end='')
        print('')


antinodes = find_antinodes()
antinodes_all = find_antinodes(all=True)
print_an(antinodes_all)
print(len(list(filter(valid, antinodes)))) # 289
print(len(list(filter(valid, antinodes_all))))
