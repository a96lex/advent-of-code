import sys
import re


seen_states = {}
counter = 0


def get_max_geodes(
    remaining_time: int, robots: list, resources: list, recipes: list, max_bots: list
) -> int:
    global counter

    if remaining_time == 0:
        return resources[3]

    cache_key = (*robots, *resources, remaining_time)
    if cache_key in seen_states:
        return seen_states[cache_key]

    max_geodes = resources[3] + robots[3] * remaining_time
    counter += 1
    if counter % 10000 == 0:
        pass
        # print(counter, remaining_time)

    for bot_type, recipe in enumerate(recipes):
        if bot_type != 3 and robots[bot_type] >= max_bots[bot_type]:
            continue

        waiting_time = 0
        for resource, cost in recipe:
            if robots[resource] == 0:
                break
            waiting_time = max(
                waiting_time, -(-(cost - resources[resource]) // robots[resource])
            )
            # print(
            #     "wait",
            #     waiting_time,
            #     robots[resource],
            #     cost,
            #     resource,
            #     resources,
            # )

        else:
            new_time = remaining_time - waiting_time - 1
            if new_time < 0:
                continue

            _robots = robots.copy()

            _resources = [
                x + y * (waiting_time + 1) for x, y in zip(resources, _robots)
            ]
            for resource, cost in recipe:
                _resources[resource] -= cost
            _robots[bot_type] += 1

            for i in range(3):
                _resources[i] = min(_resources[i], max_bots[i] * new_time)
            max_geodes = max(
                max_geodes,
                get_max_geodes(new_time, _robots, _resources, recipes, max_bots),
            )

    seen_states[cache_key] = max_geodes
    return max_geodes


max_stuff = 1

for line in sys.stdin.readlines():
    (
        blueprint_n,
        ore_cost_ore,
        clay_cost_ore,
        obsidian_cost_ore,
        obsidian_cost_clay,
        geode_cost_ore,
        geode_cost_obsidian,
    ) = list(map(int, re.findall(r"[0-9]+", line)))
    if blueprint_n == 4:
        break
    robots = [1, 0, 0, 0]
    resources = [0, 0, 0, 0]
    recipes = [
        [(0, ore_cost_ore)],
        [(0, clay_cost_ore)],
        [(0, obsidian_cost_ore), (1, obsidian_cost_clay)],
        [(0, geode_cost_ore), (2, geode_cost_obsidian)],
    ]
    # print(recipes)

    max_bots = [0, 0, 0, float("inf")]
    for c in recipes:
        for k, v in c:
            max_bots[k] = max(max_bots[k], v)

    max_geodes = 0
    max_geodes = get_max_geodes(32, robots, resources, recipes, max_bots)
    seen_states = {}
    print(max_geodes)

    max_stuff *= max_geodes

print(max_stuff)
