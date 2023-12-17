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

input_str = get_input(11)
# input_str = get_test_input(11)


def part_a():
    as_str = input_str.splitlines()
    new_as_str = []
    for row in as_str:
        if "#" not in row:
            new_as_str.append(row)
        new_as_str.append(row)

    as_str = list(zip(*new_as_str[::-1]))
    new_as_str = []
    for row in as_str:
        if "#" not in row:
            new_as_str.append(row)
        new_as_str.append(row)

    as_str = list(zip(*new_as_str[::-1]))
    grid = Grid(as_str)

    points = []
    for point in grid.all_points():
        if grid.value_at_point(point) == "#":
            points.append(point)

    all_pairs = []
    for i, point in enumerate(points):
        for point2 in points[i + 1 :]:
            all_pairs.append((point, point2))

    total = 0
    for pair in all_pairs:
        total += pair[0].manhattan_distance(pair[1])

    return total


def part_b():
    as_str = input_str.splitlines()
    new_as_str = []
    for row in as_str:
        if "#" not in row:
            new_as_str.append("X" * len(row))
        else:
            new_as_str.append(row)

    as_str = list(zip(*new_as_str[::-1]))
    new_as_str = []
    for row in as_str:
        if "#" not in row:
            new_as_str.append("X" * len(row))
        else:
            new_as_str.append(row)

    as_str = list(zip(*new_as_str[::-1]))
    grid = Grid(as_str)

    points = []
    for point in grid.all_points():
        if grid.value_at_point(point) == "#":
            points.append(point)

    all_pairs = []
    for i, point in enumerate(points):
        for point2 in points[i + 1 :]:
            all_pairs.append((point, point2))

    total = 0
    for pair in all_pairs:
        total += pair[0].manhattan_distance(pair[1])
        if pair[0].x > pair[1].x:
            x_range = range(pair[1].x + 1, pair[0].x)
        else:
            x_range = range(pair[0].x + 1, pair[1].x)
        if pair[0].y > pair[1].y:
            y_range = range(pair[1].y + 1, pair[0].y)
        else:
            y_range = range(pair[0].y + 1, pair[1].y)
        for x in x_range:
            if grid.value_at_point(Point(x, 0)) == "X":
                total += 1000000 - 1
        for y in y_range:
            if grid.value_at_point(Point(0, y)) == "X":
                total += 1000000 - 1

    return total


def part_b_2():
    exp_1 = part_a()

    as_str = input_str.splitlines()
    grid = Grid(as_str)
    points = []
    for point in grid.all_points():
        if grid.value_at_point(point) == "#":
            points.append(point)

    all_pairs = []
    for i, point in enumerate(points):
        for point2 in points[i + 1 :]:
            all_pairs.append((point, point2))

    exp_0 = 0
    for pair in all_pairs:
        exp_0 += pair[0].manhattan_distance(pair[1])

    total = exp_0 + (exp_1 - exp_0) * (1000000 - 1)
    return total


print(part_a())
print(part_b())
print(part_b_2())
