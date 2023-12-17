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

input_str = get_input(13)
input_str = get_test_input(13)


def find_reflection(lake, prev):
    for i in range(1, len(lake)):
        if prev == i:
            continue
        left = lake[:i][::-1]
        right = lake[i:]

        if len(left) <= len(right):
            if left == right[: len(left)]:
                return i
        else:
            if right == left[: len(right)]:
                return i

    return None


def find_reflections(lake, prev_hor=None, prev_ver=None):
    rotated_lake = list(zip(*lake[::-1]))

    horizontal = find_reflection(lake, prev_hor)
    vertical = find_reflection(rotated_lake, prev_ver)

    return horizontal, vertical


def part_a():
    lake = []
    total = 0
    for line in input_str.splitlines():
        if line == "":
            horizontal, vertical = find_reflections(lake)
            if horizontal:
                total += horizontal * 100
            if vertical:
                total += vertical
            lake = []
        else:
            lake.append(list(line))

    horizontal, vertical = find_reflections(lake)
    if horizontal:
        total += horizontal * 100
    if vertical:
        total += vertical

    return total


def find_smudge(lake, prev_hor, prev_ver):
    for i in range(len(lake)):
        for j in range(len(lake[i])):
            lake[i][j] = "." if lake[i][j] == "#" else "#"

            new_hor, new_ver = find_reflections(lake, prev_hor, prev_ver)

            if new_hor or new_ver:
                return new_hor, new_ver

            lake[i][j] = "." if lake[i][j] == "#" else "#"

    return 0, 0


def part_b():
    lakes = []
    lake = []
    for line in input_str.splitlines():
        if line == "":
            horizontal, vertical = find_reflections(lake)
            lakes.append((lake, horizontal, vertical))
            lake = []
        else:
            lake.append(list(line))

    horizontal, vertical = find_reflections(lake)
    lakes.append((lake, horizontal, vertical))

    total = 0
    for lake in lakes:
        hor, ver = find_smudge(*lake)
        if hor:
            total += hor * 100
        if ver:
            total += ver
    return total


print(part_a())
print(part_b())
