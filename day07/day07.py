import sys
from collections import defaultdict

tree = defaultdict(lambda: {"parent": "/", "children": set(), "size": 0})

current_dir = "/"
tree[current_dir]

for line in sys.stdin.readlines():
    line = line.replace("\n", "")
    command = line.split(" ")

    if command[0] == "$":
        if command[1] == "cd":
            new_dir = command[2]
            new_name = current_dir + "--" + new_dir

            if new_dir == "/":
                current_dir = "/"
                continue

            if new_dir == "..":
                current_dir = tree[current_dir]["parent"]
                continue

            tree[current_dir]["children"].add(new_name)
            tree[new_name]["parent"] = current_dir
            current_dir = new_name

    elif command[0] == "dir":
        tree[current_dir]["children"].add(current_dir + "--" + command[1])

    else:
        tree[current_dir]["size"] += int(command[0])


def get_dir_size(directory):
    size = tree[directory]["size"]

    children = tree[directory]["children"]

    for child in children:
        size += get_dir_size(child)

    return size


def part_1():
    total = 0
    for directory in tree.keys():
        size = get_dir_size(directory)
        if size <= 100000:
            total += size

    print(total)


def part_2():
    space_to_free = 30000000 - (70000000 - get_dir_size("/"))

    sizes = []
    for directory in tree.keys():
        size = get_dir_size(directory)
        if size > space_to_free:
            sizes.append(size)

    sizes.sort()

    print(sizes[0])


part_1()
part_2()
