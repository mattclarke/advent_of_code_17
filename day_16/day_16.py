with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

puzzle_input = [x.strip() for x in PUZZLE_INPUT.strip().split(",")]

original = [chr(97 + i) for i in range(16)]
data = list(original)


def run_once(data):
    for line in puzzle_input:
        if line.startswith("s"):
            # Spin => move x numbers from the end to the front
            offset = len(data) - int(line[1:])
            front = data[offset:]
            back = data[0:offset]
            data = front + back
        elif line.startswith("x"):
            # Exchange => swap to indices
            a, b = [int(x) for x in line[1:].split("/")]
            data[a], data[b] = data[b], data[a]
        elif line.startswith("p"):
            # Partner => swap two letters
            a, b = [x for x in line[1:].split("/")]
            a = data.index(a)
            b = data.index(b)
            data[a], data[b] = data[b], data[a]
    return data


# Part 1 = lgpkniodmjacfbeh
print(f"answer = {''.join(run_once(data))}")

data = list(original)
repeat_interval = 0
while True:
    data = run_once(data)
    repeat_interval += 1
    if data == original:
        break

data = list(original)
for i in range(1_000_000_000 % repeat_interval):
    data = run_once(data)

# Part 2 = hklecbpnjigoafmd
print(f"answer = {''.join(data)}")
