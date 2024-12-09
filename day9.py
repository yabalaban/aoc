from collections import defaultdict
import utils 

inp = utils.download_input(day=9)
rows = [row.strip() for row in inp]
rows = rows[0]
row = [int(d) for d in rows]


def move_blocks(state, whole=False):
    fs = defaultdict(dict)
    ridx = len(state) - 1 - int(len(state) % 2 == 0)
    rfid = ridx / 2
    moved = {}

    lidx, fid, pos = 0, 0, 0
    while lidx <= ridx:
        if lidx % 2 == 0: # file
            fs[lidx].update({fid: (pos, row[lidx])})
            if fid in moved:
                pos += moved[fid]
            fid += 1 
            pos += row[lidx]
        else: # free space 
            while row[lidx] > 0 and lidx < ridx:
                d = min(row[lidx], row[ridx])
                if whole:
                    if row[ridx] != d or row[ridx] == 0:
                        ridx -= 2 
                        rfid -= 1 
                        continue
                    else:
                        moved[rfid] = d
                row[lidx], row[ridx] = row[lidx] - d, row[ridx] - d
                fs[lidx].update({rfid: (pos, d)})
                pos += d
                if row[ridx] == 0:
                    ridx -= 2 
                    rfid -= 1 
            if whole:
                pos += row[lidx]
                ridx = len(state) - 1 - int(len(state) % 2 == 0)
                rfid = ridx / 2
        lidx += 1
    return fs


def checksum(fs):
    res = 0
    for _, v in fs.items():
        for fid, posd in v.items():
            pos, d = posd
            res += sum([fid * p for p in range(pos, pos + d)])
    return res  


fs1 = move_blocks(row)
res1 = checksum(fs1)
print(res1)
fs2 = move_blocks(row, whole=True)
res2 = checksum(fs2)
print(res2)