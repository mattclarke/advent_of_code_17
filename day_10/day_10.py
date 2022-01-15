with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

LENGTH = 256

puzzle_input = [int(x.strip()) for x in PUZZLE_INPUT.strip().split(",")]
print(puzzle_input)

data = [x for x in range(LENGTH)]
skip_size = 0
index = 0

for i in puzzle_input:
    selected = []
    for j in range(i):
        selected.append(data[(index + j) % LENGTH])
    selected.reverse()
    for j in range(i):
        data[(index + j) % LENGTH] = selected[j]
    index += i + skip_size
    index %= LENGTH
    skip_size += 1

# Part 1 = 20056
print(f"answer = {data[0] * data[1]}")


def solve(input_data, length=LENGTH):
    puzzle_input = [ord(x) for x in input_data]
    puzzle_input.extend([17, 31, 73, 47, 23])

    data = [x for x in range(length)]
    skip_size = 0
    index = 0

    for _ in range(64):
        for i in puzzle_input:
            selected = []
            for j in range(i):
                selected.append(data[(index + j) % length])
            selected.reverse()
            for j in range(i):
                data[(index + j) % length] = selected[j]
            index += i + skip_size
            index %= length
            skip_size += 1

    index = 0
    dense = []

    while index < len(data):
        x = data[index]

        for i in range(1, 16):
            x ^= data[index + i]
        as_hex = hex(x)[2:]
        if len(as_hex) == 1:
            as_hex = f"0{as_hex}"
        dense.append(as_hex)
        index += 16

    return "".join(dense)


assert solve("") == "a2582a3a0e66e6e86e3812dcb672a272"
assert solve("AoC 2017") == "33efeb34ea91902bb2f59c9920caa6cd"
assert solve("1,2,3") == "3efbe78a8d82f29979031a4aa0b16a9d"
assert solve("1,2,4") == "63960835bcdc130f0b66d7ff4f6a5a8e"

answer = solve(PUZZLE_INPUT.strip())
assert len(answer) == 32

# Part 2 = d9a7de4a809c56bf3a9465cb84392c8e
print(f"answer = {answer}")
