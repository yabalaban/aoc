import sympy as sp 

from utils import site 

rows = site.download_input(day=13)


games = [] 

for i in range(0, len(rows), 4):
    button_a = [int(x[1:]) for x in rows[i].split(": ")[1].split(", ")]
    button_b = [int(x[1:]) for x in rows[i + 1].split(": ")[1].split(", ")]
    goal = tuple([int(x[2:]) for x in rows[i + 2].split(": ")[1].split(", ")])
    games.append((button_a, button_b, goal))


def solve_overkill(game, extra=0):
    t_0, x, y = sp.symbols("t_0, x, y", integer=True)
    a, b, goal = game
    eqx = a[0] * x + b[0] * y - goal[0] - extra 
    solx = sp.diophantine(eqx, syms=[x, y])
    if not solx:
        return (0, 0)

    [xt, yt] = solx.pop()
    eqy = a[1] * x + b[1] * y - goal[1] - extra
    eq = eqy.subs({x: xt, y: yt})
    sol = sp.diophantine(eq)
    if not sol:
        return (0, 0)

    t = sol.pop()[0]
    return xt.subs({t_0: t}), yt.subs({t_0: t}) 


states1 = [solve_overkill(game) for game in games]
print(sum([3 * s[0] + s[1] for s in states1]))

states2 = [solve_overkill(game, 10000000000000) for game in games]
print(sum([3 * s[0] + s[1] for s in states2]))
