import sys

possible_operations = {
    "-": lambda x, y: x - y,
    "+": lambda x, y: x + y,
    "/": lambda x, y: x / y,
    "*": lambda x, y: x * y,
}


class Node:
    def __init__(
        self, name: str, left=None, right=None, value=None, operation=None
    ) -> None:
        self.name = name
        self.left = left
        self.right = right
        self.value = value
        if operation:
            self.operation = possible_operations[operation]

    def __repr__(self) -> str:
        print(self.name)
        if self.value is not None:
            return f"val:{self.value}"
        return f"right:{self.right}, left:{self.left}, op:{self.operation}"


node_dict = {}

for line in sys.stdin.readlines():
    name = line[:4]
    try:
        value = int(line.split(" ")[1])
        new_node = Node(name, value=value)
        node_dict[name] = new_node
    except ValueError as e:
        left, operation, right = line[6:].replace("\n", "").split(" ")
        new_node = Node(name, left=left, right=right, operation=operation)
        node_dict[name] = new_node


def shit(node: Node):
    if node.name == "root":
        print(node)


def find_value(node: Node):
    if node.value is not None:
        return node.value
    return node.operation(
        find_value(node_dict[node.left]), find_value(node_dict[node.right])
    )


# Initialize humn to 0, and choose an increment to perform checks
# This is the best value to start with
humn: Node = node_dict["humn"]
humn.value = 0
increment = 1000000000000

root = node_dict["root"]

# from trial-error I know that v2 value does not change
# (humn is on the left side of the root node)
v2 = find_value(node_dict[root.right])

iters = 0
while True:
    iters += 1
    v1 = find_value(node_dict[root.left])

    if v1 == v2:
        break

    if v1 / v2 < 1:
        humn.value -= increment
        increment /= 10
        continue

    humn.value += increment


print(f"Found answer after {iters} iterations: {int(humn.value)}")
