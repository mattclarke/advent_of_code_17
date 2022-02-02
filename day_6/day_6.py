with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

puzzle_input = [int(x.strip()) for x in PUZZLE_INPUT.strip().split("\t")]

data = tuple(puzzle_input)
seen = set()
count = 0


while data not in seen:
    seen.add(data)
    new_data = list(data)
    index = -1
    value = -1
    for i, v in enumerate(new_data):
        if v > value:
            index = i
            value = v
    new_data[index] = 0
    index = (index + 1) % len(new_data)
    while value > 0:
        new_data[index] += 1
        index = (index + 1) % len(new_data)
        value -= 1
    data = tuple(new_data)
    count += 1

# Part 1 = 6681
print(f"answer = {count}")

data = tuple(puzzle_input)
seen = set()
count = 0
target = None

while True:
    if data == target:
        break
    if data in seen and not target:
        target = data
        count = 0
    seen.add(data)
    new_data = list(data)
    index = -1
    value = -1
    for i, v in enumerate(new_data):
        if v > value:
            index = i
            value = v
    new_data[index] = 0
    index = (index + 1) % len(new_data)
    while value > 0:
        new_data[index] += 1
        index = (index + 1) % len(new_data)
        value -= 1
    data = tuple(new_data)
    count += 1

# Part 2 = 2392
print(f"answer = {count}")
