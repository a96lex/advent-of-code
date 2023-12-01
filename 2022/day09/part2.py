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


KNOTS = 10
visited_sites = set()
positions = [[0, 0] for _ in range(KNOTS)]

for instruction in sys.stdin.readlines():
    direction, steps = instruction.replace("\n", "").split(" ")
    for _ in range(int(steps)):
        positions[0] = update_head_position(positions[0], direction)

        for knot in range(1, KNOTS):
            difference = get_diff(positions[knot - 1], positions[knot])
            abs_distance = get_abs_distance(difference)

            # Two steps away
            if abs_distance == 2.0:
                positions[knot] = [
                    int(a + b / 2) for a, b in zip(positions[knot], difference)
                ]

            # Diagonal plus one, double diagonal or double diagonal plus one
            if abs_distance in [2.2, 2.8, 3.2]:
                positions[knot] = [
                    int(a + b / abs(b)) for a, b in zip(positions[knot], difference)
                ]

            if abs_distance not in [0.0, 1.0, 2.0, 1.4, 2.2, 2.8, 3.2]:
                print("Wrong", abs_distance, positions[knot], positions[knot - 1])

        visited_sites.add(tuple(positions[-1]))

print(len(list(visited_sites)))
