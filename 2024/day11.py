from collections import defaultdict 
from utils import site 

rows = site.download_input(day=11)
row = rows[0].split()
pebbles = defaultdict(int)
for pebble in row:
    pebbles[pebble] += 1

rules = [
    lambda x: (True, ['1']) if x == '0' else (False, [x]), 
    lambda x: (True, [x[:len(x) // 2], str(int(x[len(x) // 2:]))]) if len(x) % 2 == 0 else (False, [x]),
    lambda x: (True, [str(int(x) * 2024)]), 
]

def blink(pebbles):
    res = defaultdict(int)
    for pebble, c in pebbles.items():
        for rule in rules:
            applied, m = rule(pebble)
            if applied:
                for p in m:
                    res[p] += c
                break
    return res 


def solve(pebbles, times):
    for i in range(times):
        pebbles = blink(pebbles)
    return pebbles

res1 = sum(solve(pebbles, 25).values())
print(res1)
res2 = sum(solve(pebbles, 75).values())
print(res2)
