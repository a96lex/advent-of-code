from collections import defaultdict

from part1 import generate_paths

all_ways = [a for a in generate_paths("AA", [], 26, 0)]

clean_paths = defaultdict(lambda: 0)
for way in all_ways:
    path = way[0]
    path.sort()
    path = tuple(path)
    clean_paths[path] = max(clean_paths[path], way[1])


better_ways = [(k, v) for k, v in clean_paths.items()]
len_ways = len(better_ways)

score = 0
for i in range(len_ways):
    human_path, human_score = better_ways[i]
    human_set = set(human_path)

    for j in range(i, len_ways):
        elephant_path, elephant_score = better_ways[j]
        elephant_set = set(elephant_path)

        if not human_set & elephant_set:
            score = max(score, human_score + elephant_score)

print(score)
