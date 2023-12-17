from typing import List, Tuple

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

input_str = get_input(16)
# input_str = get_test_input(16)


def handle_ray(ray: Tuple[Point, Point], grid) -> List[Tuple[Point, Point]]:
    if not grid.valid_location(ray[0]):
        return []

    match grid.value_at_point(ray[0]):
        case ".":
            return [(ray[0] + ray[1], ray[1])]
        case "|":
            match ray[1]:
                case Point(_, 0):
                    return [
                        (ray[0] + Point(0, 1), Point(0, 1)),
                        (ray[0] + Point(0, -1), Point(0, -1)),
                    ]
                case _:
                    return [(ray[0] + ray[1], ray[1])]
        case "-":
            match ray[1]:
                case Point(0, _):
                    return [
                        (ray[0] + Point(1, 0), Point(1, 0)),
                        (ray[0] + Point(-1, 0), Point(-1, 0)),
                    ]
                case _:
                    return [(ray[0] + ray[1], ray[1])]
        case "/":
            new_dir = Point(-ray[1].y, -ray[1].x)
            return [(ray[0] + new_dir, new_dir)]
        case "\\":
            new_dir = Point(ray[1].y, ray[1].x)
            return [(ray[0] + new_dir, new_dir)]

    raise ValueError(f"Unknown value: {grid.value_at_point(ray[0])}")


def get_energized(start, grid):
    energized = set()
    rays = [start]
    seen_rays = set()
    while rays:
        ray = rays.pop()
        if not grid.valid_location(ray[0]) or ray in seen_rays:
            continue
        seen_rays.add(ray)
        energized.add(ray[0].as_tuple())
        rays.extend(handle_ray(ray, grid))
    return len(energized)


def part_a():
    grid = Grid([list(x) for x in input_str.splitlines()])
    return get_energized((Point(0, 0), Point(1, 0)), grid)


def part_b():
    grid = Grid([list(x) for x in input_str.splitlines()])

    left_edges = [(Point(0, y), Point(1, 0)) for y in range(grid.height)]
    top_edges = [(Point(x, 0), Point(0, 1)) for x in range(grid.width)]
    right_edges = [(Point(grid.width - 1, y), Point(-1, 0)) for y in range(grid.height)]
    bottom_edges = [
        (Point(x, grid.height - 1), Point(0, -1)) for x in range(grid.width)
    ]
    all_starts = left_edges + top_edges + right_edges + bottom_edges

    return max(get_energized(start, grid) for start in all_starts)


print(part_a())
print(part_b())
