cubes = set()


def get_neighbours(cube: tuple) -> list:
    nbrs = []
    for i in range(-1, 2, 2):
        nbrs.append((cube[0] + i, cube[1], cube[2]))
    for j in range(-1, 2, 2):
        nbrs.append((cube[0], cube[1] + j, cube[2]))
    for k in range(-1, 2, 2):
        nbrs.append((cube[0], cube[1], cube[2] + k))
    return nbrs


for line in open(0).readlines():
    cubes.add(tuple(map(int, (line.strip("\n").split(",")))))

visible_faces = 0
for cube in cubes:
    for face in get_neighbours(cube):
        if face not in cubes:
            visible_faces += 1

print(visible_faces)
