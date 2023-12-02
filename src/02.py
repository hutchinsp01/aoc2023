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

input_str = get_input(2)
# input_str = get_test_input(2)


def part_a():
    tot = 0

    for game in input_str.splitlines():
        possible = True
        game_num, rest = game.split(":")
        game_num = game_num.strip().replace("Game ", "")
        rest = rest.strip()
        rounds = rest.split(";")
        for round in rounds:
            round = round.strip()
            for select in round.split(","):
                count, colour = select.strip().split(" ")
                if colour == "red" and int(count) > 12:
                    possible = False
                    break
                elif colour == "green" and int(count) > 13:
                    possible = False
                    break
                elif colour == "blue" and int(count) > 14:
                    possible = False
                    break

        if possible:
            tot += int(game_num)

    return tot


def part_b():
    tot = 0
    for game in input_str.splitlines():
        red_max = green_max = blue_max = 0

        # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        game_num, rest = game.split(":")
        rest = rest.strip()
        rounds = rest.split(";")
        for round in rounds:
            round = round.strip()
            for select in round.split(","):
                count, colour = select.strip().split(" ")
                count = int(count)
                if colour == "red" and count > red_max:
                    red_max = count
                elif colour == "green" and count > green_max:
                    green_max = count
                elif colour == "blue" and count > blue_max:
                    blue_max = count

        tot += red_max * green_max * blue_max

    return tot


print(part_a())
print(part_b())
