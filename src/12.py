from functools import lru_cache

from utils.api import get_input, get_test_input

input_str = get_input(12)
# input_str = get_test_input(12)


@lru_cache(maxsize=None)
def solve(string, arangement, in_match=False) -> int:
    matches = sum(arangement)
    if not string:
        return not bool(matches)

    remaining = arangement[0] if arangement else 0

    match string[0]:
        case "#":
            if remaining <= 0:
                return 0
            return solve(string[1:], (remaining - 1, *arangement[1:]), True)
        case ".":
            if in_match and remaining != 0:
                return 0
            if remaining == 0:
                return solve(string[1:], arangement[1:], False)
            return solve(string[1:], arangement, False)
        case "?":
            return solve("#" + string[1:], arangement, in_match) + solve(
                "." + string[1:], arangement, in_match
            )
        case _:
            raise ValueError(f"Invalid char: {string[0]}")


def part_a():
    total = 0
    for line in input_str.splitlines():
        string, arangement = line.split()
        arangement = [int(x) for x in arangement.split(",")]
        total += solve(string, tuple(arangement))
    return total


def part_b():
    total = 0
    for line in input_str.splitlines():
        string, arangement = line.split()
        arangement = [int(x) for x in arangement.split(",")]
        string = string + ("?" + string) * 4
        arangement = arangement * 5
        total += solve(string, tuple(arangement))
    return total


print(part_a())
print(part_b())
