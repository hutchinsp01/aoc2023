import copy
import sys
from functools import lru_cache

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

input_str = get_input(14)
# input_str = get_test_input(14)

sys.set_int_max_str_digits(10001)


def part_a():
    rock_garden = Grid([list(x) for x in input_str.splitlines()])

    move = True

    while move:
        move = False
        for point in rock_garden.all_points():
            north = Point(point.x, point.y - 1)
            if rock_garden.valid_location(north):
                if (
                    rock_garden.value_at_point(point) == "O"
                    and rock_garden.value_at_point(north) == "."
                ):
                    rock_garden.set_value_at_point(north, "O")
                    rock_garden.set_value_at_point(point, ".")
                    move = True

    total = 0
    height = rock_garden.height
    for rock in rock_garden.all_points():
        if rock_garden.value_at_point(rock) == "O":
            total += height - rock.y

    return total


directions = {
    "N": Point(0, -1),
    "S": Point(0, 1),
    "E": Point(1, 0),
    "W": Point(-1, 0),
}


@lru_cache
def get_next_board(board: Grid) -> Grid:
    # print("++++++++++++++++")
    # print(board)
    board = copy.deepcopy(board)
    for direction in ["N", "W", "S", "E"]:
        look = directions[direction]

        move = True
        while move:
            move = False
            for point in board.all_points():
                new_point = point + look
                if board.valid_location(new_point):
                    if (
                        board.value_at_point(point) == "O"
                        and board.value_at_point(new_point) == "."
                    ):
                        board.set_value_at_point(new_point, "O")
                        board.set_value_at_point(point, ".")
                        move = True
    # print("\n")
    # print(board)
    return board


def part_b():
    board_state_hash = {}
    rock_garden = Grid([list(x) for x in input_str.splitlines()])

    i = 0
    end = 1000000000
    while i < end:
        print(i)
        if i % 10000 == 0:
            print(i)
        i += 1
        rock_garden = get_next_board(rock_garden)
        # print(rock_garden.__hash__())

        if rock_garden.__hash__() in board_state_hash:
            can_move = i - board_state_hash[rock_garden.__hash__()]
            i += can_move * ((end - i) // can_move)

        board_state_hash[rock_garden.__hash__()] = i

    total = 0
    height = rock_garden.height
    for rock in rock_garden.all_points():
        if rock_garden.value_at_point(rock) == "O":
            total += height - rock.y

    return total


print(part_a())
print(part_b())
