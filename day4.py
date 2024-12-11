import itertools as it

import utils 

letters = utils.download_input(day=4)

def line_patterns(s):
    return [
        lambda l, x, y: x + len(s) - 1 < len(l) and all([l[x + i][y] == c for i, c in enumerate(s)]),
        lambda l, x, y: x + len(s) - 1 < len(l) and all([l[x + len(s) - i - 1][y] == c for i, c in enumerate(s)]),
        lambda l, x, y: y + len(s) - 1 < len(l) and all([l[x][y + i] == c for i, c in enumerate(s)]),
        lambda l, x, y: y + len(s) - 1 < len(l) and all([l[x][y + len(s) - i - 1] == c for i, c in enumerate(s)]),
    ]


def diag_patterns(s):
    return [
        lambda l, x, y: x + len(s) - 1 < len(l) and y + len(s) - 1 < len(l[x]) and all([l[x + i][y + i] == c for i, c in enumerate(s)]),   
        lambda l, x, y: x + len(s) - 1 < len(l) and y + len(s) - 1 < len(l[x]) and all([l[x + len(s) - i - 1][y + len(s) - i - 1] == c for i, c in enumerate(s)]),   
        lambda l, x, y: x + len(s) - 1 < len(l) and y + len(s) - 1 < len(l[x]) and all([l[x + i][y + len(s) - i - 1] == c for i, c in enumerate(s)]),   
        lambda l, x, y: x + len(s) - 1 < len(l) and y + len(s) - 1 < len(l[x]) and all([l[x + len(s) - i - 1][y + i] == c for i, c in enumerate(s)]), 
    ]


def count(input, x, y, patterns):
    return sum([int(pattern(input, x, y)) for pattern in patterns])


xlen = len(letters)
ylen = len(letters[0])

# problem 1
res = 0
patterns = line_patterns("XMAS") + diag_patterns("XMAS")
for x, y in it.product(range(xlen), range(ylen)):
    res += count(letters, x, y, patterns)
print(res)

# problem 2
res = 0
patterns = diag_patterns("MAS")
for x, y in it.product(range(xlen), range(ylen)):
    if count(letters, x, y, patterns) >= 2:
        res += 1
print(res)
