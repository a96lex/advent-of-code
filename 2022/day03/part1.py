import sys

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


score = 0
for line in sys.stdin.readlines():
    items = line.replace("\n", "")
    half_of_items = int(len(items) / 2)
    rack_a, rack_b = set(items[:half_of_items]), set(items[half_of_items:])
    common_item_set = rack_a.intersection(rack_b)
    common_item = list(common_item_set)[0]
    score += alphabet.index(common_item) + 1

print(score)
