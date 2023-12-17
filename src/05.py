from typing import Tuple

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

input_str = get_input(5)
# input_str = get_test_input(5)


def part_a():
    seeds = []
    seeds2 = []
    cur_map = {}

    lines = input_str.splitlines()
    for line in lines:
        if line == "":
            continue
        if line.startswith("seeds:"):
            seeds = line.split(":")[1].split()
            seeds = [int(x) for x in seeds]
            continue
        if line[0] in ["s", "f", "w", "l", "t", "h"]:
            if len(cur_map) == 0:
                continue
            for seed in seeds:
                found = False
                for k, v in cur_map.items():
                    if seed >= k[0] and seed < k[1]:
                        found = True
                        seeds2.append(seed + v)
                        break
                if not found:
                    seeds2.append(seed)
            seeds = seeds2
            seeds2 = []
            cur_map = {}
            continue

        i, o, r = [int(x) for x in line.split()]
        cur_map[(o, o + r)] = i - o

    for seed in seeds:
        found = False
        for k, v in cur_map.items():
            if seed >= k[0] and seed < k[1]:
                found = True
                seeds2.append(seed + v)
                break
        if not found:
            seeds2.append(seed)
    seeds = seeds2
    return min(seeds)


def convert_seed(seed: Tuple[int, int], cur_map) -> list[Tuple[int, int]]:
    # seed = (int, int) that represents a range
    for k, v in cur_map.items():
        if seed[0] >= k[0] and seed[0] < k[1]:
            if seed[1] <= k[1]:
                return [(seed[0] + v, seed[1] + v)]
            else:
                return [(seed[0] + v, k[1] + v)] + convert_seed(
                    (k[1], seed[1]), cur_map
                )
        if seed[1] <= k[1] and seed[1] > k[0]:
            return [(k[0] + v, seed[1] + v)] + convert_seed((seed[0], k[0]), cur_map)
    return [seed]


def convert_seeds(seeds, cur_map):
    # print(seeds, cur_map)
    seeds_return = []
    for seed in seeds:
        seeds_return += convert_seed(seed, cur_map)

    return seeds_return


def part_b():
    seeds = []
    cur_map = {}

    lines = input_str.splitlines()
    for line in lines:
        if line == "":
            continue
        if line.startswith("seeds:"):
            seeds_ish = line.split(":")[1].split()
            even = [int(x) for x in seeds_ish[::2]]
            odd = [int(x) for x in seeds_ish[1::2]]
            seeds_ish = list(zip(even, odd))
            seeds = [(x, x + y) for x, y in seeds_ish]
            continue
        if line[0] in ["s", "f", "w", "l", "t", "h"]:
            seeds = convert_seeds(seeds, cur_map)
            cur_map = {}
            continue

        i, o, r = [int(x) for x in line.split()]
        cur_map[(o, o + r)] = i - o

    seeds = convert_seeds(seeds, cur_map)
    return min([x[0] for x in seeds])


print(part_a())
print(part_b())  # Low: 12238241 High: 32956608
