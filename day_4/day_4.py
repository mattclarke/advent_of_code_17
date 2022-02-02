with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

puzzle_input = [x.strip() for x in PUZZLE_INPUT.strip().split("\n")]

num_valid = 0

for line in puzzle_input:
    parts = line.split(" ")
    seen = set(parts)
    if len(seen) == len(parts):
        num_valid += 1

# Part 1 = 477
print(f"answer = {num_valid}")

num_valid = 0

for line in puzzle_input:
    parts = line.split(" ")
    parts = ["".join(sorted(p)) for p in parts]
    seen = set(parts)
    if len(seen) == len(parts):
        num_valid += 1

# Part 2 = 167
print(f"answer = {num_valid}")
