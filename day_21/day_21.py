import copy
import math

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

puzzle_input = [x.strip() for x in PUZZLE_INPUT.strip().split("\n")]

rule_lookup = {}

for line in puzzle_input:
    rules = set()
    pattern, output = line.split(" => ")
    for_rot = pattern.split("/")
    for rot in range(0, 4):
        rules.add("/".join(for_rot))
        # Flip vertically
        flipped = [x for x in reversed(for_rot)]
        rules.add("/".join(flipped))
        # Flip horizontally
        flipped = ["".join([y for y in reversed(x)]) for x in for_rot]
        rules.add("/".join(flipped))
        # Rotate
        for_rot = [
            "".join([x[y] for x in reversed(for_rot)]) for y in range(len(for_rot))
        ]
    for rule in rules:
        if rule in rule_lookup:
            # have assumed rules are unique
            assert False
        rule_lookup[rule] = output


start_pattern = ".#./..#/###"
current = copy.copy(start_pattern)
answer_1 = 0

for it in range(18):
    if it == 5:
        answer_1 = current.count("#")

    pattern = current.split("/")
    if len(pattern) % 2 == 0:
        size = 2
    elif len(pattern) % 3 == 0:
        size = 3
    else:
        assert False
    squares = []
    for n in range(len(pattern) // size):
        for m in range(len(pattern) // size):
            sq = []
            for r in range(size):
                row = []
                for c in range(size):
                    row.append(pattern[(n * size) + r][(m * size) + c])
                sq.append("".join(row))
            squares.append("/".join(sq))
    new_squares = []
    for sq in squares:
        if sq not in rule_lookup:
            assert False
        new_squares.append(rule_lookup[sq])
    if len(new_squares) == 1:
        current = new_squares[0]
    else:
        length = int(math.sqrt(len(new_squares)))
        size = len(new_squares[0].split("/"))
        temp = []
        for n in range(length):
            for m in range(size):
                row = []
                start = n * length
                for sq in new_squares[start : start + length]:
                    pattern = sq.split("/")
                    row.append(pattern[m])
                temp.append("".join(row))
        current = "/".join(temp)

# Part 1 = 133
print(f"answer = {answer_1}")

# Part 2 = 2221990
print(f"answer = {current.count('#')}")
