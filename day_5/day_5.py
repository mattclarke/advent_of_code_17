with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

puzzle_input = [int(x.strip()) for x in PUZZLE_INPUT.strip().split("\n")]

index = 0
count = 0
instructions = list(puzzle_input)

while 0 <= index < len(instructions):
    step = instructions[index]
    instructions[index] += 1
    index += step
    count += 1

# Part 1 = 343467
print(f"answer = {count}")

index = 0
count = 0
instructions = list(puzzle_input)

while 0 <= index < len(instructions):
    step = instructions[index]
    if step >= 3:
        instructions[index] -= 1
    else:
        instructions[index] += 1
    index += step
    count += 1

# Part 2 = 24774780
print(f"answer = {count}")
