with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# 12131415
# """

puzzle_input = [int(x) for x in PUZZLE_INPUT.strip()]
# print(puzzle_input)

prev = None
answer = 0

for i in puzzle_input:
    if prev is None:
        prev = i
        continue
    if i == prev:
        answer += i
    prev = i

if prev == puzzle_input[0]:
    answer += prev


# Part 1 = 997
print(f"answer = {answer}")

prev = None
answer = 0

for i in range(len(puzzle_input)):
    halfway = (i + len(puzzle_input) // 2) % len(puzzle_input)
    if puzzle_input[i] == puzzle_input[halfway]:
        answer += puzzle_input[i]

# Part 2 = 1358
print(f"answer = {answer}")
