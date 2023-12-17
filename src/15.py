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

input_str = get_input(15)
# input_str = get_test_input(15)


def part_a():
    total = 0
    for code in input_str.split(","):
        code_total = 0
        for char in code:
            code_total = ((code_total + ord(char)) * 17) % 256
        total += code_total

    return total


def part_b():
    lens_box = [list() for _ in range(256)]
    for code in input_str.split(","):
        action = None
        action_type = None
        code_total = 0
        if "=" in code:
            action = code[-2:]
            action_type = "="
            code = code[:-2]

        if "-" in code:
            action = code[-1]
            action_type = "-"
            code = code[:-1]

        code_total = 0
        for char in code:
            code_total += ord(char)
            code_total *= 17
            code_total %= 256

        if action_type == "=":
            duplicate_lens_index = None
            for i, lens in enumerate(lens_box[code_total]):
                if lens[0] == code:
                    duplicate_lens_index = i
                    break

            if duplicate_lens_index is not None:
                lens_box[code_total][duplicate_lens_index] = (code, action[1])
            else:
                lens_box[code_total].append((code, action[1]))

        if action_type == "-":
            for i, lens in enumerate(lens_box[code_total]):
                if lens[0] == code:
                    lens_box[code_total].pop(i)
                    break

    total = 0
    for box_num, lens in enumerate(lens_box):
        for i, (code, focal) in enumerate(lens):
            total += (box_num + 1) * (i + 1) * int(focal)
    return total


print(part_a())
print(part_b())
