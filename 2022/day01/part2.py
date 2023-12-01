with open("input.dat", "r") as f:
    data = [line.replace("\n", "") for line in f.readlines()]

elfs = set()
current_elf = 0
for line in data:
    if line == "":
        elfs.add(current_elf)
        current_elf = 0
    else:
        current_elf += int(line)

print(sum(sorted(elfs)[-3:]))
