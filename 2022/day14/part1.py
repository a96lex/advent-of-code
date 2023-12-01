import sys
import math
from time import sleep

DRAW_OUTPUT = True

grid = {}

for line in sys.stdin.readlines():
    trajectories = [
        tuple(map(int, t.split(","))) for t in line.replace("\n", "").split(" -> ")
    ]

    pointer = trajectories[0]
    grid[pointer] = "#"
    for trajectory in trajectories:

        if pointer[0] != trajectory[0]:
            for i in range(
                pointer[0],
                trajectory[0],
                int(math.copysign(1, trajectory[0] - pointer[0])),
            ):
                grid[(i, pointer[1])] = "#"

        if pointer[1] != trajectory[1]:
            for i in range(
                pointer[1],
                trajectory[1],
                int(math.copysign(1, trajectory[1] - pointer[1])),
            ):
                grid[(pointer[0], i)] = "#"

        pointer = trajectory
        grid[pointer] = "#"


max_i = max([a for (a, _), b in grid.items() if b == "#"])
min_i = min([a for (a, _), b in grid.items() if b == "#"])
max_j = max([a for (_, a), b in grid.items() if b == "#"])
min_j = min([a for (_, a), b in grid.items() if b == "#"])

min_j = min(min_j, 0)

bounds = max_i, min_i, max_j, min_j


def print_grid(current):
    print("\n\n")
    for j in range(min_j, max_j + 1):
        row = ""
        for i in range(min_i, max_i + 1):
            if (i, j) == current:
                row += "x"
            else:
                row += grid.get((i, j), ".")
        print(row, end="\n")


START = (500, 0)
count = 0
while True:
    new_particle = START
    while True:
        # particle falls forever
        if new_particle[1] > max_j:
            print(count)
            exit()

        if DRAW_OUTPUT:
            sleep(0.01)
            print_grid(new_particle)

        # attempt down
        new_pos = (new_particle[0], new_particle[1] + 1)
        if not grid.get(new_pos):
            new_particle = new_pos
            continue

        # attempt left
        new_pos = (new_particle[0] - 1, new_particle[1] + 1)
        if not grid.get(new_pos):
            new_particle = new_pos
            continue

        # attempt right
        new_pos = (new_particle[0] + 1, new_particle[1] + 1)
        if not grid.get(new_pos):
            new_particle = new_pos
            continue
        else:
            # if we get here, particle is blocked
            grid[new_particle] = "o"
            new_particle = START
            count += 1
            if DRAW_OUTPUT:
                print_grid(new_particle)

            break
