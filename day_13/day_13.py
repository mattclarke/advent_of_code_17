with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# 0: 3
# 1: 2
# 4: 4
# 6: 4
# """

puzzle_input = [x.strip() for x in PUZZLE_INPUT.strip().split("\n")]

INPUT = {}

num_layers = 0

for line in puzzle_input:
    layer, depth = line.split(": ")
    INPUT[int(layer)] = int(depth)
    num_layers = max(num_layers, int(layer))

tick = 0
severity = 0

for x in range(num_layers + 1):
    if tick in INPUT:
        depth = INPUT[tick]
        current = tick % (depth * 2 - 2)
        if current >= depth:
            current -= depth - 1
            current = depth - current
        if current == 0:
            severity += tick * depth
    tick += 1


# Part 1 = 3184
print(f"answer = {severity}")

delay = 0
while True:
    position = 0
    tick = delay
    clean = True

    for x in range(num_layers + 1):
        if position in INPUT:
            depth = INPUT[position]
            current = tick % (depth * 2 - 2)
            if current >= depth:
                current -= depth - 1
                current = depth - current
            if current == 0:
                clean = False
                break
        tick += 1
        position += 1
    if clean:
        break
    delay += 1

# Part 2 = 3878062
print(f"answer = {delay}")
