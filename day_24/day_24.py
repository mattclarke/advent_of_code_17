from collections import defaultdict

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# 0/2
# 2/2
# 2/3
# 3/4
# 3/5
# 0/1
# 10/1
# 9/10
# """

puzzle_input = [x.strip() for x in PUZZLE_INPUT.strip().split("\n")]

# Check all connections are unique
assert len(set(puzzle_input)) == len(puzzle_input)


CONNECTIONS = defaultdict(list)

for line in puzzle_input:
    a, b = line.split("/")
    CONNECTIONS[int(a)].append(int(b))
    CONNECTIONS[int(b)].append(int(a))

max_len = 0
strength = 0


def solve(connections):
    def _recurse(curr, seen):
        global max_len, strength
        best = 0
        for con in connections[curr]:
            if (curr, con) not in seen and (con, curr) not in seen:
                new_seen = set(seen)
                new_seen.add((curr, con))
                best = max(best, curr + con + _recurse(con, new_seen))
                curr_strength = sum((s[0] + s[1] for s in new_seen))
                if len(new_seen) > max_len:
                    max_len = len(new_seen)
                    strength = curr_strength
                elif len(new_seen) == max_len and curr_strength > strength:
                    strength = curr_strength
        return best

    best = 0
    for con in connections[0]:
        ans = con + _recurse(con, {(0, con)})
        best = max(best, ans)
    return best


# Part 1 = 1940
print(f"answer = {solve(CONNECTIONS)}")

# Part 2 = 1928
print(f"answer = {strength}")
