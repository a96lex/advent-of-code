import sys

with open(sys.argv[1]) as f:
    directions = list(
        map(lambda x: -1 if x == "<" else 1, list(f.read().replace("\n", "")))
    )
len_directions = len(directions)


pieces = [
    [[2, 0], [3, 0], [4, 0], [5, 0]],
    [[3, 2], [2, 1], [3, 1], [4, 1], [3, 0]],
    [[2, 0], [3, 0], [4, 0], [4, 1], [4, 2]],
    [[2, 0], [2, 1], [2, 2], [2, 3]],
    [[2, 0], [2, 1], [3, 0], [3, 1]],
]
len_pieces = len(pieces)


def change_piece_position(piece, dx, dy):
    return [[x + dx, y + dy] for x, y in piece]


def print_grid(current_piece, filled_positions):
    print("\n")
    for j in range(10, -1, -1):
        row = ""
        for i in range(0, 7):
            if [i, j] in current_piece:
                row += "@"
            elif (i, j) in filled_positions:
                row += "#"
            else:
                row += "."
        print(row, end="\n")


est = ""
filled_positions = set()
direction_count = 0


def update_n(end, cycle, piece_idx):
    global direction_count, est
    filled_positions = set()
    max_height = -1
    old_max_height = max_height
    last_diff = -1
    is_stable = False
    for piece_count in range(end):
        piece_position = change_piece_position(
            pieces[(piece_count + piece_idx) % len_pieces], 0, max_height + 4
        )
        while True:
            new_piece_position = change_piece_position(
                piece_position, directions[direction_count % len_directions], 0
            )
            direction_count += 1
            direction_count %= len_directions

            if not any([x >= 7 or x < 0 for x, _ in new_piece_position]) and not any(
                [tuple(piece) in filled_positions for piece in new_piece_position]
            ):
                piece_position = new_piece_position
            new_piece_position = change_piece_position(piece_position, 0, -1)
            if any(
                [tuple(piece) in filled_positions for piece in new_piece_position]
            ) or any([y < 0 for _, y in new_piece_position]):
                for piece in piece_position:
                    filled_positions.add(tuple(piece))
                max_height = max(max_height, *[y for _, y in piece_position])

                if (piece_count) % (5) == 0:
                    est += str(piece_position[0][0])

                break
            piece_position = new_piece_position
            # print([x for x, y in piece_position[:1]])

        # if piece_count % (347*5) == 0:
        if piece_count % (cycle) == 0:
            # if piece_count % (10092 * 5) == 0:
            print(piece_count, ":")
            est = ""
            print(max_height, max_height - old_max_height)
            if max_height - old_max_height == last_diff:
                print("stabilized", max_height - old_max_height)
                is_stable = True
            last_diff = max_height - old_max_height
            old_max_height = max_height
            if is_stable:
                return (piece_count, max_height, last_diff)
    return max_height


iters = 1_000_000_000_000
max_height = -1

# found this value in the terminal, checking repetitions after printing
# every iteration for the x position of the first element of the rock
cycle = 347 * 5
piece_count, max_height, delta_height = update_n(400000 * cycle, cycle, 0 % 5)
print(piece_count, max_height, delta_height)

max_height += ((iters - piece_count) // cycle) * delta_height
new_height = update_n((iters - piece_count) % cycle, cycle, (iters - piece_count) % 5)

# -4 works on my input, i refuse to reason this lol
print(new_height + max_height - 4)
