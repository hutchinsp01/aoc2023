from utils.api import get_input, get_test_input
from utils.common import (
    Grid,
    Point,
    VectorDicts,
    Vectors,
    binary_search,
    get_factors,
    to_base_n,
)

DIRECTIONS = {
    "|": [Point(0, 1), Point(0, -1)],
    "-": [Point(1, 0), Point(-1, 0)],
    "L": [Point(1, 0), Point(0, -1)],
    "J": [Point(-1, 0), Point(0, -1)],
    "7": [Point(-1, 0), Point(0, 1)],
    "F": [Point(1, 0), Point(0, 1)],
    ".": [],
    "S": [Point(0, 1)],
}

input_str = get_input(10)
# input_str = get_test_input(10)


def part_a():
    grid = Grid(input_str.splitlines())
    seen = set()

    start = None
    for point in grid.all_points():
        if grid.value_at_point(point) == "S":
            start = point
            break

    # breadth first search
    queue = [start]
    ordered_points = [start]
    max_score = 0
    while queue:
        point = queue.pop(0)
        seen.add(point)

        if not grid.valid_location(point):
            continue
        if point.score > max_score:
            max_score = point.score
        for direction in DIRECTIONS[grid.value_at_point(point)]:
            if not grid.valid_location(point + direction):
                continue
            if grid.value_at_point(point + direction) == ".":
                continue
            new_point = point + direction
            new_point.score = point.score + 1
            if new_point not in seen:
                ordered_points.append(new_point)
                queue.append(new_point)

    return max_score, ordered_points, grid


# def part_b():
#     loop, grid = part_a()[1:]
#     print(loop)

#     new_grid = []
#     for i in range(grid.height):
#         new_grid.append(["."] * grid.width)
#     for point in loop:
#         new_grid[point.y][point.x] = "X"

#     double_size_grid = []
#     for i in range(grid.height * 2):
#         double_size_grid.append(["."] * grid.width * 2)

#     double_size_grid = Grid(double_size_grid)
#     start = True
#     last_point = None
#     for point in loop:
#         if start:
#             double_size_grid.set_value_at_point(Point(point.x * 2, point.y * 2), "X")
#             double_size_grid.set_value_at_point(
#                 Point(point.x * 2 + 1, point.y * 2), "X"
#             )
#             double_size_grid.set_value_at_point(
#                 Point(point.x * 2, point.y * 2 + 1), "X"
#             )
#             double_size_grid.set_value_at_point(
#                 Point(point.x * 2 + 1, point.y * 2 + 1), "X"
#             )
#             start = False
#             last_point = Point(point.x * 2 + 1, point.y * 2 + 1)
#         else:
#             next_point = Point(point.x * 2, point.y * 2)
#             cur = last_point
#             x_diff = next_point.x - last_point.x
#             y_diff = next_point.y - last_point.y
#             while x_diff:
#                 if x_diff > 0:
#                     cur = cur + Point(1, 0)
#                     double_size_grid.set_value_at_point(cur, "X")
#                     x_diff -= 1
#                 else:
#                     cur = cur + Point(-1, 0)
#                     double_size_grid.set_value_at_point(cur, "X")
#                     x_diff += 1
#             while y_diff:
#                 if y_diff > 0:
#                     cur = cur + Point(0, 1)
#                     double_size_grid.set_value_at_point(cur, "X")
#                     y_diff -= 1
#                 else:
#                     cur = cur + Point(0, -1)
#                     double_size_grid.set_value_at_point(cur, "X")
#                     y_diff += 1
#             last_point = next_point

#     # flood fill
#     queue = [Point(-2, -2)]
#     seen = set()
#     while queue:
#         point = queue.pop(0)

#         if point in seen:
#             continue

#         seen.add(point)

#         for new_point in [x for x in point.neighbours()]:
#             if new_point in seen:
#                 continue
#             if not double_size_grid.valid_location(new_point):
#                 if (
#                     -2 <= point.x <= double_size_grid.width + 2
#                     and -2 <= point.y <= double_size_grid.height + 2
#                 ):
#                     queue.append(new_point)
#                 continue
#             if not double_size_grid.value_at_point(new_point) == ".":
#                 continue
#             queue.append(new_point)

#             double_size_grid.set_value_at_point(new_point, "X")

#     # print(double_size_grid)

#     count = 0
#     for point in grid.all_points():
#         scaled_point = Point(point.x * 2, point.y * 2)
#         if double_size_grid.value_at_point(scaled_point) == ".":
#             count += 1

#     return count


# def part_b():
#     loop, grid = part_a()[1:]

#     new_grid = []
#     for i in range(grid.height):
#         new_grid.append(["."] * grid.width)

#     for point in loop:
#         new_grid[point.y][point.x] = grid.value_at_point(point)

#     space_1_set = set()
#     space_1_direction = Point(-1, 0)

#     prev_point = loop[0]
#     cur_direction = Point(0, -1)

#     new_grid = Grid(new_grid)
#     print(new_grid)

#     for i, point in enumerate(loop):
#         direction = point - prev_point
#         prev_point = point

