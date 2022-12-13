import json

with open("input.dat") as f:
    data = [json.loads(l) for l in f.readlines() if l != "\n"]
data += [[[2]]]
data += [[[6]]]


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


ordered_data = []

for value in data:
    if len(ordered_data) == 0:
        ordered_data.append(value)
    else:
        idx = None
        for i in range(len(ordered_data)):
            ordered = compare(value, ordered_data[i])
            if ordered:
                idx = i
                break

        if idx is not None:
            ordered_data = ordered_data[:idx] + [value] + ordered_data[idx:]
        else:
            ordered_data.append(value)

result = (ordered_data.index([[2]]) + 1) * (ordered_data.index([[6]]) + 1)


print(result)
