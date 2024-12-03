import utils 

inp = utils.download_input(day=3)

res1 = 0
res2 = 0
do = True

def parse_number(inp, idx, stop=',', limit=3):
    number = '' 
    acc = 0
    while idx < len(inp) and inp[idx].isdigit():
        number += inp[idx]
        idx += 1
        acc += 1
        if acc == limit:
            break
    if idx < len(inp) and inp[idx] == stop:
        return int(number), idx + 1
    else:
        return None, idx
    

def parse_mul(inp, idx):
    if idx + 7 < len(inp) and inp[idx:idx+4] == "mul(":
        idx += 4 
        lhs, idx = parse_number(inp, idx, ',')
        if not lhs:
            return 0, idx
        rhs, idx = parse_number(inp, idx, ')')
        if not rhs:
            return 0, idx
        return lhs * rhs, idx 
    else:
        return 0, idx + 1
    

def parse_do(inp, idx):
    if inp[idx:idx+4] == "do()":
        return True, idx + 4
    else:
        return None, idx


def parse_dont(inp, idx):
    if inp[idx:idx+7] == "don't()":
        return False, idx + 7
    else:
        return None, idx


idx = 0
program = ' '.join([x.strip() for x in inp])
while idx < len(program):
    flag, idx = parse_do(program, idx)
    if flag is not None:
        do = flag 
        continue 
    flag, idx = parse_dont(program, idx)
    if flag is not None:
        do = flag
        continue 
    s, idx = parse_mul(program, idx)
    res1 += s
    if do:
        res2 += s

print(res1) 
print(res2) 
    