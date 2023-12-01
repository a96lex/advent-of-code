with open("input.dat", "r") as f:
    data = [line.replace("\n", "") for line in f.readlines()]


def get_score(tree_seq) -> int:
    root_height = tree_seq[0]
    score = 0
    for tree in tree_seq[1:]:
        score += 1
        if tree >= root_height:
            break
    return score


best_views = 0

for row in range(len(data)):
    for column in range(len(data[0])):
        total_score = 1

        sequences = []

        # top
        top_sequence = [some_rows[column] for some_rows in data[: row + 1]]
        top_sequence.reverse()
        sequences.append(top_sequence)

        # left
        left_sequence = [x for x in data[row][column:]]
        sequences.append(left_sequence)

        # down
        down_sequence = [some_rows[column] for some_rows in data[row:]]
        sequences.append(down_sequence)

        # right
        right_sequence = [x for x in data[row][: column + 1]]
        right_sequence.reverse()
        sequences.append(right_sequence)

        for seq in sequences:
            score = get_score(seq)
            total_score *= score

        best_views = max(total_score, best_views)

print(best_views)
