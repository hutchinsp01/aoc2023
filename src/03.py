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

input_str = get_input(3)
# input_str = get_test_input(3)

NUMS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def part_a():
    arr = []
    for line in input_str.splitlines():
        l = []
        for char in line:
            l.append(char)
        arr.append(l)

    grid = Grid(arr)

    cur_sum = 0
    cur_num = ""
    valid_point = False
    for point in grid.all_points():
        if grid.value_at_point(point) not in NUMS:
            if valid_point:
                valid_point = False
                cur_sum += int(cur_num)
            cur_num = ""
            continue

        cur_num += str(grid.value_at_point(point))

        for neighbour in point.yield_neighbors(include_diagonals=True):
            if (
                grid.valid_location(neighbour)
                and grid.value_at_point(neighbour) not in NUMS
                and grid.value_at_point(neighbour) != "."
            ):
                valid_point = True

        if point.x == grid.width - 1 and valid_point:
            valid_point = False
            cur_sum += int(cur_num)
            cur_num = ""
            continue

    return cur_sum


def part_b():
    arr = []
    for line in input_str.splitlines():
        l = []
        for char in line:
            l.append(char)
        arr.append(l)

    grid = Grid(arr)

    tot = 0
    for point in grid.all_points():
        neighbours = 0
        neighbour_nums = set()
        if grid.value_at_point(point) != "*":
            continue

        for neighbour in point.yield_neighbors(include_diagonals=True):
            if (
                grid.valid_location(neighbour)
                and grid.value_at_point(neighbour) in NUMS
            ):
                neighbours += 1

                num_start = neighbour
                while (
                    grid.valid_location(num_start)
                    and grid.value_at_point(neighbour) in NUMS
                ):
                    num_start = neighbour
                    neighbour += Point(x=-1, y=0)

                num = ""
                while (
                    grid.valid_location(num_start)
                    and grid.value_at_point(num_start) in NUMS
                ):
                    num += str(grid.value_at_point(num_start))
                    num_start += Point(x=1, y=0)

                neighbour_nums.add(int(num))

        if len(neighbour_nums) == 2:
            tot += neighbour_nums.pop() * neighbour_nums.pop()

    return tot


print(part_a())
print(part_b())
