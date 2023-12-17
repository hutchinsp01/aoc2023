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

input_str = get_input(7)
# input_str = get_test_input(7)

CARDORDER = "23456789TJQKA"
JOKERCARDORDER = "J23456789TQKA"


class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid

    def is_5_of_a_kind(self):
        return len(set(self.cards)) == 1

    def is_4_of_a_kind(self):
        if len(set(self.cards)) == 2:
            return (
                self.cards.count(self.cards[0]) == 4
                or self.cards.count(self.cards[1]) == 4
            )

    def is_3_of_a_kind(self):
        sets = set(self.cards)
        if not len(sets) == 3:
            return False

        for card in sets:
            if self.cards.count(card) == 3:
                return True

    def is_full_house(self):
        sets = set(self.cards)
        if not len(sets) == 2:
            return False

        for card in sets:
            if self.cards.count(card) == 3:
                return True

    def is_2_pair(self):
        sets = set(self.cards)
        if not len(sets) == 3:
            return False

        pairs = 0
        for card in sets:
            if self.cards.count(card) == 2:
                pairs += 1

        return pairs == 2

    def is_1_pair(self):
        sets = set(self.cards)
        if not len(sets) == 4:
            return False

        for card in sets:
            if self.cards.count(card) == 2:
                return True

    def is_high_card(self):
        return len(set(self.cards)) == 5

    def get_value(self):
        if self.is_5_of_a_kind():
            return 9
        if self.is_4_of_a_kind():
            return 8
        if self.is_full_house():
            return 7
        if self.is_3_of_a_kind():
            return 6
        if self.is_2_pair():
            return 5
        if self.is_1_pair():
            return 4
        if self.is_high_card():
            return 3

    def tie_breaker(self, other):
        if self.cards[0] != other.cards[0]:
            return CARDORDER.index(self.cards[0]) > CARDORDER.index(other.cards[0])
        if self.cards[1] != other.cards[1]:
            return CARDORDER.index(self.cards[1]) > CARDORDER.index(other.cards[1])
        if self.cards[2] != other.cards[2]:
            return CARDORDER.index(self.cards[2]) > CARDORDER.index(other.cards[2])
        if self.cards[3] != other.cards[3]:
            return CARDORDER.index(self.cards[3]) > CARDORDER.index(other.cards[3])
        if self.cards[4] != other.cards[4]:
            return CARDORDER.index(self.cards[4]) > CARDORDER.index(other.cards[4])

    def __gt__(self, other):
        self_value = self.get_value()
        other_value = other.get_value()
        if self_value == other_value:
            return self.tie_breaker(other)
        return self_value > other_value


class JokerHand(Hand):
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.joker_count = cards.count("J")
        self.max_other_count = max(
            [
                cards.count("2"),
                cards.count("3"),
                cards.count("4"),
                cards.count("5"),
                cards.count("6"),
                cards.count("7"),
                cards.count("8"),
                cards.count("9"),
                cards.count("T"),
                cards.count("Q"),
                cards.count("K"),
                cards.count("A"),
            ]
        )
        self.card_counts = [
            cards.count("2"),
            cards.count("3"),
            cards.count("4"),
            cards.count("5"),
            cards.count("6"),
            cards.count("7"),
            cards.count("8"),
            cards.count("9"),
            cards.count("T"),
            cards.count("Q"),
            cards.count("K"),
            cards.count("A"),
        ]

    def is_5_of_a_kind(self):
        normal_5 = super().is_5_of_a_kind()
        if normal_5:
            return True

        if self.joker_count + self.max_other_count >= 5:
            return True

        return False

    def is_4_of_a_kind(self):
        normal_4 = super().is_4_of_a_kind()
        if normal_4:
            return True

        if self.joker_count + self.max_other_count >= 4:
            return True

        return False

    def is_3_of_a_kind(self):
        normal_3 = super().is_3_of_a_kind()
        if normal_3:
            return True

        if self.joker_count + self.max_other_count >= 3:
            return True

        return False

    def is_2_pair(self):
        normal_2 = super().is_2_pair()
        if normal_2:
            print(self.cards)
            return True

        if self.joker_count == 1:
            sorted_counts = sorted(self.card_counts, reverse=True)
            if sorted_counts[0] >= 2 and sorted_counts[1] >= 1:
                print(self.cards)
                return True

        if self.joker_count == 2:
            sorted_counts = sorted(self.card_counts, reverse=True)
            if sorted_counts[0] >= 2 and sorted_counts[1] >= 0:
                print(self.cards)
                return True

            if sorted_counts[0] >= 1 and sorted_counts[1] >= 1:
                print(self.cards)
                return True

        if self.joker_count == 3:
            sorted_counts = sorted(self.card_counts, reverse=True)
            if sorted_counts[0] >= 1 and sorted_counts[1] >= 0:
                print(self.cards)
                return True

        if self.joker_count == 4:
            print(self.cards)
            return True

        return False

    def is_1_pair(self):
        normal_1 = super().is_1_pair()
        if normal_1:
            return True

        if self.joker_count == 1:
            return True

        if self.joker_count == 2:
            return True

        return False

    def is_full_house(self):
        normal_full = super().is_full_house()
        if normal_full:
            return True

        if self.joker_count == 1:
            sorted_counts = sorted(self.card_counts, reverse=True)
            if sorted_counts[1] >= 2:
                return True

        if self.joker_count == 2:
            sorted_counts = sorted(self.card_counts, reverse=True)
            if sum(sorted_counts[:2]) >= 3 and sorted_counts[2] >= 1:
                return True

        if self.joker_count == 3:
            sorted_counts = sorted(self.card_counts, reverse=True)
            if sum(sorted_counts[:2]) >= 2 and sorted_counts[2] >= 0:
                return True

        if self.joker_count >= 4:
            return True

        return False

    def tie_breaker(self, other):
        if self.cards[0] != other.cards[0]:
            return JOKERCARDORDER.index(self.cards[0]) > JOKERCARDORDER.index(
                other.cards[0]
            )
        if self.cards[1] != other.cards[1]:
            return JOKERCARDORDER.index(self.cards[1]) > JOKERCARDORDER.index(
                other.cards[1]
            )
        if self.cards[2] != other.cards[2]:
            return JOKERCARDORDER.index(self.cards[2]) > JOKERCARDORDER.index(
                other.cards[2]
            )
        if self.cards[3] != other.cards[3]:
            return JOKERCARDORDER.index(self.cards[3]) > JOKERCARDORDER.index(
                other.cards[3]
            )
        if self.cards[4] != other.cards[4]:
            return JOKERCARDORDER.index(self.cards[4]) > JOKERCARDORDER.index(
                other.cards[4]
            )


def part_a():
    hands = []
    for line in input_str.splitlines():
        cards, bid = line.split()
        bid = int(bid)
        hands.append(Hand(cards, bid))

    hands = sorted(hands)
    total = 0
    for i, hand in enumerate(hands):
        total += hand.bid * (i + 1)

    return total


def part_b():
    hands = []
    for line in input_str.splitlines():
        cards, bid = line.split()
        bid = int(bid)
        hands.append(JokerHand(cards, bid))

    hands = sorted(hands)
    total = 0
    for i, hand in enumerate(hands):
        total += hand.bid * (i + 1)

    return total


print(part_a())
print(part_b())
