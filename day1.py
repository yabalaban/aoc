import utils 

inp = utils.download_input(day=1)

ls, rs = [], [] 
for row in inp:
    items = row.split()
    l = int(items[0])
    r = int(items[1])
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