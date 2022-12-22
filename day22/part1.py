import sys

positions = {}
instructions = []
for j, line in enumerate(sys.stdin.readlines()):
    if line[0] in [" ", ".", "#"]:
        for i, char in enumerate(line.replace("\n", "")):
            if char != " ":
                positions[(i, j)] = char
    elif line == "\n":
        continue
    else:
        instructions = line.replace("R", " R ").replace("L", " L ").split(" ")

directions_clockwise = [(1, 0), (0, 1), (-1, 0), (0, -1)]
direction_drawings = [">", "v", "<", "^"]
dir_changes = {"R": 1, "L": -1}


def update_direction(current_direction_index: tuple, change: str) -> tuple:
    return (current_direction_index + dir_changes[change]) % 4


def update_position(current_pos: tuple, direction_index: int) -> tuple:
    return (
        current_pos[0] + directions_clockwise[direction_index][0],
        current_pos[1] + directions_clockwise[direction_index][1],
    )


def wrap_position(current_pos: tuple, direction_index: int):
    direction = directions_clockwise[direction_index]

    if direction[0] == 0:  # we are moving up/down
        column = [(a, b) for a, b in positions.keys() if a == current_pos[0]]
        new_pos = max(column, key=lambda x: -1 * x[1] * direction[1])
    else:  # we are moving left/right
        row = [(a, b) for a, b in positions.keys() if b == current_pos[1]]
        new_pos = max(row, key=lambda x: -1 * x[0] * direction[0])

    return new_pos


def print_grid():
    for j in range(max(positions.keys(), key=lambda x: x[1])[1]):
        row = ""
        for i in range(max(positions.keys(), key=lambda x: x[0])[0]):
            row += positions.get((i, j), " ")
        print(row, end="\n")


direction_index = 0  # start by going right

# get first position
current_position = min(positions.keys(), key=lambda x: x[1])

for instruction in instructions:
    if instruction in ["R", "L"]:
        direction_index = update_direction(direction_index, instruction)
        continue
    else:
        steps = int(instruction)
        for step in range(steps):
            candidate_position = update_position(current_position, direction_index)
            map_obj = positions.get(candidate_position)

            if map_obj is None:
                candidate_position = wrap_position(current_position, direction_index)

            map_obj = positions.get(candidate_position)
            if map_obj == "#":
                break
            else:
                positions[current_position] = direction_drawings[direction_index]
                current_position = candidate_position

score = (
    1000 * (current_position[1] + 1) + 4 * (current_position[0] + 1) + direction_index
)
print(score)
