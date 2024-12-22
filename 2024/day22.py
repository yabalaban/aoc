from collections import defaultdict
from utils import site 

rows = site.download_input(day=22)


def next_secret(secret):
    r1 = secret * 64
    r2 = secret ^ r1
    secret = r2 % 16777216 

    r4 = secret // 32 
    r5 = secret ^ r4
    secret = r5 % 16777216 

    r6 = secret * 2048
    r7 = secret ^ r6
    secret = r7 % 16777216 

    return secret


def next_n_secret(secret, n=2000):
    for _ in range(n):
        secret = next_secret(secret)
    return secret


def change(secret, n=2000):
    delta = [(secret % 10, 0)]
    for _ in range(n):
        secret = next_secret(secret)
        delta.append((secret % 10, secret % 10 - delta[-1][0]))
    return delta[1:]


def offer(delta):
    book = defaultdict(int)
    for i, d in enumerate(delta[3:]):
        k = (delta[i][1], delta[i + 1][1], delta[i + 2][1], delta[i + 3][1])
        if k in book:
            continue 
        book[k] = d[0]
    return book


deltas = [change(int(r)) for r in rows]
books = [offer(delta) for delta in deltas]
total = set() 
for book in books:
    total = total.union(list(book.keys()))
    
max = 0
for seq in total:
    smax = sum([book[seq] for book in books])
    if smax > max:
        max = smax
print('max', max)
