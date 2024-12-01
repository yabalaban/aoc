with open("input/day1.txt") as f:
    inp = f.readlines()

ls, rs = [], [] 
for item in inp:
    items = item.split('   ')
    l = int(items[0])
    r = int(items[1].strip())
    ls.append(l)
    rs.append(r)
ls.sort()
rs.sort() 

acc = 0
for i in range(len(ls)):
    acc += abs(ls[i] - rs[i])
print(acc)

rsm = {} 
for r in rs:
    rsm[r] = rsm.get(r, 0) + 1

acc2 = 0 
for l in ls:
    acc2 += (l * rsm.get(l, 0))
print(acc2)