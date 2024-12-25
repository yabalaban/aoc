from utils import site 

rows = site.download_input(day=25)

locks = set() 
keys = set() 

completed = True 
is_lock = True 
state = []
height = 0
for row in rows:
    if row == '':
        if is_lock:
            locks.add(tuple(state))
        else:
            keys.add(tuple(state))
        completed = True 
        continue

    if completed:
        is_lock = set([ch for ch in row]) == set(['#'])
        state = [0] * len(row)
        completed = False
        height = 0
    for i, ch in enumerate(row):
        if ch == "#":
            state[i] += 1  
    height += 1
if is_lock:
    locks.add(tuple(state))
else:
    keys.add(tuple(state))

res = 0 
for lock in locks:
    for key in keys: 
        if all([sum(x) <= height for x in zip(lock, key)]):
            res += 1 
print(res)
