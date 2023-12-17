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

input_str = get_input(9)
# input_str = get_test_input(9)


def part_a():
    total = 0
    for line in input_str.splitlines():
        patterns = [[int(x) for x in line.split()]]

        while not all(x == 0 for x in patterns[-1]):
            new_pattern = []
            for i in range(len(patterns[-1]) - 1):
                new_pattern.append(patterns[-1][i + 1] - patterns[-1][i])
            patterns.append(new_pattern)

        base = diff = 0
        for pattern in patterns[::-1]:
            base = pattern[-1]
            pattern.append(base + diff)
            diff = pattern[-1]
        total += patterns[0][-1]

    return total


def part_b():
    total = 0
    for line in input_str.splitlines():
        patterns = [[int(x) for x in line.split()]]

        while not all(x == 0 for x in patterns[-1]):
            new_pattern = []
            for i in range(len(patterns[-1]) - 1):
                new_pattern.append(patterns[-1][i + 1] - patterns[-1][i])
            patterns.append(new_pattern)

        base = diff = 0
        for pattern in patterns[::-1]:
            base = pattern[0]
            pattern.insert(0, base - diff)
            diff = pattern[0]
        total += patterns[0][0]

    return total


print(part_a())
print(part_b())
