with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

puzzle_input = [x.strip() for x in PUZZLE_INPUT.strip().split("\n")]


def convert_arg(regs, value):
    if value.isdigit() or value.startswith("-"):
        return int(value)
    else:
        return regs[value]


def set_reg(regs, x, y):
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
        cmd, *args = puzzle_input[sp].split(" ")
        if len(args) == 2:
            args = (args[0], convert_arg(registers, args[1]))

        if cmd == "set":
            set_reg(registers, args[0], args[1])
        elif cmd == "sub":
            sub(registers, args[0], args[1])
        elif cmd == "mul":
            mul(registers, args[0], args[1])
            num_mul += 1
        elif cmd == "jnz":
            sp, jump = jnz(sp, convert_arg(registers, args[0]), args[1])
            if jump:
                continue
        sp += 1

    return num_mul


registers = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0}

# Part 1 = 6724
print(f"answer = {run_code(registers)}")

# Part 2 = 903
