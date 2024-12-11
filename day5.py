from collections import defaultdict
import utils 

rows = utils.download_input(day=5)

sep = rows.index("")
rrules, rupdates = rows[:sep], rows[sep + 1:]


def parse_reversed_rules(rows):
    rules = defaultdict(set)
    for row in rows: 
        pages = row.split("|")
        rules[pages[1]].add(pages[0])
    return rules


def filter_updates(updates, correct=True):
    filtered = []
    for update in updates:
        pages = update.split(",")
        bag = set(pages)
        valid = True 
        for page in pages:
            bag.remove(page)
            if rules[page].intersection(bag):
                valid = False 
                break 
        if valid and correct:
            filtered.append(pages)
        elif not valid and not correct:
            filtered.append(pages)
    return filtered

rules = parse_reversed_rules(rrules)

res1 = 0 
correct_updates = filter_updates(rupdates)
for pages in correct_updates:
    res1 += int(pages[len(pages) // 2])
print(res1)


res2 = 0 
incorrect_updates = filter_updates(rupdates, correct=False)
for pages in incorrect_updates:
    bag = set(pages)
    fixed = [] 
    while bag: 
        remove = False
        for page in bag:
            r = rules[page]
            if not r:
                fixed.append(page)
                remove = True
                break
            elif not bag.intersection(r): 
                fixed.append(page)
                remove = True 
                break 
        if remove: 
            bag.remove(fixed[-1])
    res2 += int(fixed[len(fixed) // 2])
print(res2)
