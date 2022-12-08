with open("input.dat", "r") as f:
    data = [line.replace("\n", "") for line in f.readlines()]

visible_trees = set()
for row in range(len(data)):
    # left
    max_height = -1
    for column in range(len(data[row])):
        height = int(data[row][column])
        if height > max_height:
            max_height = height
            visible_trees.add((row, column))

    # right
    max_height = -1
    for column in range(len(data[row]) - 1, 0, -1):
        height = int(data[row][column])
        if height > max_height:
            max_height = height
            visible_trees.add((row, column))

for column in range(len(data[0])):
    # top
    max_height = -1
    for row in range(len(data)):
        height = int(data[row][column])
        if height > max_height:
            max_height = height
            visible_trees.add((row, column))

    # bottom
    max_height = -1
    for row in range(len(data) - 1, 0, -1):
        height = int(data[row][column])
        if height > max_height:
            max_height = height
            visible_trees.add((row, column))

print(len(list(visible_trees)))
