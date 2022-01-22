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

while True:
    r, c = current
    if path[current] == "|":
        if direction == "s":
            current = (r + 1, c)
        elif direction == "n":
            current = (r - 1, c)
        elif direction == "e":
            current = (r, c + 1)
        elif direction == "w":
            current = (r, c - 1)
    elif path[current] == "-":
        if direction == "e":
            current = (r, c + 1)
        elif direction == "w":
            current = (r, c - 1)
        elif direction == "n":
            current = (r - 1, c)
        elif direction == "s":
            current = (r + 1, c)
    elif path[current] == "+":
        if direction == "n":
            if (r - 1, c) in path and (
                path[(r - 1, c)] == "|" or path[(r - 1, c)].isupper()
            ):
                current = (r - 1, c)
            elif (r, c + 1) in path and (
                path[(r, c + 1)] == "-" or path[(r, c + 1)].isupper()
            ):
                direction = "e"
                current = (r, c + 1)
            elif (r, c - 1) in path and (
                path[(r, c - 1)] == "-" or path[(r, c - 1)].isupper()
            ):
                direction = "w"
                current = (r, c - 1)
            else:
                assert False
        elif direction == "s":
            if (r + 1, c) in path and (
                path[(r + 1, c)] == "|" or path[(r + 1, c)].isupper()
            ):
                current = (r + 1, c)
            elif (r, c + 1) in path and (
                path[(r, c + 1)] == "-" or path[(r, c + 1)].isupper()
            ):
                direction = "e"
                current = (r, c + 1)
            elif (r, c - 1) in path and (
                path[(r, c - 1)] == "-" or path[(r, c - 1)].isupper()
            ):
                direction = "w"
                current = (r, c - 1)
            else:
                assert False
        elif direction == "e":
            if (r, c + 1) in path and (
                path[(r, c + 1)] == "|" or path[(r, c + 1)].isupper()
            ):
                current = (r, c + 1)
            elif (r - 1, c) in path and (
                path[(r - 1, c)] == "|" or path[(r - 1, c)].isupper()
            ):
                direction = "n"
                current = (r - 1, c)
            elif (r + 1, c) in path and (
                path[(r + 1, c)] == "|" or path[(r + 1, c)].isupper()
            ):
                direction = "s"
                current = (r + 1, c)
            else:
                assert False
        elif direction == "w":
            if (r, c - 1) in path and (
                path[(r, c - 1)] == "|" or path[(r, c - 1)].isupper()
            ):
                current = (r, c - 1)
            elif (r - 1, c) in path and (
                path[(r - 1, c)] == "|" or path[(r - 1, c)].isupper()
            ):
                direction = "n"
                current = (r - 1, c)
            elif (r + 1, c) in path and (
                path[(r + 1, c)] == "|" or path[(r + 1, c)].isupper()
            ):
                direction = "s"
                current = (r + 1, c)
            else:
                assert False
    elif path[current].isupper():
        letters.append(path[current])
        if direction == "n":
            current = (r - 1, c)
        elif direction == "s":
            current = (r + 1, c)
        elif direction == "e":
            current = (r, c + 1)
        elif direction == "w":
            current = (r, c - 1)
    if current not in path:
        break


# Part 1 = AYRPVMEGQ
print(f"answer = {''.join(letters)}")

# Part 2 = 133
# print(f"answer = {abs(position[0]) + abs(position[1])}")
