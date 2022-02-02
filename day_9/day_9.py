with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

puzzle_input = [x.strip() for x in PUZZLE_INPUT.strip()]

in_garbage = False
negated = False
garbage_count = 0
score = 0
depth = 0

for ch in puzzle_input:
    if ch == "{" and not negated and not in_garbage:
        depth += 1
    elif ch == "}" and not negated and not in_garbage:
        score += depth
        depth -= 1
    elif ch == "<" and not negated and not in_garbage:
        in_garbage = True
    elif ch == ">" and not negated and in_garbage:
        in_garbage = False
    elif ch == "!":
        negated = not negated
        continue
    else:
        if in_garbage and not negated:
            garbage_count += 1
    if negated:
        negated = False

# Part 1 = 7616
print(f"answer = {score}")

# Part 2 = 3838
print(f"answer = {garbage_count}")
