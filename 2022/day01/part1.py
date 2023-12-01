with open("input.dat", "r") as f:
    data = [line.replace("\n", "") for line in f.readlines()]

max_elf = 0
current_elf = 0
for line in data:
    if line == "":
        max_elf = max(current_elf, max_elf)
        current_elf = 0
    else:
        current_elf += int(line)

print(max_elf)
