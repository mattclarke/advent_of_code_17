PUZZLE_INPUT = 376


class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None


HEAD = Node()
HEAD.next = HEAD
current = HEAD

for i in range(1, 2018):
    for j in range(PUZZLE_INPUT):
        current = current.next
    new_node = Node(i)
    new_node.next = current.next
    current.next = new_node
    current = new_node


# Part 1 = 777
print(f"answer = {current.next.value}")

buff_size = 1
first = 0
index = 0

for i in range(1, 50000001):
    index = (index + PUZZLE_INPUT) % buff_size
    if index == 0:
        first = i
    buff_size += 1
    index += 1


# Part 2 = 39289581
print(f"answer = {first}")
