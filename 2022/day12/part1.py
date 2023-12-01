from heapq import heappop, heappush

heights = "abcdefghijklmnopqrstuvwxyz"

with open("input.dat", "r") as f:
    data = [list(l.replace("\n", "")) for l in f.readlines()]

w = len(data[0])
h = len(data)


for y in range(h):
    for x in range(w):
        if data[y][x] == "E":
            E_pos = y, x
        if data[y][x] == "S":
            S_pos = y, x


def get_height(char):
    if char == "S":
        return 0
    if char == "E":
        return 25
    return heights.index(char)


def get_neighbours(y, x):
    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nbr_y = y + dy
        nbr_x = x + dx

        if not (0 <= nbr_y < h and 0 <= nbr_x < w):
            continue

        if get_height(data[nbr_y][nbr_x]) <= get_height(data[y][x]) + 1:
            yield nbr_y, nbr_x


visited_points = [[False] * w for _ in range(h)]
heap = [(0, S_pos[0], S_pos[1])]

while True:
    steps, pos_y, pos_x = heappop(heap)

    if visited_points[pos_y][pos_x]:
        continue

    visited_points[pos_y][pos_x] = True

    if (pos_y, pos_x) == E_pos:
        print(steps)
        break

    for new_y, new_x in get_neighbours(pos_y, pos_x):
        heappush(heap, (steps + 1, new_y, new_x))
