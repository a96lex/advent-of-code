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


filled_positions = set()
max_height = -1
direction_count = 0
for piece_count in range(2022):
    piece_position = change_piece_position(
        pieces[piece_count % len_pieces], 0, max_height + 4
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
            break
        piece_position = new_piece_position

print(max_height + 1)