#         if direction == cur_direction:
#             if point + space_1_direction not in loop:
#                 new_grid.set_value_at_point(point + space_1_direction, "X")
#                 space_1_set.add(point + space_1_direction)
#             continue

#         if cur_direction == Point(1, 0):
#             if direction == Point(0, -1):
#                 if space_1_direction == Point(0, 1):
#                     space_1_direction = Point(1, 0)
#                 if space_1_direction == Point(0, -1):
#                     space_1_direction = Point(-1, 0)
#             if direction == Point(0, 1):
#                 if space_1_direction == Point(0, 1):
#                     space_1_direction = Point(-1, 0)
#                 if space_1_direction == Point(0, -1):
#                     space_1_direction = Point(1, 0)
#         if cur_direction == Point(0, -1):
#             if direction == Point(1, 0):
#                 if space_1_direction == Point(1, 0):
#                     space_1_direction = Point(0, 1)
#                 if space_1_direction == Point(-1, 0):
#                     space_1_direction = Point(0, -1)
#             if direction == Point(-1, 0):
#                 if space_1_direction == Point(1, 0):
#                     space_1_direction = Point(0, -1)
#                 if space_1_direction == Point(-1, 0):
#                     space_1_direction = Point(0, 1)
#         if cur_direction == Point(-1, 0):
#             if direction == Point(0, -1):
#                 if space_1_direction == Point(0, 1):
#                     space_1_direction = Point(-1, 0)
#                 if space_1_direction == Point(0, -1):
#                     space_1_direction = Point(1, 0)
#             if direction == Point(0, 1):
#                 if space_1_direction == Point(0, 1):
#                     space_1_direction = Point(1, 0)
#                 if space_1_direction == Point(0, -1):
#                     space_1_direction = Point(-1, 0)
#         if cur_direction == Point(0, 1):
#             if direction == Point(-1, 0):
#                 if space_1_direction == Point(1, 0):
#                     space_1_direction = Point(0, 1)
#                 if space_1_direction == Point(-1, 0):
#                     space_1_direction = Point(0, -1)
#             if direction == Point(1, 0):
#                 if space_1_direction == Point(1, 0):
#                     space_1_direction = Point(0, -1)
#                 if space_1_direction == Point(-1, 0):
#                     space_1_direction = Point(0, 1)

#         if point + space_1_direction not in loop:
#             new_grid.set_value_at_point(point + space_1_direction, "X")
#             space_1_set.add(point + space_1_direction)
#         cur_direction = direction

#     # flood fill
#     queue = [Point(-1, -1)] + list(space_1_set)
#     seen = set()

#     while queue:
#         point = queue.pop(0)

#         if point in seen:
#             continue

#         seen.add(point)

#         for new_point in [x for x in point.neighbours()]:
#             if new_point in seen:
#                 continue
#             if not new_grid.valid_location(new_point):
#                 if (
#                     -1 <= point.x <= new_grid.width + 1
#                     and -1 <= point.y <= new_grid.height + 1
#                 ):
#                     queue.append(new_point)
#                 continue
#             if not new_grid.value_at_point(new_point) == ".":
#                 continue
#             queue.append(new_point)

#             new_grid.set_value_at_point(new_point, "X")

#     total = 0
#     for point in new_grid.all_points():
#         if new_grid.value_at_point(point) == ".":
#             total += 1

#     print(new_grid)
#     return total


