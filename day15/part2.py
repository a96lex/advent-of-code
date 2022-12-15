import sys
from collections import defaultdict


def get_distance(s, b):
    return abs(b[0] - s[0]) + abs(b[1] - s[1])


MAX_BOUND = 4_000_000

sensors_and_distances = {}
boundary_points = defaultdict(lambda: 0)

beacons = set()
positions_to_check = set()

for line in sys.stdin.readlines():
    line = (
        line.replace("Sensor at x=", "")
        .replace(": closest beacon is at x=", ", ")
        .replace("y=", "")
    )

    numbers = tuple(map(int, line.split(",")))
    sensor, beacon = numbers[:2], numbers[2:]

    sensors_and_distances[sensor] = get_distance(sensor, beacon)
    beacons.add(beacon)

    # add one to check the closest not available positions
    distance = get_distance(sensor, beacon) + 1

    for i in range(distance):
        positions = [
            (sensor[0] + i, sensor[1] + (distance - i)),
            (sensor[0] - i, sensor[1] + (distance - i)),
            (sensor[0] + i, sensor[1] - (distance - i)),
            (sensor[0] - i, sensor[1] - (distance - i)),
        ]

        for position in positions:
            x, y = position
            if 0 > x or x > MAX_BOUND or 0 > y or y > MAX_BOUND:
                break

            boundary_points[position] += 1

            if boundary_points[position] == 4:
                positions_to_check.add(position)


def print_grid():
    for j in range(20):
        row = ""
        for i in range(20):
            if (i, j) in beacons:
                row += "B"
            elif (i, j) in sensors_and_distances.keys():
                row += "S"
            elif boundary_points.get((i, j), 0) > 3:
                row += "#"
            else:
                row += "."
            row += " "
        print(row, end="\n")


for (x, y) in positions_to_check:
    is_possible = True
    for sensor, distance in sensors_and_distances.items():
        if (x, y) in beacons:
            is_possible = False
            break
        if get_distance(sensor, (x, y)) <= distance:
            is_possible = False
            break
    if is_possible:
        print(x, y)
        print(x * 4000000 + y)
        exit()
