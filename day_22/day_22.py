import copy

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# ..#
# #..
# ...
# """

puzzle_input = [x.strip() for x in PUZZLE_INPUT.strip().split("\n")]

START_GRID = {}
for r, line in enumerate(puzzle_input):
    for c, ch in enumerate(line):
        if ch == "#":
            START_GRID[(r, c)] = "#"


def print_grid(grid, curr):
    for r in range(-10, 10):
        row = []
        for c in range(-10, 10):
            if (r, c) == curr:
                row.append("X")
            elif (r, c) in grid:
                row.append(grid[(r, c)])
            else:
                row.append(".")
        print("".join(row))
    print("\n")


grid = copy.deepcopy(START_GRID)
curr_pos = (len(puzzle_input) // 2, len(puzzle_input[0]) // 2)
heading = 0  # 0 = N, 1 = E, 2 = S, 3 = W
infections = 0

for _ in range(10_000):
    infected = False
    if curr_pos in grid:
        infected = True
        del grid[curr_pos]
    else:
        grid[curr_pos] = "#"
        infections += 1

    if infected:
        heading = (heading + 1) % 4
    else:
        heading = (heading - 1) % 4

    if heading == 0:
        curr_pos = (curr_pos[0] - 1, curr_pos[1])
    elif heading == 1:
        curr_pos = (curr_pos[0], curr_pos[1] + 1)
    elif heading == 2:
        curr_pos = (curr_pos[0] + 1, curr_pos[1])
    elif heading == 3:
        curr_pos = (curr_pos[0], curr_pos[1] - 1)

# Part 1 = 5352
print(f"answer = {infections}")

grid = copy.deepcopy(START_GRID)
curr_pos = (len(puzzle_input) // 2, len(puzzle_input[0]) // 2)
heading = 0  # 0 = N, 1 = E, 2 = S, 3 = W
infections = 0

for _ in range(10_000_000):
    state = grid[curr_pos] if curr_pos in grid else "."
    new_state = None
    if curr_pos in grid:
        if grid[curr_pos] == "W":
            new_state = "#"
            infections += 1
        elif grid[curr_pos] == "#":
            new_state = "F"
        elif grid[curr_pos] == "F":
            new_state = "."
    else:
        new_state = "W"
    if new_state == ".":
        del grid[curr_pos]
    else:
        grid[curr_pos] = new_state

    if state == ".":
        heading = (heading - 1) % 4
    elif state == "#":
        heading = (heading + 1) % 4
    elif state == "F":
        heading = (heading + 2) % 4

    if heading == 0:
        curr_pos = (curr_pos[0] - 1, curr_pos[1])
    elif heading == 1:
        curr_pos = (curr_pos[0], curr_pos[1] + 1)
    elif heading == 2:
        curr_pos = (curr_pos[0] + 1, curr_pos[1])
    elif heading == 3:
        curr_pos = (curr_pos[0], curr_pos[1] - 1)

# Part 2 = 2511475
print(f"answer = {infections}")
