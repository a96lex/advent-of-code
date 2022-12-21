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


def find_value(node: Node):
    if node.value:
        return node.value
    return node.operation(
        find_value(node_dict[node.left]), find_value(node_dict[node.right])
    )


ans = find_value(node_dict["root"])
print(ans)
