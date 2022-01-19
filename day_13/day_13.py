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
    layer, rnge = line.split(": ")
    INPUT[int(layer)] = int(rnge)
    num_layers = max(num_layers, int(layer))

tick = 0
severity = 0

for x in range(num_layers+1):
    if tick in INPUT:
        rnge = INPUT[tick]
        # TODO: should be able to do this with maths!
        current = 0
        inc = True
        for i in range(tick):
            if inc and current < rnge-1:
                current += 1
                if current == rnge -1:
                    inc = False
                    continue
            if not inc and current > 0:
                current -= 1
                if current == 0:
                    inc = True
        if current == 0:
            severity += tick * rnge
    tick += 1


# Part 1 = 3184
print(f"answer = {severity}")

delay = 0
while True:
    position = 0
    tick = delay
    clean = True

    for x in range(num_layers+1):
        if position in INPUT:
            rnge = INPUT[position]
            # TODO: should be able to do this with maths!
            current = 0
            inc = True
            for i in range(tick):
                if inc and current < rnge-1:
                    current += 1
                    if current == rnge -1:
                        inc = False
                        continue
                if not inc and current > 0:
                    current -= 1
                    if current == 0:
                        inc = True
            if current == 0:
                clean = False
                break
        tick += 1
        position += 1
    if clean:
        break
    delay += 1

# Part 2 = 133
print(f"answer = {delay}")
