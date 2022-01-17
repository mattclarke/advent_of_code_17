with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# ne,ne,s,s
# """

puzzle_input = [x.strip() for x in PUZZLE_INPUT.strip().split(",")]

location = (0, 0)
max_steps = 0
distance = 0

def calc_steps(location):
    steps = 0
    while location != (0, 0):
        if location[0] < 0 and location[1] < 0:
            # SW
            steps += 1
            location = (location[0] + 1, location[1] + 1)
        elif location[0] < 0 and location[1] > 0:
            # NW
            steps += 1
            location = (location[0] + 1, location[1] - 1)
        elif location[0] > 0 and location[1] > 0:
            # NE
            steps += 1
            location = (location[0] - 1, location[1] - 1)
        elif location[0] > 0 and location[1] < 0:
            # SE
            steps += 1
            location = (location[0] - 1, location[1] + 1)
        elif location[1] < 0:
            # S
            steps += 1
            location = (location[0], location[1] + 2)
        elif location[1] > 0:
            # N
            steps += 1
            location = (location[0], location[1] - 2)
        elif location[0] != 0 and location[1] == 0:
            # when y = 0 => distance from origin = x
            return steps + location[0]
    return steps


for move in puzzle_input:
    if move == "n":
        location = (location[0], location[1] + 2)
    elif move == "ne":
        location = (location[0] + 1, location[1] + 1)
    elif move == "se":
        location = (location[0] + 1, location[1] - 1)
    elif move == "s":
        location = (location[0], location[1] - 2)
    elif move == "sw":
        location = (location[0] - 1, location[1] - 1)
    elif move == "nw":
        location = (location[0] - 1, location[1] + 1)
    else:
        assert False
    distance = calc_steps(location)
    max_steps = max(max_steps, distance)


# Part 1 = 796
print(f"answer = {distance}")

# Part 2 = 1585
print(f"answer = {max_steps}")
