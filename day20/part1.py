import sys


with open(sys.argv[1]) as f:
    data = list(
        map(
            lambda x: (x[0], int(x[1].strip("\n"))),
            [a for a in enumerate(f.readlines())],
        )
    )

total_nums = len(data)
moved_nums = 0


new_positions = data.copy()

for groove in data:
    current_pos = new_positions.index(groove)

    new_pos = (current_pos + groove[1]) % (total_nums - 1)
    new_positions.remove(groove)
    new_positions = new_positions[:new_pos] + [groove[1]] + new_positions[new_pos:]

pos_0 = new_positions.index(0)

result = 0
for n in [1000, 2000, 3000]:
    result += new_positions[(n + pos_0) % total_nums]

print(result)
