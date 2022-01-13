with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# pbga (66)
# xhth (57)
# ebii (61)
# havc (66)
# ktlj (57)
# fwft (72) -> ktlj, cntj, xhth
# qoyq (66)
# padx (45) -> pbga, havc, qoyq
# tknk (41) -> ugml, padx, fwft
# jptl (61)
# ugml (68) -> gyxo, ebii, jptl
# gyxo (61)
# cntj (57)
# """

puzzle_input = [x.strip() for x in PUZZLE_INPUT.strip().split("\n")]
# print(puzzle_input)

nodes = {}

for line in puzzle_input:
    subnodes = []
    if "->" in line:
        line, second = line.split(" -> ")
        subnodes = second.split(", ")
    line = line.replace("(", "").replace(")", "")
    name, weight = line.split(" ")
    nodes[name] = (subnodes, int(weight))

# Find root
candidates = set(nodes.keys())

for n, v in nodes.items():
    for c in v[0]:
        if c in candidates:
            candidates.remove(c)

assert len(candidates) == 1
root_name = candidates.pop()

# Part 1 = hmvwl
print(f"answer = {root_name}")


def solve(root_name):
    def _recurse(name):
        node = nodes[name]
        names = node[0]
        weight = node[1]
        weights = [_recurse(n) for n in names]
        if weights and len(set(weights)) != 1:
            wrong_weight = -1
            correct_weight = -1
            wrong_node = None
            for u in set(weights):
                if weights.count(u) == 1:
                    wrong_node = nodes[names[weights.index(u)]]
                    wrong_weight = u
                else:
                    correct_weight = u
            diff = abs(wrong_weight - correct_weight)
            if correct_weight > wrong_weight:
                print(f"answer = {wrong_node[1]+diff}")
            else:
                print(f"answer = {wrong_node[1]-diff}")
            raise RuntimeError("done")
        return weight + sum(weights)

    try:
        _recurse(root_name)
    except:
        pass


# Part 2 = 1853
solve(root_name)
