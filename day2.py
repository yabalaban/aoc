import utils 

inp = utils.download_input(day=2)

def is_safe(levels):
    incr = levels[1] > levels[0]
    for idx in range(1, len(levels)):
        if incr and 1 <= levels[idx] - levels[idx - 1] <= 3:
            continue 
        elif not incr and 1 <= levels[idx - 1] - levels[idx] <= 3:
            continue
        else:
            return False 
    return True

res1 = 0
for row in inp:
    items = row.split(" ")
    levels =  [int(item.strip()) for item in items]
    if is_safe(levels):
        res1 += 1
print(res1)

res2 = 0
for row in inp:
    items = row.split(" ")
    levels =  [int(item.strip()) for item in items]
    if is_safe(levels):
        res2 += 1 
    else: 
        for i in range(0, len(levels)): 
            if is_safe(levels[:i] + levels[i + 1:]):
                res2 += 1
                break 
print(res2)