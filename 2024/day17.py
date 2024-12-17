import math

from dataclasses import dataclass 
from utils import site 

rows = site.download_input(day=17)


@dataclass 
class CPU: 
    a: int
    b: int 
    c: int 


@dataclass 
class State: 
    cpu: CPU 
    ip: int 
    program: list[int]
    output: list[int]

    def advance(self, combo=False):
        n = self.program[self.ip]
        self.ip += 1 
        if not combo:
            return n 
        else:
            if n == 7:
                assert False, "not valid combo operand"
            elif n == 4:
                return self.cpu.a 
            elif n == 5:
                return self.cpu.b 
            elif n == 6:
                return self.cpu.c 
            else:
                return n 
    
    def halted(self):
        return self.ip >= len(self.program)


def adv(state):
    state.cpu.a = math.trunc(state.cpu.a / (2 ** state.advance(combo=True)))


def bxl(state):
    state.cpu.b = state.cpu.b ^ state.advance()


def bst(state):
    state.cpu.b = state.advance(combo=True) % 8


def jnz(state):
    jmp = state.advance()
    if state.cpu.a == 0:
        return 
    state.ip = jmp


def bxc(state):
    _ = state.advance()
    state.cpu.b = state.cpu.b ^ state.cpu.c


def out(state):
    state.output.append(state.advance(combo=True) % 8)


def bdv(state):
    state.cpu.b = math.trunc(state.cpu.a / (2 ** state.advance(combo=True)))


def cdv(state):
    state.cpu.c = math.trunc(state.cpu.a / (2 ** state.advance(combo=True)))


opcode = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc, 
    5: out, 
    6: bdv,
    7: cdv, 
}

regb = int(rows[1][len('Register B: '):]),
regc = int(rows[2][len('Register C: '):]),
cpu = CPU(
    int(rows[0][len('Register A: '):]),
    regb,
    regc,
)
state = State(
    cpu, 
    ip=0,
    program=[int(i) for i in rows[4][len("Program: "):].split(',')],
    output=[]
)

def eval(state, haltcond=None): 
    while True:
        if state.halted():
            return 0
        if haltcond and haltcond(state):
            return 1
        inst = state.advance() 
        opcode[inst](state)

eval(state)
print(','.join([str(x) for x in state.output]))


def recover_reg_a():
    rega = 0
    l = 0
    while True: 
        state.cpu = CPU(rega, regb, regc) 
        state.ip = 0 
        state.output = []

        status = eval(state, haltcond=lambda state: state.program[-len(state.output):] == state.output and len(state.output) > l)
        if status == 1:
            if state.program == state.output:
                return rega
            l = len(state.output)
            rega <<= 3
        else:
            rega += 1


print(recover_reg_a())
# 239976271