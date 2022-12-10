import sys

CHAR_COUNT = 14

for line in sys.stdin.readlines():
    string = line.replace("\n", "")

    for i in range(CHAR_COUNT, len(string) + 1):
        four_last = string[i - CHAR_COUNT : i]
        if len(list(set(four_last))) == CHAR_COUNT:
            print(i, four_last)
            break
