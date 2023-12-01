import sys
from time import sleep


positions = {}
instructions = []
area_size = 0

filename = sys.argv[1]
test_file = filename == "test.dat"

if test_file:
    import os

    os.system("cls||clear")

with open(filename) as f:
    for j, line in enumerate(f.readlines()):
        if area_size == 0:
            if test_file:
                area_size = len(line.replace("\n", "").replace(" ", ""))
            else:
                area_size = int(len(line.replace("\n", "").replace(" ", "")) / 2)
        if line[0] in [" ", ".", "#"]:
            for i, char in enumerate(line.replace("\n", "")):
                if char != " ":
                    positions[(i, j)] = char
        elif line == "\n":
            continue
        else:
            instructions = line.replace("R", " R ").replace("L", " L ").split(" ")

directions_clockwise = [(1, 0), (0, 1), (-1, 0), (0, -1)]
directions_named = ["right", "bottom", "left", "top"]
direction_drawings = [">", "v", "<", "^"]
dir_changes = {"R": 1, "L": -1}

if test_file:
    # fmt: off
    area_transitions = {
        "a": {"left": ("c", "top", -1), "top": ("b", "top", 2), "right": ("f", "left", 2)},
        "b": {"left": ("f", "bottom", 1), "top": ("a", "top", 2), "bottom": ("e", "bottom", 2),},
        "c": {"top": ("a", "left", 1), "bottom": ("e", "left", -1)},
        "d": {"right": ("f", "top", 1)},
        "e": {"left": ("a", "bottom", -1), "bottom": ("b", "bottom", 2)},
        "f": {"top": ("d", "left", -1), "right": ("a", "right", 2), "bottom": ("b", "left", 1),},
    }
    # fmt: on

    area_by_grid_index = {
        (2, 0): "a",
        (0, 1): "b",
        (1, 1): "c",
        (2, 1): "d",
        (2, 2): "e",
        (3, 2): "f",
    }

else:
    # fmt: off
    area_transitions = {
        "a": {"left": ("d", "left", 2), "top": ("f", "left", 1)},
        "b": {"top": ("f", "bottom", 0), "right": ("e", "right", 2), "bottom": ("c", "right", 1),},
        "c": {"right": ("b", "bottom", -1), "left": ("d", "top", -1)},
        "d": {"left": ("a", "left", 2),"top": ("c", "left", 1)},
        "e": {"right": ("b", "right", 2), "bottom": ("f", "right", 1)},
        "f": {"right": ("e", "bottom", -1), "bottom": ("b", "top", 0), "left": ("a", "top", -1),},
    }
    # fmt: on

    area_by_grid_index = {
        (1, 0): "a",
        (2, 0): "b",
        (1, 1): "c",
        (0, 2): "d",
        (1, 2): "e",
        (0, 3): "f",
    }


grid_index_by_area = {v: k for k, v in area_by_grid_index.items()}

starting_positions_by_entrypoint = {
    "top": (0, 0),
    "right": (area_size - 1, 0),
    "bottom": (area_size - 1, area_size - 1),
    "left": (0, area_size - 1),
}


def get_current_area(current_pos: tuple):
    area_idx = tuple(map(lambda x: int(x / area_size), current_pos))
    return area_by_grid_index[area_idx]


CURSOR_UP_ONE = "\x1b[1A"
ERASE_LINE = "\x1b[2K"


def print_grid():
    print(CURSOR_UP_ONE + CURSOR_UP_ONE)
    for j in range(max(positions.keys(), key=lambda x: x[1])[1] + 1):
        print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
    for j in range(max(positions.keys(), key=lambda x: x[1])[1] + 1):
        row = ""
        for i in range(max(positions.keys(), key=lambda x: x[0])[0] + 1):
            row += positions.get((i, j), " ")

        print(row, end="\n")
    sleep(0.01)


def update_direction(current_direction_index: tuple, change: str) -> tuple:
    return (current_direction_index + dir_changes[change]) % 4


def update_position(current_pos: tuple, direction_index: int) -> tuple:
    return (
        current_pos[0] + directions_clockwise[direction_index][0],
        current_pos[1] + directions_clockwise[direction_index][1],
    )


def wrap_position(current_pos: tuple, direction_index: int):
    direction_name = directions_named[direction_index]
    current_area = get_current_area(current_pos)

    transitions = area_transitions[current_area]
    target_area, orientation, direction_change = transitions[direction_name]
    new_direction_idx = (direction_index + direction_change) % 4

    new_start_position = tuple(
        map(lambda x: x * area_size, grid_index_by_area[target_area])
    )
    starting_position_offset = starting_positions_by_entrypoint[orientation]
    new_curr_pos = tuple(
        [a + b for a, b in zip(new_start_position, starting_position_offset)]
    )

    if direction_name == "left":
        offset = current_pos[1] % area_size
    if direction_name == "right":
        offset = (area_size - current_pos[1] - 1) % area_size
    elif direction_name == "bottom":
        offset = current_pos[0] % area_size
    elif direction_name == "top":
        offset = (area_size - current_pos[0] - 1) % area_size

    if orientation == "left":
        new_pos_x = new_curr_pos[0]
        new_pos_y = new_curr_pos[1] - offset
    if orientation == "right":
        new_pos_x = new_curr_pos[0]
        new_pos_y = new_curr_pos[1] + offset
    elif orientation == "bottom":
        new_pos_x = new_curr_pos[0] - offset
        new_pos_y = new_curr_pos[1]
    elif orientation == "top":
        new_pos_x = new_curr_pos[0] + offset
        new_pos_y = new_curr_pos[1]

    return (new_pos_x, new_pos_y), new_direction_idx


if test_file:
    assert wrap_position((11, 5), 0)[0] == (14, 8), "uh oh"
    assert wrap_position((10, 11), 1)[0] == (1, 7), "uh oh"
    assert wrap_position((6, 4), 3)[0] == (8, 2), "uh oh"

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
            if test_file:
                print_grid()

            candidate_position = update_position(current_position, direction_index)
            canidate_direction_index = direction_index
            map_obj = positions.get(candidate_position)

            if map_obj is None:
                candidate_position, canidate_direction_index = wrap_position(
                    current_position, direction_index
                )

            map_obj = positions.get(candidate_position)
            if map_obj == "#":
                break
            else:
                positions[current_position] = direction_drawings[direction_index]
                current_position = candidate_position
                direction_index = canidate_direction_index

if test_file:
    positions[current_position] = "*"
    print_grid()

score = (
    1000 * (current_position[1] + 1) + 4 * (current_position[0] + 1) + direction_index
)
print(score)