def part_b():
    loop, grid = part_a()[1:]

    new_grid = []
    for i in range(grid.height):
        new_grid.append(["."] * grid.width)
    for point in loop:
        new_grid[point.y][point.x] = "X"

    triple_size_grid = []
    for i in range(grid.height * 3):
        triple_size_grid.append(["."] * grid.width * 3)

    triple_size_grid = Grid(triple_size_grid)

    for pipe in loop:
        pipe_type = grid.value_at_point(pipe)
        if pipe_type == "S":
            pipe_type = "7"
        if pipe_type == "F":
            triple_size_grid.set_value_at_point(Point(pipe.x * 3, pipe.y * 3), "X")
            triple_size_grid.set_value_at_point(Point(pipe.x * 3 + 1, pipe.y * 3), "X")
            triple_size_grid.set_value_at_point(Point(pipe.x * 3, pipe.y * 3 + 1), "X")
        if pipe_type == "7":
            triple_size_grid.set_value_at_point(Point(pipe.x * 3 - 1, pipe.y * 3), "X")
            triple_size_grid.set_value_at_point(Point(pipe.x * 3, pipe.y * 3), "X")
            triple_size_grid.set_value_at_point(Point(pipe.x * 3, pipe.y * 3 + 1), "X")
        if pipe_type == "L":
            triple_size_grid.set_value_at_point(Point(pipe.x * 3, pipe.y * 3 - 1), "X")
            triple_size_grid.set_value_at_point(Point(pipe.x * 3, pipe.y * 3), "X")
            triple_size_grid.set_value_at_point(Point(pipe.x * 3 + 1, pipe.y * 3), "X")
        if pipe_type == "J":
            triple_size_grid.set_value_at_point(Point(pipe.x * 3, pipe.y * 3), "X")
            triple_size_grid.set_value_at_point(Point(pipe.x * 3, pipe.y * 3 - 1), "X")
            triple_size_grid.set_value_at_point(Point(pipe.x * 3 - 1, pipe.y * 3), "X")
        if pipe_type == "-":
            triple_size_grid.set_value_at_point(Point(pipe.x * 3 + 1, pipe.y * 3), "X")
            triple_size_grid.set_value_at_point(Point(pipe.x * 3, pipe.y * 3), "X")
            triple_size_grid.set_value_at_point(Point(pipe.x * 3 - 1, pipe.y * 3), "X")
        if pipe_type == "|":
            triple_size_grid.set_value_at_point(Point(pipe.x * 3, pipe.y * 3 + 1), "X")
            triple_size_grid.set_value_at_point(Point(pipe.x * 3, pipe.y * 3), "X")
            triple_size_grid.set_value_at_point(Point(pipe.x * 3, pipe.y * 3 - 1), "X")

    # flood fill
    queue = [Point(-1, -1)]
    seen_order = [Point(-1, -1)]
    seen = set()
    while queue:
        point = queue.pop(0)

        if point in seen:
            continue

        seen.add(point)
        seen_order.append(point)

        for new_point in [x for x in point.neighbours()]:
            if new_point in seen:
                continue
            if not triple_size_grid.valid_location(new_point):
                if (
                    -1 <= point.x <= triple_size_grid.width + 1
                    and -1 <= point.y <= triple_size_grid.height + 1
                ):
                    queue.append(new_point)
                continue
            if not triple_size_grid.value_at_point(new_point) == ".":
                continue
            queue.append(new_point)

            triple_size_grid.set_value_at_point(new_point, "X")

    total = 0
    for point in grid.all_points():
        scaled_point = Point(point.x * 3, point.y * 3)
        if triple_size_grid.value_at_point(scaled_point) == ".":
            total += 1

    return total, seen_order


print(part_a()[0])
print(part_b()[0])


def get_file_name(i: int) -> str:
    return f"r{i}.mcfunction"


def get_load_tick_name(i: int) -> str:
    return f"r{i}_0"


def vis():
    loop, grid = part_a()[1:]
    seen_order = part_b()[1]
    load_tick_list = []
    base_file_num = 2
    commands_in_tick = 25
    directory = "/Users/hutchinsp01/Projects/personal/world/datapacks/day10/data/day10/functions/"

    tick = 0
    command_str = ""
    cur_commands_in_tick = 0
    load_tick_name = get_load_tick_name(base_file_num)
    for point in loop:
        cur_commands_in_tick += 1
        load_tick_name = get_load_tick_name(base_file_num)

        command_str += f"execute if data storage dp_conv:day10 {{{load_tick_name}_auto:1b}} run execute if score #timer delay matches {tick} run setblock {point.x} -60 {point.y} minecraft:lime_wool\n"

        if cur_commands_in_tick == commands_in_tick:
            cur_commands_in_tick = 0
            tick += 1

    command_str += f"execute if data storage dp_conv:day10 {{{load_tick_name}_auto:1b}} run execute if score #timer delay matches {700} run fill 0 -60 0 139 -60 139 minecraft:air"

    with open(directory + get_file_name(base_file_num), "w") as f:
        f.write(command_str + "\n")
        load_tick_list.append(load_tick_name)

    # reset
    # tick = 700
    # file_name = get_file_name(file_count)
    # load_tick_name = get_load_tick_name(file_count)
    command_str = f"execute if data storage dp_conv:day10 {{{load_tick_name}_auto:1b}} run execute if score #timer delay matches {tick} run fill 0 -60 0 139 -60 139 minecraft:air"
    # with open(directory + file_name, "w") as f:
    #     f.write(command_str + "\n")
    # load_tick_list.append(load_tick_name)

    # file_count += 1

    # copy from tick-base.mcfunction
    tick_base = open(
        "/Users/hutchinsp01/Projects/personal/AOC2023/src/vis/tick-base.mcfunction", "r"
    ).read()
    with open(directory + "tick.mcfunction", "w") as f:
        f.write(tick_base + "\n")
        for load_tick in load_tick_list:
            # execute if data storage dp_conv:day10 {r0_0_auto:1b} run function day10:r0
            f.write(
                f"execute if data storage dp_conv:day10 {{{load_tick}_auto:1b}} run function day10:{load_tick.split('_')[0]}\n"
            )
        for load_tick in load_tick_list:
            f.write(
                f"execute if data storage dp_conv:day10 {{{load_tick}_auto:1b}} run data merge storage dp_conv:day10 {{{load_tick}_success:0b}}\n"
            )

    # copy from init-base.mcfunction
    init_base = open(
        "/Users/hutchinsp01/Projects/personal/AOC2023/src/vis/init-base.mcfunction", "r"
    ).read()
    with open(directory + "init.mcfunction", "w") as f:
        f.write(init_base + "\n")
        for load_tick in load_tick_list:
            f.write(f'data merge storage dp_conv:day10 {{"{load_tick}_auto":0b}}\n')


vis()
