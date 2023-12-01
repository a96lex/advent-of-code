import sys


directions = {"R": [1, 0], "L": [-1, 0], "U": [0, 1], "D": [0, -1]}


def update_head_position(position, direction):
    delta_pos = directions[direction]
    new_pos = [a + b for a, b in zip(position, delta_pos)]
    return new_pos


def get_diff(pos_1, pos_2):
    difference = [a - b for a, b in zip(pos_1, pos_2)]
    return difference


def get_abs_distance(difference):
    return round((difference[0] ** 2 + difference[1] ** 2) ** (1 / 2), 1)


visited_sites = set()
H_pos = [0, 0]
T_pos = [0, 0]
for instruction in sys.stdin.readlines():
    direction, steps = instruction.replace("\n", "").split(" ")
    for _ in range(int(steps)):
        H_pos = update_head_position(H_pos, direction)

        difference = get_diff(H_pos, T_pos)
        abs_distance = get_abs_distance(difference)

        # Two steps away
        if abs_distance == 2.0:
            T_pos = [int(a + b / 2) for a, b in zip(T_pos, difference)]

        # Diagonal plus one
        if abs_distance == 2.2:
            T_pos = [int(a + b / abs(b)) for a, b in zip(T_pos, difference)]

        if abs_distance not in [0.0, 1.0, 2.0, 1.4, 2.2]:
            print("Wrong", abs_distance, H_pos, T_pos)

        visited_sites.add(tuple(T_pos))


print(len(list(visited_sites)))
