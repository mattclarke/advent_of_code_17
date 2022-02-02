a = 591
b = 393

count_1 = 0
a_list = []  # For part 2
b_list = []  # For part 2

for i in range(40_000_000):
    a *= 16807
    b *= 48271
    a %= 2147483647
    b %= 2147483647
    a_16 = a & 0b1111111111111111
    b_16 = b & 0b1111111111111111

    if a_16 == b_16:
        count_1 += 1
    # For part 2
    if a % 4 == 0 and len(a_list) < 5_000_000:
        a_list.append(a_16)
    if b % 8 == 0 and len(b_list) < 5_000_000:
        b_list.append(b_16)

# Part 1 = 619
print(f"answer = {count_1}")

count_2 = 0
i = 0
while i < len(a_list) and i < len(b_list):
    if a_list[i] == b_list[i]:
        count_2 += 1
    i += 1

# Part 2 = 290
print(f"answer = {count_2}")
