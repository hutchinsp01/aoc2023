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

input_str = get_input(4)
# input_str = get_test_input(4)


def part_a():
    track_arr = []
    tot = 0
    for card in input_str.splitlines():
        score = 0
        nums = card.split(": ")[1]
        winning_nums, my_nums = nums.split(" | ")
        my_nums = my_nums.split(" ")
        winning_nums = winning_nums.split(" ")

        # remove " "
        my_nums = list(filter(lambda x: x != "", my_nums))
        winning_nums = list(filter(lambda x: x != "", winning_nums))
        track = 0
        for num in my_nums:
            if num in winning_nums:
                track += 1
                if score == 0:
                    score = 1
                else:
                    score *= 2
                continue
        track_arr.append(track)
        tot += score

    print(track_arr)
    return tot


class Card:
    def __init__(self, i, my_nums, winning_nums):
        self.i = i
        self.my_nums = my_nums
        self.winning_nums = winning_nums


def part_b():
    cards = {}
    for i, card in enumerate(input_str.splitlines()):
        nums = card.split(": ")[1]
        winning_nums, my_nums = nums.split(" | ")
        my_nums = my_nums.split(" ")
        winning_nums = winning_nums.split(" ")

        my_nums = list(filter(lambda x: x != "", my_nums))
        winning_nums = list(filter(lambda x: x != "", winning_nums))

        card = Card(i, my_nums, winning_nums)

        cards[i] = card

    tot = 0
    cards_to_check = []
    for i, card in cards.items():
        tot += 1
        score = 0
        for num in card.my_nums:
            if num in card.winning_nums:
                score += 1
                continue

        card_num = i
        if score > 0:
            while score > 0:
                if card_num + score < len(cards):
                    cards_to_check.append(cards[card_num + score])
                    score -= 1

    while cards_to_check:
        tot += 1
        card = cards_to_check.pop()
        score = 0
        for num in card.my_nums:
            if num in card.winning_nums:
                score += 1
                continue

        card_num = card.i
        if score > 0:
            while score > 0:
                if card_num + score < len(cards):
                    cards_to_check.append(cards[card_num + score])
                    score -= 1

    return tot


print(part_a())
print(part_b())
