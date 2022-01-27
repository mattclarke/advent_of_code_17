with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

puzzle_input = [x.strip() for x in PUZZLE_INPUT.strip().split("\n")]


def sets(regs, x, y):
    regs[x] = y


def sub(regs, x, y):
    regs[x] -= y


def mul(regs, x, y):
    regs[x] *= y


def jnz(sp, x, y):
    if x != 0:
        return sp + y, True
    return sp, False


def run_code(registers):
    sp = 0
    num_mul = 0

    while sp < len(puzzle_input):
        line = puzzle_input[sp]
        cmd, *args = line.split(" ")
        if len(args) == 2:
            if args[1].isdigit() or args[1].startswith("-"):
                args = (args[0], int(args[1]))
            else:
                args = (args[0], registers[args[1]])

        if cmd == "set":
            sets(registers, args[0], args[1])
        elif cmd == "sub":
            sub(registers, args[0], args[1])
        elif cmd == "mul":
            mul(registers, args[0], args[1])
            num_mul += 1
        elif cmd == "jnz":
            arg0 = registers[args[0]] if args[0] in registers else int(args[0])
            sp, jump = jnz(sp, arg0, args[1])
            if jump:
                continue
        sp += 1

    return num_mul


registers = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0}

# Part 1 = 6724
print(f"answer = {run_code(registers)}")

# Part 2 = 903
