import sys
import textwrap


class Data:
    score = 0
    cycles = 0
    register_x = 1
    sprite_positions = [0, 1, 2]
    result = ""

    def update(self, value: int = None) -> None:
        if self.cycles in self.sprite_positions:
            self.result += "#"
        else:
            self.result += "."

        self.cycles += 1
        self.cycles %= 40
        if value:
            self.sprite_positions = [(a + value) % 40 for a in self.sprite_positions]


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


print("\n".join(textwrap.wrap(score_tracker.result, 40)))
