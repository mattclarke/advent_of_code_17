with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# ne,ne,s,s
# """

puzzle_input = [x.strip() for x in PUZZLE_INPUT.strip().split(",")]

max_steps = 0
q = 0
r = 0

for move in puzzle_input:
    if move == "n":
        r -= 1
    elif move == "ne":
        r -= 1
        q += 1
    elif move == "se":
        q += 1
    elif move == "s":
        r += 1
    elif move == "sw":
        q -= 1
        r += 1
    elif move == "nw":
        q -= 1
    else:
        assert False
    max_steps = max(max_steps, max(abs(q), abs(r)))

# Part 1 = 796
print(f"answer = {max(abs(q), abs(r))}")

# Part 2 = 1585
print(f"answer = {max_steps}")
