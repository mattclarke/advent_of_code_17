PUZZLE_INPUT = 289326


def solve(puzzle_input):
    if puzzle_input == 1:
        return 0

    i = 1
    ring = 0

    # Basically it is finding the Manhattan distance using polar coordinates
    # Find the "ring" where the puzzle input is, i.e. r
    while i * i < puzzle_input:
        ring += 1
        i += 2

    lowest_value = (i - 2) * (i - 2)
    # "Rotate" the puzzle so theta is < 90
    offset = (puzzle_input - lowest_value) % (i - 1)
    # Calculate distance from that to the x-axis
    y = abs(offset - i // 2)

    # Because using Manhattan distances, x = r = ring
    return ring + y


assert solve(1) == 0
assert solve(2) == 1
assert solve(3) == 2
assert solve(4) == 1
assert solve(5) == 2
assert solve(6) == 1
assert solve(7) == 2
assert solve(8) == 1
assert solve(9) == 2
assert solve(10) == 3
assert solve(11) == 2
assert solve(12) == 3
assert solve(23) == 2
assert solve(1024) == 31

# Part 1 = 419
print(f"answer = {solve(PUZZLE_INPUT)}")

grid = {(0, 0): 1}
pos = (0, 0)
# East = 0, North = 1, etc.
direction = 0
value = 1

while value <= PUZZLE_INPUT:
    if direction == 0:
        pos = (pos[0] + 1, pos[1])
    elif direction == 1:
        pos = (pos[0], pos[1] + 1)
    elif direction == 2:
        pos = (pos[0] - 1, pos[1])
    elif direction == 3:
        pos = (pos[0], pos[1] - 1)
    else:
        assert False

    value = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            dpos = (pos[0] + dx, pos[1] + dy)
            value += grid.get(dpos, 0)
    grid[pos] = value

    if direction == 0:
        if (pos[0], pos[1] + 1) not in grid:
            direction = 1
    elif direction == 1:
        if (pos[0] - 1, pos[1]) not in grid:
            direction = 2
    elif direction == 2:
        if (pos[0], pos[1] - 1) not in grid:
            direction = 3
    elif direction == 3:
        if (pos[0] + 1, pos[1]) not in grid:
            direction = 0
    else:
        assert False

# Part 2 = 295229
print(f"answer = {value}")
