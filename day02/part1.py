options_and_scores = {
    "X": {"value": 1, "A": 3, "B": 0, "C": 6},
    "Y": {"value": 2, "A": 6, "B": 3, "C": 0},
    "Z": {"value": 3, "A": 0, "B": 6, "C": 3},
}


with open("input.dat", "r") as f:
    data = [line.replace("\n", "") for line in f.readlines()]


score = 0
for line in data:
    choice_a, choice_b = line.split(" ")
    score += options_and_scores[choice_b]["value"]
    score += options_and_scores[choice_b][choice_a]

print(score)
