import sys

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


score = 0
line_count = 0
intersected_badges = set()
for line in sys.stdin.readlines():
    items = line.replace("\n", "")
    if line_count % 3 == 0:
        intersected_badges = set(items)
    else:
        intersected_badges = intersected_badges.intersection(set(items))
        if line_count % 3 == 2:
            common_item = list(intersected_badges)[0]
            score += alphabet.index(common_item) + 1

    line_count += 1

print(score)
