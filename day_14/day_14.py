PUZZLE_INPUT = "wenycdww"


# From day 10
def as_knot_hash(input_data, length=256):
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


def as_bin(input_data):
    result = ""

    for c in input_data:
        result += f"{int(c, 16):0>4b}"
    return result


result = 0
grid = []

for i in range(128):
    data = PUZZLE_INPUT + "-" + str(i)
    data = as_knot_hash(data)
    data = as_bin(data)
    result += data.count("1")
    grid.append([s for s in data])

# Part 1 = 8226
print(f"answer = {result}")

seen = set()
count = 0

for r in range(128):
    for c in range(128):
        if (r, c) in seen:
            continue
        if grid[r][c] == "0":
            seen.add((r, c))
            continue
        count += 1

        queue = [(r, c)]
        while queue:
            qr, qc = queue.pop()
            if (qr, qc) in seen:
                continue
            seen.add((qr, qc))
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = qr + dr
                nc = qc + dc
                if nr < 0 or nr >= 128 or nc < 0 or nc >= 128:
                    continue
                if grid[nr][nc] == "1" and (nr, nc) not in seen:
                    queue.append((nr, nc))

# Part 2 = 1128
print(f"answer = {count}")
