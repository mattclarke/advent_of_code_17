from collections import defaultdict

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# snd 1
# snd 2
# snd p
# rcv a
# rcv b
# rcv c
# rcv d
# """

puzzle_input = [x.strip() for x in PUZZLE_INPUT.strip().split("\n")]


def convert_arg(regs, value):
    if value.isdigit() or value.startswith("-"):
        return int(value)
    else:
        return regs[value]


def set_reg(regs, x, y):
    regs[x] = y


def add(regs, x, y):
    regs[x] += y


def mul(regs, x, y):
    regs[x] *= y


def mod(regs, x, y):
    regs[x] %= y


def jgz(sp, x, y):
    if x > 0:
        return sp + y, True
    return sp, False


sp = 0
registers = defaultdict(int)
answer = -1
played = None

while sp < len(puzzle_input):
    cmd, *args = puzzle_input[sp].split(" ")
    if len(args) == 2:
        args = (args[0], convert_arg(registers, args[1]))

    if cmd == "set":
        set_reg(registers, args[0], args[1])
    elif cmd == "add":
        add(registers, args[0], args[1])
    elif cmd == "mul":
        mul(registers, args[0], args[1])
    elif cmd == "mod":
        mod(registers, args[0], args[1])
    elif cmd == "jgz":
        sp, jump = jgz(sp, convert_arg(registers, args[0]), args[1])
        if jump:
            continue
    elif cmd == "snd":
        played = registers[args[0]]
    elif cmd == "rcv":
        if registers[args[0]] != 0:
            if played is not None:
                answer = played
                break
    sp += 1


# Part 1 = 7071
print(f"answer = {answer}")


def run_until(registers, sp, write, read):
    while sp < len(puzzle_input):
        cmd, *args = puzzle_input[sp].split(" ")
        if len(args) == 2:
            args = (args[0], convert_arg(registers, args[1]))

        if cmd == "set":
            set_reg(registers, args[0], args[1])
        elif cmd == "add":
            add(registers, args[0], args[1])
        elif cmd == "mul":
            mul(registers, args[0], args[1])
        elif cmd == "mod":
            mod(registers, args[0], args[1])
        elif cmd == "jgz":
            sp, jump = jgz(sp, convert_arg(registers, args[0]), args[1])
            if jump:
                continue
        elif cmd == "snd":
            write.append(registers[args[0]])
        elif cmd == "rcv":
            if not read:
                return registers, sp, write, read
            v = read.pop(0)
            registers[args[0]] = v
        sp += 1
    assert False


registers_a = defaultdict(int)
registers_b = defaultdict(int)
registers_b["p"] = 1
queue_a = []
queue_b = []
sp_a = 0
sp_b = 0
is_a = True
ans = 0

a = (registers_a, sp_a, queue_a, queue_b)
b = (registers_b, sp_b, queue_b, queue_a)

while True:
    if is_a:
        a = run_until(*a)
        is_a = False
    else:
        b = run_until(*b)
        is_a = True
        ans += len(queue_b)

    if not queue_a and not queue_b:
        break


# Part 2 = 8001
print(f"answer = {ans}")
