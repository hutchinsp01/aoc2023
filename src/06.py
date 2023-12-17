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

input_str = get_input(6)
input_str = get_test_input(6)


def part_a():
    times = [int(x) for x in input_str.splitlines()[0].split(":")[1].split()]
    distances = [int(x) for x in input_str.splitlines()[1].split(":")[1].split()]
    races = zip(times, distances)

    score = 1
    for race in races:
        race_score = 0
        time, distance = race
        for i in range(time):
            if i * (time - i) > distance:
                race_score += 1
        score *= race_score

    return score


def part_b():
    times = [x for x in input_str.splitlines()[0].split(":")[1].split()]
    distances = [x for x in input_str.splitlines()[1].split(":")[1].split()]

    time = int("".join(times))
    distance = int("".join(distances))

    race_score = 0
    for i in range(time):
        if i * (time - i) > distance:
            race_score += 1

    return race_score


print(part_a())
print(part_b())
