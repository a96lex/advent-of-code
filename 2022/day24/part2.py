from collections import defaultdict
from heapq import heappop, heappush


og_grid = defaultdict(lambda: [])
valid_pos = set()
for j, line in enumerate(open(0).readlines()):
    for i, c in enumerate(line.strip("\n")):
        og_grid[(i - 1, j - 1)].append(c)
        if c in [".", ">", "v", "<", "^"]:
            valid_pos.add((i - 1, j - 1))


starting_point = (0, -1)
target_point = (i - 2, j - 1)

og_grid[starting_point] = "E"
og_grid[target_point] = "X"

lower_bound_x = 1
lower_bound_y = 1
upper_bound_x = i - 1
upper_bound_y = j - 1


def print_grid(grid_to_draw):
    min_h = min([y for x, y in grid_to_draw.keys()])
    max_h = max([y for x, y in grid_to_draw.keys()])
    min_w = min([x for x, y in grid_to_draw.keys()])
    max_w = max([x for x, y in grid_to_draw.keys()])

    for j in range(min_h, max_h + 1):
        row = ""
        for i in range(min_w, max_w + 1):
            arr = grid_to_draw[(i, j)]
            if len(arr) == 1:
                row += arr[0]
            elif len(arr) == 0:
                row += "."
            else:
                row += str(len(arr))
        print(row, end="\n")
    print("\n")


def get_nbrs(pos):
    nbr = [pos]
    for i in range(-1, 2, 2):
        nbr.append((pos[0] + i, pos[1]))
    for j in range(-1, 2, 2):
        nbr.append((pos[0], pos[1] + j))
    return nbr


def get_current_pos(grid_to_check):
    for k, v in grid_to_check.items():
        if v == "E":
            return k


move = {
    ">": lambda x, s: ((s + x[0]) % upper_bound_x, x[1]),
    "v": lambda x, s: (x[0], (s + x[1]) % upper_bound_y),
    "<": lambda x, s: ((x[0] - s) % upper_bound_x, x[1]),
    "^": lambda x, s: (x[0], (x[1] - s) % upper_bound_y),
}


def is_whithin_bounds(pos):
    ok = True
    if og_grid[pos] == "#":
        return False
    return not (
        pos[0] == 0 or pos[0] == upper_bound_x or pos[1] == 0 or pos[1] == upper_bound_y
    )


heap = [(0, starting_point, False, False)]
seen_states = set()
seen_states.add(heap[0])

c = 0
while True:
    steps, e_pos, has_been_to_x, has_been_to_e = heappop(heap)
    c += 1
    if c % 1000 == 0:
        print(c, steps)

    updated_dict = defaultdict(lambda: [])
    for k, v in og_grid.items():
        for arrow in v:
            if arrow in [">", "v", "<", "^"]:
                new_pos = move[arrow](k, steps + 1)
                updated_dict[new_pos].append(arrow)
            if arrow in ["#", "X"]:
                updated_dict[k].append(arrow)

    candidate_positions = get_nbrs(e_pos)

    for pos in candidate_positions:
        if updated_dict[pos] == ["X"]:
            if has_been_to_e:
                print(steps + 1)
                exit()
            if not has_been_to_x:
                heap = []
                has_been_to_x = True

        if pos == starting_point:
            if has_been_to_x:
                if not has_been_to_e:
                    has_been_to_e = True
                    heap = []

        if updated_dict[pos] in [[], ["E"], ["X"]] and pos in valid_pos:
            new_state = (steps + 1, pos, has_been_to_x, has_been_to_e)
            if new_state not in seen_states:
                seen_states.add(new_state)
                heappush(heap, new_state)
