import sys


def get_distance(s, b):
    return abs(b[0] - s[0]) + abs(b[1] - s[1])


sensors_and_distances = {}
beacons = set()
for line in sys.stdin.readlines():
    line = (
        line.replace("Sensor at x=", "")
        .replace(": closest beacon is at x=", ", ")
        .replace("y=", "")
    )
    # print(line.split())
    numbers = tuple(map(int, line.split(",")))
    sensor, beacon = numbers[:2], numbers[2:]
    sensors_and_distances[sensor] = get_distance(sensor, beacon)
    beacons.add(beacon)


# get maximum and minimum x so we know where to start looking:
min_x = min([x for (x, _) in sensors_and_distances.keys()])
max_x = max([x for (x, _) in sensors_and_distances.keys()])
max_distance = max([d for d in sensors_and_distances.values()])


y = 2000000
impossible_positions = 0
for x in range(min_x - max_distance, max_x + max_distance):
    if x % 10000 == 0:
        print(x, max_x + max_distance)
    for sensor in sensors_and_distances.keys():
        if (x, y) in beacons:
            break
        if get_distance(sensor, (x, y)) <= sensors_and_distances[sensor]:
            impossible_positions += 1
            break

print(impossible_positions)
