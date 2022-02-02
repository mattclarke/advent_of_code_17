import copy

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>
# p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
# p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>
# p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>
# """

puzzle_input = [x.strip() for x in PUZZLE_INPUT.strip().split("\n")]


class Particle:
    def __init__(self, pos, vel, acc):
        self.pos = pos
        self.vel = vel
        self.acc = acc

    def __repr__(self):
        return f"{self.pos} | {self.vel} | {self.acc}"


PARTICLES = {}

for i, line in enumerate(puzzle_input):
    line = (
        line.replace("p=<", "")
        .replace(", v=<", "|")
        .replace(", a=<", "|")
        .replace(">", "")
    )
    p, v, a = line.split("|")
    pos = []
    for c in p.split(","):
        pos.append(int(c.strip()))
    vel = []
    for c in v.split(","):
        vel.append(int(c.strip()))
    acc = []
    for c in a.split(","):
        acc.append(int(c.strip()))
    PARTICLES[i] = Particle(pos, vel, acc)

slow_particles = {}
min_acc = 10000000000

for k, v in PARTICLES.items():
    acc = abs(v.acc[0]) + abs(v.acc[1]) + abs(v.acc[2])
    if acc < min_acc:
        slow_particles.clear()
        slow_particles[k] = v
        min_acc = acc
    elif acc == min_acc:
        slow_particles[k] = v

# If there were more than one with the same acc then we take into account
# starting velocity and position

# Part 1 = 150
print(f"answer = {list(slow_particles.keys())[0]}")


def update_particle(p):
    particle = copy.deepcopy(p)
    particle.vel[0] += particle.acc[0]
    particle.vel[1] += particle.acc[1]
    particle.vel[2] += particle.acc[2]
    particle.pos[0] += particle.vel[0]
    particle.pos[1] += particle.vel[1]
    particle.pos[2] += particle.vel[2]
    return particle


particles = copy.deepcopy(PARTICLES)
num_particles = len(particles)

while True:
    new_particles = {}
    reverse_lookup = {}
    collisions = set()
    for k, v in particles.items():
        p = update_particle(v)
        pos = tuple(p.pos)
        if pos in collisions:
            continue
        elif pos in reverse_lookup:
            collisions.add(pos)
            d = reverse_lookup[pos]
            del new_particles[d]
            del reverse_lookup[pos]
        else:
            reverse_lookup[pos] = k
            new_particles[k] = p
    particles = new_particles
    if len(particles) < num_particles:
        num_particles = len(particles)
        print(num_particles)

# Part 2 = 657
