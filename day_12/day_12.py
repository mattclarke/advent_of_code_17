from collections import defaultdict

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# 0 <-> 2
# 1 <-> 1
# 2 <-> 0, 3, 4
# 3 <-> 2, 4
# 4 <-> 2, 3, 6
# 5 <-> 6
# 6 <-> 4, 5
# """

puzzle_input = [x.strip() for x in PUZZLE_INPUT.strip().split("\n")]

nodes = defaultdict(set)

for line in puzzle_input:
    node, rest = line.split(" <-> ")
    joins = rest.split(", ")
    for j in joins:
        nodes[node].add(j)
    for n in joins:
        nodes[n].add(node)


def find_connected(start):
    joined = set()
    queue = [start]
    while queue:
        front = queue.pop(0)
        if front in joined:
            continue

        joined.add(front)
        queue.extend(list(nodes[front]))
    return joined


joined = find_connected("0")

# Part 1 = 169
print(f"answer = {len(joined)}")

num_groups = 1
for n in nodes:
    if n in joined:
        continue
    joined.update(find_connected(n))
    num_groups += 1

# Part 2 = 179
print(f"answer = {num_groups}")
