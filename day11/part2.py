from math import gcd


def lcm(*nums):  # because pyhon3.7
    lcm = 1
    for num in nums:
        lcm = (lcm * num) // gcd(lcm, num)
    return lcm


with open("input.dat", "r") as f:
    data = [line.replace("\n", "") for line in f.readlines()]

monkeys = []


class Monkey:
    inspections = 0
    divider = 3

    def __init__(
        self,
        items: list,
        operation: callable,
        test: int,
        monkey_if_true: int,
        monkey_if_false: int,
    ) -> None:
        self.items = items
        self.operation = operation
        self.test = test
        self.monkey_if_true = monkey_if_true
        self.monkey_if_false = monkey_if_false

    def accept_item(self, new_item):
        self.items.append(new_item)

    def update(self):
        global monkeys  # nice
        for item in self.items:
            old = item
            new = eval(self.operation)

            if new % self.test == 0:
                new_monkey = self.monkey_if_true
            else:
                new_monkey = self.monkey_if_false

            new = new % self.divider
            monkeys[new_monkey].accept_item(new)
            self.inspections += 1
        self.items = []


dividers = []
for i in range(int(len(data) / 7 + 1)):
    line_idx = i * 7
    items = list(map(int, data[line_idx + 1].split(":")[-1].split(",")))
    operation = data[line_idx + 2].split("new = ")[-1]
    test = int(data[line_idx + 3].split(" ")[-1])
    dividers.append(test)
    monkey_if_true = int(data[line_idx + 4].split(" ")[-1])
    monkey_if_false = int(data[line_idx + 5].split(" ")[-1])
    monkeys.append(Monkey(items, operation, test, monkey_if_true, monkey_if_false))

new_divider = lcm(*dividers)
for monkey in monkeys:
    monkey.divider = new_divider

for round_n in range(10000):
    c = 0
    for monkey in monkeys:
        c += 1
        monkey.update()


values = []
for monkey in monkeys:
    values.append(monkey.inspections)

values.sort(reverse=True)
print(values[0] * values[1])
