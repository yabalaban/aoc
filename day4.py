import utils 

inp = utils.download_input(day=4)

letters = [row.strip() for row in inp]
patterns = [
    lambda l, x, y: x + 3 < len(l) and l[x][y] == 'X' and l[x + 1][y] == 'M' and l[x + 2][y] == 'A' and l[x + 3][y] == 'S', 
    lambda l, x, y: x + 3 < len(l) and l[x + 3][y] == 'X' and l[x + 2][y] == 'M' and l[x + 1][y] == 'A' and l[x][y] == 'S',  
    lambda l, x, y: y + 3 < len(l[x]) and l[x][y] == 'X' and l[x][y + 1] == 'M' and l[x][y + 2] == 'A' and l[x][y + 3] == 'S',   
    lambda l, x, y: y + 3 < len(l[x]) and l[x][y + 3] == 'X' and l[x][y + 2] == 'M' and l[x][y + 1] == 'A' and l[x][y] == 'S',   
    lambda l, x, y: x + 3 < len(l) and y + 3 < len(l[x]) and l[x][y] == 'X' and l[x + 1][y + 1] == 'M' and l[x + 2][y + 2] == 'A' and l[x + 3][y + 3] == 'S',   
    lambda l, x, y: x + 3 < len(l) and y + 3 < len(l[x]) and l[x + 3][y + 3] == 'X' and l[x + 2][y + 2] == 'M' and l[x + 1][y + 1] == 'A' and l[x][y] == 'S',
    lambda l, x, y: x + 3 < len(l) and y + 3 < len(l[x]) and l[x][y + 3] == 'X' and l[x + 1][y + 2] == 'M' and l[x + 2][y + 1] == 'A' and l[x + 3][y] == 'S',   
    lambda l, x, y: x + 3 < len(l) and y + 3 < len(l[x]) and l[x + 3][y] == 'X' and l[x + 2][y + 1] == 'M' and l[x + 1][y + 2] == 'A' and l[x][y + 3] == 'S',   
]

mas_patterns = [ 
    lambda l, x, y: x + 2 < len(l) and y + 2 < len(l[x]) and l[x][y] == 'M' and l[x + 1][y + 1] == 'A' and l[x + 2][y + 2] == 'S',
    lambda l, x, y: x + 2 < len(l) and y + 2 < len(l[x]) and l[x + 2][y + 2] == 'M' and l[x + 1][y + 1] == 'A' and l[x][y] == 'S',
    lambda l, x, y: x + 2 < len(l) and y + 2 < len(l[x]) and l[x][y + 2] == 'M' and l[x + 1][y + 1] == 'A' and l[x + 2][y] == 'S',
    lambda l, x, y: x + 2 < len(l) and y + 2 < len(l[x]) and l[x + 2][y] == 'M' and l[x + 1][y + 1] == 'A' and l[x][y + 2] == 'S',
]

# problem 1
res = 0
for i in range(len(letters)):
    for j in range(len(letters[i])):
        for pattern in patterns:
            if pattern(letters, i, j):
                res += 1
print(res)

# problem 2
res = 0
for i in range(len(letters)):
    for j in range(len(letters[i])):
        c = 0
        for pattern in mas_patterns:
            if pattern(letters, i, j):
                c += 1
        if c >= 2:
            res += 1
print(res)