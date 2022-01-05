with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# """

puzzle_input = [
    [int(y.strip()) for y in x.split("\t")] for x in PUZZLE_INPUT.strip().split("\n")
]

answer = sum([max(row) - min(row) for row in puzzle_input])

# Part 1 = 53978
print(f"answer = {answer}")

answer = 0

for row in puzzle_input:
    for i, a in enumerate(row):
        for b in row[i + 1 :]:
            if max(a, b) % min(a, b) == 0:
                answer += max(a, b) // min(a, b)
                break

# Part 2 = 314
print(f"answer = {answer}")
