import timeit

import numpy as np

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

input_str = get_input(8)
# input_str = get_test_input(8)


class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right


def part_a():
    node_dict = {}

    sequence, _, *nodes = input_str.splitlines()
    end = "ZZZ"

    for node in nodes:
        key, value = node.split(" = ")
        value = value[1:-1]
        left, right = value.split(", ")
        node_dict[key] = Node(key, left, right)

    i = 0
    cur_node = node_dict["AAA"]
    while True:
        move = sequence[i % len(sequence)]
        i += 1
        if move == "R":
            cur_node = node_dict[cur_node.right]
        else:
            cur_node = node_dict[cur_node.left]
        if cur_node.key == end:
            break
    return i


def part_b():
    node_dict = {}
    sequence, _, *nodes = input_str.splitlines()
    for node in nodes:
        key, value = node.split(" = ")
        value = value[1:-1]
        left, right = value.split(", ")
        node_dict[key] = Node(key, left, right)

    starttime = timeit.default_timer()
    i = 0
    start_nodes = [node for node in node_dict if node.endswith("A")]
    loop_nodes = [-1 for _ in start_nodes]
    cur_nodes = [node for node in node_dict if node.endswith("A")]
    while True:
        move = sequence[i % len(sequence)]
        i += 1
        if move == "R":
            cur_nodes = [node_dict[node].right for node in cur_nodes]
        else:
            cur_nodes = [node_dict[node].left for node in cur_nodes]

        if sum([node.endswith("Z") for node in cur_nodes]) != 0:
            for j, node in enumerate(cur_nodes):
                if node.endswith("Z") and loop_nodes[j] == -1:
                    loop_nodes[j] = i

        if all([loop_node != -1 for loop_node in loop_nodes]):
            return np.lcm.reduce(loop_nodes)


print(part_a())
print(part_b())
