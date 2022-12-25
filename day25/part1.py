from math import log

char_to_num = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
num_to_char = {v: k for k, v in char_to_num.items()}


def snafu_to_dec(num: str) -> int:
    total_c = len(num)
    val = 0
    for i, c in enumerate(num):
        val += 5 ** (total_c - i - 1) * char_to_num[c]
    return val


def dec_to_snafu(num: int) -> str:
    digits = int(round(log(num, 5) + 1, 0))
    res = ""
    for d in range(digits - 1, -1, -1):
        diff = 5 ** (d + 1)
        base = 5**d
        digit = None
        for j in range(-2, 3):
            new_diff = abs(num - base * j)
            if diff > new_diff:
                diff = new_diff
                digit = j
        num -= base * digit
        res += num_to_char[digit]
    return res


total_sum = 0
for line in open(0).readlines():
    total_sum += snafu_to_dec(line.strip("\n"))

print(dec_to_snafu(total_sum))
