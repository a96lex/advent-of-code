import json

with open("input.dat") as f:
    data = f.read().split("\n\n")


def compare(l1, l2):  # returns right_order
    if type(l1) == int and type(l2) == list:
        l1 = [l1]
    if type(l2) == int and type(l1) == list:
        l2 = [l2]

    if type(l1) == type(l2) == int:
        if l1 > l2:
            return False
        if l1 < l2:
            return True
    else:
        right_order = None
        if len(l1) > len(l2):
            right_order = False
        if len(l1) < len(l2):
            right_order = True

        for a, b in zip(l1, l2):
            right_order_inner = compare(a, b)
            if right_order_inner is None:
                continue
            else:
                return right_order_inner

        return right_order


count = 0
score = 0
for pair in data:
    a, b = [json.loads(l) for l in pair.split("\n")]

    right_order = compare(a, b)

    count += 1
    score += right_order * count

print(score)
