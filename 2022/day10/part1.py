import sys


class Data:
    score = 0
    cycles = 0
    register_x = 1

    def update(self, value: int = None) -> None:
        self.cycles += 1
        if (self.cycles + 20) % 40 == 0:
            self.score += self.register_x * self.cycles
        if value:
            self.register_x += value


score_tracker = Data()
for instruction in sys.stdin.readlines():
    data = instruction.replace("\n", "").split(" ")
    operation = data[0]

    if operation == "noop":
        score_tracker.update()

    if operation == "addx":
        amount = int(data[1])
        score_tracker.update()
        score_tracker.update(amount)


print(score_tracker.score)
