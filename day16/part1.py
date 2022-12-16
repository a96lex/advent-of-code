import sys
from collections import defaultdict, deque
from copy import copy
from functools import lru_cache

all_pipes = defaultdict(lambda: {"connected_pipes": [], "flow_rate": 0})

pipes_with_flow = []
for line in sys.stdin.readlines():
    line_clean = (
        line.replace("\n", "")
        .replace("Valve ", "")
        .replace(" has flow rate=", ",")
        .replace("; tunnels lead to valves ", ",")
        .replace("; tunnel leads to valve ", ",")
        .replace(", ", ",")
        .split(",")
    )
    current_pipe, flow_rate, *connected_pipes = line_clean

    if int(flow_rate) > 0:
        pipes_with_flow.append(current_pipe)

    all_pipes[current_pipe]["flow_rate"] = int(flow_rate)
    all_pipes[current_pipe]["connected_pipes"] = connected_pipes


@lru_cache()
def find_distance(p1, p2):
    if p1 == p2:
        return 0

    seen = set()
    seen.add(p1)
    to_see = deque()

    for i in all_pipes[p1]["connected_pipes"]:
        seen.add(i)
        to_see.append((i, 1))

    while len(to_see):
        new_p, steps = to_see.popleft()
        if p2 == new_p:
            return steps
        for j in all_pipes[new_p]["connected_pipes"]:
            if j not in seen:
                seen.add(j)
                to_see.append((j, steps + 1))


# We need AA here cause is where we start
pipes_with_flow.append("AA")

distances = {}
for i in range(len(pipes_with_flow)):
    for j in range(i + 1, len(pipes_with_flow)):
        p1, p2 = pipes_with_flow[i], pipes_with_flow[j]
        distances[p1 + p2] = find_distance(p1, p2)
        distances[p2 + p1] = find_distance(p1, p2)

pipes_with_flow.remove("AA")


def generate_paths(current_valve, open_valves, remaining_time, score):
    for next_valve in pipes_with_flow:
        if (
            next_valve not in open_valves
            and next_valve != current_valve
            and distances[current_valve + next_valve] <= remaining_time
        ):
            open_valves = copy(open_valves)
            open_valves.append(next_valve)
            new_remaining_time = (
                remaining_time - distances[current_valve + next_valve] - 1
            )
            new_score = score + new_remaining_time * all_pipes[next_valve]["flow_rate"]
            yield (copy(open_valves), score)  # need for part 2
            yield from generate_paths(
                next_valve, open_valves, new_remaining_time, new_score
            )
            open_valves.pop()

    yield copy(open_valves), score


if __name__ == "__main__":
    print(max([a for _, a in generate_paths("AA", [], 30, 0)]))
