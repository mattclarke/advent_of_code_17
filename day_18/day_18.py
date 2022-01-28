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

played = []


def snd(regs, x, played):
    played.clear()
    played.append(regs[x])


def set(regs, x, y):
    regs[x] = y


def add(regs, x, y):
    regs[x] += y


def mul(regs, x, y):
    regs[x] *= y


def mod(regs, x, y):
    regs[x] %= y


def rcv(regs, x, played):
    return played[~0]


def jgz(regs, sp, x, y):
    if regs[x] > 0:
        return sp + y, True
    return sp, False


sp = 0
registers = defaultdict(int)
answer = -1

while sp < len(puzzle_input):
    line = puzzle_input[sp]
    cmd, *args = line.split(" ")
    if len(args) == 2:
        if args[1].isdigit() or args[1].startswith("-"):
            args = (args[0], int(args[1]))
        else:
            args = (args[0], registers[args[1]])

    if cmd == "set":
        set(registers, args[0], args[1])
    elif cmd == "add":
        add(registers, args[0], args[1])
    elif cmd == "mul":
        mul(registers, args[0], args[1])
    elif cmd == "mod":
        mod(registers, args[0], args[1])
    elif cmd == "jgz":
        sp, jump = jgz(registers, sp, args[0], args[1])
        if jump:
            continue
    elif cmd == "snd":
        snd(registers, args[0], played)
    elif cmd == "rcv":
        if registers[args[0]] != 0:
            r = rcv(registers, args[0], played)
            if r is not None:
                answer = r
                break
    sp += 1


# Part 1 = 7071
print(f"answer = {answer}")
