import sys

count = 0
for line in sys.stdin.readlines():
    a, b = line.replace("\n", "").split(",")
    x1, x2 = map(int, a.split("-"))
    y1, y2 = map(int, b.split("-"))
    if (x1 <= y1 and x2 >= y1) or (y1 <= x1 and y2 >= x1):
        count += 1

print(count)
