from collections import defaultdict


with open("input.dat") as f:
    positions, instructions = f.read().split("\n\n")

crates = defaultdict(lambda: [])

for row in positions.split("\n")[:-1]:
    for i in range(int(len(row) / 4 + 1)):
        letter = row[i * 4 + 1]
        if letter != " ":
            crates[i + 1].append(letter)

for crate in crates.keys():
    crates[crate].reverse()

for instruction in instructions.split("\n"):
    if instruction == "":
        break

    _move, _from, _to = list(
        map(
            int,
            instruction.replace("move ", "")
            .replace(" from ", ",")
            .replace(" to ", ",")
            .split(","),
        )
    )

    crate_value = crates[_from]
    crates[_from], letter = crate_value[:-_move], crate_value[-_move:]
    crates[_to] += letter


word = ""
for i in range(len(crates.keys())):
    letter = crates[i + 1].pop()
    word += letter

print(word)
