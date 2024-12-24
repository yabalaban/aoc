from copy import copy
from dataclasses import dataclass
from typing import Callable
from utils import site 

rows = site.download_input(day=24)
wires = {}

@dataclass
class Wire:
    name: str
    op_name: str
    op: Callable
    inputs: list[Callable]

    def __call__(self):
        return self.op(*[w() for w in self.inputs])

    def __repr__(self) -> str:
        return f"{self.name}[{self.__call__()}]={self.op_name}({', '.join([repr(w()) for w in self.inputs])})"


def op_const(state):
    return lambda: state


def op_wire(in1):
    return lambda: wires[in1]


def reset(x, y):
    xs = set()
    ys = set()
    for wire in wires:
        if wire.startswith("x"):
            xs.add(wire)
        if wire.startswith("y"):
            ys.add(wire)
    for wire in sorted(xs):
        wires[wire] = Wire(wire, "const", op_const(bool(x % 2)), [])
        x = x >> 1
    for wire in sorted(ys):
        wires[wire] = Wire(wire, "const", op_const(bool(y % 2)), [])
        y = y >> 1


def eval():
    zwires = set()
    for wire in wires:
        if wire.startswith("z"):
            zwires.add(wire)

    res = 0
    for zwire in reversed(sorted(zwires)):
        res += int(wires[zwire]())
        res <<= 1
    res >>= 1
    return res


def sanity_check():
    wx = []
    wy = []
    for i in range(45):
        reset(1 << i, 0)
        if 1 << i != eval():
            wx.append(i)
        reset(0, 1 << i)
        if 1 << i != eval():
            wy.append(i)
    assert not wx, wx
    assert not wy, wy


processed = []
split = rows.index("")
for swire in rows[:split]:
    items = swire.split(": ")
    wire, state = val = copy(items[0]), copy(bool(int(items[1])))
    processed.append([wire, "const", [state]])
for wire in rows[split + 1 :]:
    items = wire.split(" ")
    in1, op, in2, out = items[0], items[1], items[2], items[4]
    processed.append([out, op, [in1, in2]])


for wire, op, rest in processed:
    if op == "const":
        wires[wire] = Wire(wire, "const", op_const(rest[0]), [])
    else:
        lmbd = lambda x, y: x() and y()
        if op == "OR":
            lmbd = lambda x, y: x() or y()
        elif op == "XOR":
            lmbd = lambda x, y: x() ^ y()
        wires[wire] = Wire(wire, op, lmbd, [op_wire(rest[0]), op_wire(rest[1])])


# part1
print(eval())


# part2
z17 = wires["z17"]
wires["z17"] = wires["cmv"]
wires["cmv"] = z17
z23 = wires["z23"]
wires["z23"] = wires["rmj"]
wires["rmj"] = z23
z30 = wires["z30"]
wires["z30"] = wires["rdg"]
wires["rdg"] = z30
mwp = wires["mwp"]
wires["mwp"] = wires["btb"]
wires["btb"] = mwp

swaps = ["z17", "cmv", "z23", "rmj", "z30", "rdg", "mwp", "btb"]
sanity_check()
print(",".join(sorted(swaps)))