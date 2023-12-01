import sys


with open(sys.argv[1]) as f:
    data = list(
        map(
            lambda x: (x[0], int(x[1].strip("\n")) * 811589153),
            [a for a in enumerate(f.readlines())],
        )
    )

for a, b in data:
    if b == 0:
        zero_key = (a, b)


total_nums = len(data)
moved_nums = 0


new_positions = data.copy()
for _ in range(10):
    for groove in data:
        current_pos = new_positions.index(groove)

        new_pos = (current_pos + groove[1]) % (total_nums - 1)
        new_positions.remove(groove)
        new_positions = new_positions[:new_pos] + [groove] + new_positions[new_pos:]

pos_0 = new_positions.index(zero_key)

result = 0
for n in [1000, 2000, 3000]:
    result += new_positions[(n + pos_0) % total_nums][1]

print(result)
