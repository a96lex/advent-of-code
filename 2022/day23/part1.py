import sys


prefered_moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
elf_positions = set()

for j, line in enumerate(sys.stdin.readlines()):
    position_array = list(line.strip("\n"))
    for i, c in enumerate(position_array):
        if c == "#":
            elf_positions.add((i, j))


def print_grid():
    min_h = min([y for x, y in elf_positions] + [0])
    max_h = max([y for x, y in elf_positions] + [5])
    min_w = min([x for x, y in elf_positions] + [0])
    max_w = max([x for x, y in elf_positions] + [5])

    for j in range(min_h, max_h + 1):
        row = ""
        for i in range(min_w, max_w + 1):
            if (i, j) in elf_positions:
                row += "#"
            else:
                row += "."
        print(row, end="\n")


def get_neighbours_by_drection(direction, position):
    if direction[0] == 0:
        return [(a + position[0], direction[1] + position[1]) for a in range(-1, 2)]
    else:
        return [(direction[0] + position[0], b + position[1]) for b in range(-1, 2)]


def get_all_neigbours(position):
    return [
        (position[0] + a, position[1] + b)
        for a, b in [
            (1, -1),
            (1, 0),
            (1, 1),
            (0, -1),
            (0, 1),
            (-1, -1),
            (-1, 0),
            (-1, 1),
        ]
    ]


def update_position(direction, position):
    return (direction[0] + position[0], direction[1] + position[1])


debug = False
for turn in range(10):

    proposed_positions = set()
    blocked_positions = set()
    elf_updates = {}

    for elf in elf_positions:
        eight_nbr = get_all_neigbours(elf)

        if not any([n in elf_positions for n in eight_nbr]):
            continue

        for move in range(4):
            direction = prefered_moves[(turn + move) % 4]
            neighbours = get_neighbours_by_drection(direction, elf)
            if any([n in elf_positions for n in neighbours]):
                continue
            else:
                proposed_position = update_position(direction, elf)
                elf_updates[elf] = proposed_position
                if proposed_position in proposed_positions:
                    blocked_positions.add(proposed_position)
                proposed_positions.add(proposed_position)
                break

    for elf, new_pos in elf_updates.items():
        if new_pos in blocked_positions:
            continue
        elf_positions.remove(elf)
        elf_positions.add(new_pos)

min_h = min([y for x, y in elf_positions])
max_h = max([y for x, y in elf_positions])
min_w = min([x for x, y in elf_positions])
max_w = max([x for x, y in elf_positions])


height = max_h - min_h + 1
width = max_w - min_w + 1


total_space = height * width - len(elf_positions)

print(total_space)
