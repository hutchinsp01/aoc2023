import re

from utils.api import get_input, get_test_input

input_str = get_input(1)
# input_str = get_test_input(1)


def part_a():
    lines = input_str.splitlines()
    num = 0
    for line in lines:
        numbers = re.findall(r"\d", line)
        num += int(numbers[0] + numbers[-1])
    return num


def part_b():
    lines = input_str.splitlines()
    num = 0
    for line in lines:
        line = line.replace("one", "on1e")
        line = line.replace("two", "tw2o")
        line = line.replace("three", "thr3ee")
        line = line.replace("four", "fo4ur")
        line = line.replace("five", "fi5ve")
        line = line.replace("six", "si6x")
        line = line.replace("seven", "sev7en")
        line = line.replace("eight", "eig8ht")
        line = line.replace("nine", "ni9ne")

        numbers = re.findall(r"\d", line)
        num += int(numbers[0] + numbers[-1])

    return num


print(part_a())
print(part_b())
