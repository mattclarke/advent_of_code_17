from collections import defaultdict

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# b inc 5 if a > 1
# a inc 1 if b < 5
# c dec -10 if a >= 1
# c inc -20 if c == 10
# """

puzzle_input = [x.strip() for x in PUZZLE_INPUT.strip().split("\n")]

commands = []

for line in puzzle_input:
    reg, cmd, amount, _, a, cmp, b = line.split(" ")
    amount = int(amount)
    b = int(b)
    commands.append((reg, cmd, amount, a, cmp, b))

registers = defaultdict(int)

answer_2 = 0

for cmd in commands:
    reg, cmd, amount, a, cmp, b = cmd
    do_cmd = False
    if cmp == ">":
        if registers[a] > b:
            do_cmd = True
    elif cmp == ">=":
        if registers[a] >= b:
            do_cmd = True
    elif cmp == "<":
        if registers[a] < b:
            do_cmd = True
    elif cmp == "<=":
        if registers[a] <= b:
            do_cmd = True
    elif cmp == "==":
        if registers[a] == b:
            do_cmd = True
    elif cmp == "!=":
        if registers[a] != b:
            do_cmd = True
    else:
        assert False

    if do_cmd:
        if cmd == "inc":
            registers[reg] += amount
        else:
            registers[reg] -= amount
        answer_2 = max(answer_2, registers[reg])

answer = max(registers.values())

# Part 1 = 5849
print(f"answer = {answer}")

# Part 2 = 6702
print(f"answer = {answer_2}")
