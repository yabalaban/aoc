from utils import site 


rows = site.download_input(day=1, year=2015)

floor = 0
fbasement = None
rule = { '(': 1, ")": -1 }
for idx, ch in enumerate(rows[0]):
    floor += rule[ch]
    if floor == -1 and not fbasement:
        fbasement = idx + 1
print(floor)
print(fbasement)