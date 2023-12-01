from heapq import heappop, heappush


cubes = {}
aux_cubes = {}

# 0 -> reachable space
# 1 -> reachable cube
# 2 -> unreachable


def get_neighbours(cube: tuple) -> list:
    nbrs = []
    for i in range(-1, 2, 2):
        nbrs.append((cube[0] + i, cube[1], cube[2]))
    for j in range(-1, 2, 2):
        nbrs.append((cube[0], cube[1] + j, cube[2]))
    for k in range(-1, 2, 2):
        nbrs.append((cube[0], cube[1], cube[2] + k))
    return nbrs


# got the bounds manually
for i in range(-1, 23):
    for j in range(-1, 23):
        for k in range(-1, 23):
            cubes[(i, j, k)] = 0
            aux_cubes[(i, j, k)] = 2

for line in open(0).readlines():
    cubes[tuple(map(int, (line.strip("\n").split(","))))] = 1


seen_points = set()
starting_point = (0, 0, 0)
heap = [starting_point]

while heap:
    point = heappop(heap)
    if point in seen_points:
        continue
    seen_points.add(point)

    nbrs = get_neighbours(point)

    for nbr in nbrs:
        if nbr not in cubes.keys():
            continue
        if cubes[nbr] == 0:
            aux_cubes[nbr] = 0
            heappush(heap, nbr)
        elif cubes[nbr] == 1:
            aux_cubes[nbr] = 1


visible_faces = 0
for p, v in aux_cubes.items():
    if v in [0, 2]:
        continue

    for nbr in get_neighbours(p):
        if nbr not in aux_cubes.keys():
            continue
        if aux_cubes[nbr] == 0:
            visible_faces += 1

print(visible_faces)
