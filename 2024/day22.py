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
    return delta[1:], secret


gbook = defaultdict(int)
def goffer(delta):
    book = set()
    for d0, d1, d2, d3 in zip(delta, delta[1:], delta[2:], delta[3:]):
        k = (d0[1], d1[1], d2[1], d3[1])
        if k in book:
            continue 
        gbook[k] += d3[0]
        book.add(k)
    return book


deltas = [change(int(r)) for r in rows]
[goffer(delta[0]) for delta in deltas]
print(sum([delta[1] for delta in deltas]))
print(max(gbook.values()))
