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

# Part 2 = 133
# print(f"answer = {abs(position[0]) + abs(position[1])}")
