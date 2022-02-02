from collections import defaultdict


def a(tape, slot):
    if tape[slot] == 0:
        tape[slot] = 1
        slot += 1
        return "b", slot
    else:
        tape[slot] = 0
        slot -= 1
        return "c", slot


def b(tape, slot):
    if tape[slot] == 0:
        tape[slot] = 1
        slot -= 1
        return "a", slot
    else:
        tape[slot] = 1
        slot -= 1
        return "d", slot


def c(tape, slot):
    if tape[slot] == 0:
        tape[slot] = 1
        slot += 1
        return "d", slot
    else:
        tape[slot] = 0
        slot += 1
        return "c", slot


def d(tape, slot):
    if tape[slot] == 0:
        tape[slot] = 0
        slot -= 1
        return "b", slot
    else:
        tape[slot] = 0
        slot += 1
        return "e", slot


def e(tape, slot):
    if tape[slot] == 0:
        tape[slot] = 1
        slot += 1
        return "c", slot
    else:
        tape[slot] = 1
        slot -= 1
        return "f", slot


def f(tape, slot):
    if tape[slot] == 0:
        tape[slot] = 1
        slot -= 1
        return "e", slot
    else:
        tape[slot] = 1
        slot += 1
        return "a", slot


FUNCS = {
    "a": a,
    "b": b,
    "c": c,
    "d": d,
    "e": e,
    "f": f,
}
TAPE = defaultdict(int)
NUM_STEPS = 12172063

curr_func = "a"
slot = 0

for _ in range(NUM_STEPS):
    curr_func, slot = FUNCS[curr_func](TAPE, slot)

# Part 1 = 2474
print(f"answer = {sum(list(TAPE.values()))}")
