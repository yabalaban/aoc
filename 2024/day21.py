from collections import defaultdict
from utils import site 

# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+

numeric_keypad_layout = {
    '7': (2, 3),    '8': (1, 3),    '9': (0, 3),
    '4': (2, 2),    '5': (1, 2),    '6': (0, 2),
    '1': (2, 1),    '2': (1, 1),    '3': (0, 1),
                    '0': (1, 0),    'A': (0, 0),
}


def numeric_to_directional_keypad(start, end):
    sp = numeric_keypad_layout[start]
    ep = numeric_keypad_layout[end]
    dx, dy = ep[0] - sp[0], ep[1] - sp[1]

    if sp[1] == 0 and ep[0] == 2:
        return abs(dy) * ('^' if dy >= 0 else 'v') + abs(dx) * ('<' if dx > 0 else '>') + 'A'
    elif sp[0] == 2 and ep[1] == 0:
        return abs(dx) * ('<' if dx > 0 else '>') + abs(dy) * ('^' if dy >= 0 else 'v') + 'A'
    elif dx >= 0:
        return abs(dx) * ('<' if dx > 0 else '>') + abs(dy) * ('^' if dy >= 0 else 'v') + 'A'
    else:
        return abs(dy) * ('^' if dy >= 0 else 'v') + abs(dx) * ('<' if dx > 0 else '>') + 'A'

#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+

directional_keypad_layout = {
                    '^': (1, 0),    'A': (0, 0), 
    '<': (2, -1),   'v': (1, -1),   '>': (0, -1),
}


def directional_to_directional_keypad(start, end):
    sp = directional_keypad_layout[start]
    ep = directional_keypad_layout[end]
    dx, dy = ep[0] - sp[0], ep[1] - sp[1]
    if ep[0] == 2:
        return abs(dy) * ('^' if dy >= 0 else 'v') + abs(dx) * ('<' if dx > 0 else '>') + 'A'
    elif sp[0] == 2:
        return abs(dx) * ('<' if dx > 0 else '>') + abs(dy) * ('^' if dy >= 0 else 'v') + 'A'
    elif dx >= 0:
        return abs(dx) * ('<' if dx > 0 else '>') + abs(dy) * ('^' if dy >= 0 else 'v') + 'A'
    else:
        return abs(dy) * ('^' if dy >= 0 else 'v') + abs(dx) * ('<' if dx > 0 else '>') + 'A'



rows = site.download_input(day=21)
test_rows = [
"029A",
"980A",
"179A",
"456A",
"379A",
]

def sequence(code, d = 2):
    pas = ''.join([numeric_to_directional_keypad(s, e) for (s, e) in zip('A' + code, code)])
    for i in range(d):
        pas = ''.join([directional_to_directional_keypad(s, e) for (s, e) in zip('A' + pas, pas)])
    return pas


def sequence_opt(code, d=2):
    pas = ''.join([numeric_to_directional_keypad(s, e) for (s, e) in zip('A' + code, code)])

    state = defaultdict(int)
    for (s, e) in zip('A' + pas, pas):
        state[f"{s}{e}"] += 1

    for _ in range(d):
        nstate = defaultdict(int)
        for k, v in state.items(): 
            seq = directional_to_directional_keypad(k[0], k[1])
            for (s, e) in zip('A' + seq, seq):
                nstate[f"{s}{e}"] += v
        state = nstate 

    return sum(state.values())


def complexity(code, d=2):
    seq = sequence(code, d)
    return int(code[:-1]) * len(seq)


def complexity_opt(code, d=2):
    seqlen = sequence_opt(code, d)
    return int(code[:-1]) * seqlen


print([68 * 29, 60 * 980, 68 * 179, 64 * 456, 64 * 379], sum([68 * 29, 60 * 980, 68 * 179, 64 * 456, 64 * 379]))
print([complexity(code) for code in test_rows], sum([complexity(code) for code in test_rows]))
print([complexity_opt(code) for code in test_rows], sum([complexity_opt(code) for code in test_rows]))


print(sum([complexity_opt(code) for code in rows]))
print(sum([complexity_opt(code, 25) for code in rows]))
