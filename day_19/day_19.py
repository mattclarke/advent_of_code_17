with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """     |
#      |  +--+
#      A  |  C
#  F---|----E|--+
#      |  |  |  D
#      +B-+  +--+ """

puzzle_input = [x for x in PUZZLE_INPUT.split("\n")]

path = {}
start = None

for r, line in enumerate(puzzle_input):
    for c, ch in enumerate(line):
        if ch != " ":
            path[(r, c)] = ch
            if r == 0:
                start = (r, c)

current = start
direction = "s"
letters = []
num_steps = 1


def go(direction, r, c):
    if direction == "s":
        return r + 1, c
    elif direction == "n":
        return r - 1, c
    elif direction == "e":
        return r, c + 1
    elif direction == "w":
        return r, c - 1


def handle_junction(direction, r, c):
    straight = go(direction, r, c)
    if direction == "n" or direction == "s":
        okay = "|"
        option = "-"
        possible = [("e", (0, 1)), ("w", (0, -1))]
    else:
        okay = "-"
        option = "|"
        possible = [("s", (1, 0)), ("n", (-1, 0))]
    if straight in path and (path[straight] == okay or path[straight].isupper()):
        return direction
    else:
        for d, p in possible:
            nr, nc = r + p[0], c + p[1]
            if (nr, nc) in path and (
                path[(nr, nc)] == option or path[(nr, nc)].isupper()
            ):
                return d
    assert False


while True:
    r, c = current
    if path[current] == "|" or path[current] == "-" or path[current].isupper():
        if path[current].isupper():
            letters.append(path[current])
        current = go(direction, r, c)
    elif path[current] == "+":
        direction = handle_junction(direction, r, c)
        current = go(direction, r, c)
    if current not in path:
        break
    num_steps += 1


# Part 1 = AYRPVMEGQ
print(f"answer = {''.join(letters)}")

# Part 2 = 16408
print(f"answer = {num_steps}")
