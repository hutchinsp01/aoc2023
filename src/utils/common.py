import operator
from dataclasses import asdict, dataclass
from enum import Enum
from functools import cache

#################################
# POINTS,
#################################


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def yield_neighbors(self, include_diagonals=False, include_self=False):
        yield self + Point(1, 0)
        yield self + Point(-1, 0)
        yield self + Point(0, 1)
        yield self + Point(0, -1)

        if include_diagonals:
            yield self + Point(1, 1)
            yield self + Point(1, -1)
            yield self + Point(-1, 1)
            yield self + Point(-1, -1)

        if include_self:
            yield self

    def neighbours(self, include_diagonals=False, include_self=False):
        return list(self.yield_neighbors(include_diagonals, include_self))

    def manhattan_distance(self, to: "Point"):
        return abs(self.x - to.x) + abs(self.y - to.y)


class Vectors(Enum):
    """Enumeration of 8 directions.
    Note: y axis increments in the North direction, i.e. N = (0, 1)"""

    N = (0, 1)
    NE = (1, 1)
    E = (1, 0)
    SE = (1, -1)
    S = (0, -1)
    SW = (-1, -1)
    W = (-1, 0)
    NW = (-1, 1)

    @property
    def y_inverted(self):
        """Return vector, but with y-axis inverted. I.e. N = (0, -1)"""
        x, y = self.value
        return (x, -y)


class VectorDicts:
    """Contains constants for Vectors"""

    ARROWS = {
        "^": Vectors.N.value,
        ">": Vectors.E.value,
        "v": Vectors.S.value,
        "<": Vectors.W.value,
    }

    DIRS = {
        "U": Vectors.N.value,
        "R": Vectors.E.value,
        "D": Vectors.S.value,
        "L": Vectors.W.value,
    }

    NINE_BOX: dict[str, tuple[int, int]] = {
        # x, y vector for adjacent locations
        "tr": (1, 1),
        "mr": (1, 0),
        "br": (1, -1),
        "bm": (0, -1),
        "bl": (-1, -1),
        "ml": (-1, 0),
        "tl": (-1, 1),
        "tm": (0, 1),
    }


class Grid:
    """2D grid of point values."""

    def __init__(self, grid_array: list) -> None:
        self._array = grid_array
        self._width = len(self._array[0])
        self._height = len(self._array)

    def value_at_point(self, point: Point) -> int:
        """The value at this point"""
        return self._array[point.y][point.x]

    def set_value_at_point(self, point: Point, value: int):
        self._array[point.y][point.x] = value

    def valid_location(self, point: Point) -> bool:
        """Check if a location is within the grid"""
        if 0 <= point.x < self._width and 0 <= point.y < self._height:
            return True

        return False

    @property
    def width(self):
        """Array width (cols)"""
        return self._width

    @property
    def height(self):
        """Array height (rows)"""
        return self._height

    def all_points(self) -> list[Point]:
        points = [Point(x, y) for x in range(self.width) for y in range(self.height)]
        return points

    def rows_as_str(self):
        """Return the grid"""
        return ["".join(str(char) for char in row) for row in self._array]

    def cols_as_str(self):
        """Render columns as str. Returns: list of str"""
        cols_list = list(zip(*self._array))
        return ["".join(str(char) for char in col) for col in cols_list]

    def __repr__(self) -> str:
        return f"Grid(size={self.width}*{self.height})"

    def __str__(self) -> str:
        return "\n".join("".join(map(str, row)) for row in self._array)


def binary_search(target, low: int, high: int, func, *func_args, reverse_search=False):
    """Generic binary search function that takes a target to find,
    low and high values to start with, and a function to run, plus its args.
    Implicitly returns None if the search is exceeded."""

    res = None  # just set it to something that isn't the target
    candidate = 0  # initialise; we'll set it to the mid point in a second

    while low < high:  # search exceeded
        candidate = int((low + high) // 2)  # pick mid-point of our low and high
        res = func(candidate, *func_args)  # run our function, whatever it is
        if res == target:
            return candidate  # solution found

        comp = operator.lt if not reverse_search else operator.gt
        if comp(res, target):
            low = candidate
        else:
            high = candidate


@cache
def get_factors(num: int) -> set[int]:
    """Gets the factors for a given number. Returns a set[int] of factors.
    # E.g. when num=8, factors will be 1, 2, 4, 8"""
    factors = set()

    # Iterate from 1 to sqrt of 8,
    # since a larger factor of num must be a multiple of a smaller factor already checked
    for i in range(1, int(num**0.5) + 1):  # e.g. with num=8, this is range(1, 3)
        if (
            num % i == 0
        ):  # if it is a factor, then dividing num by it will yield no remainder
            factors.add(i)  # e.g. 1, 2
            factors.add(num // i)  # i.e. 8//1 = 8, 8//2 = 4

    return factors


def to_base_n(number: int, base: int):
    """Convert any integer number into a base-n string representation of that number.
    E.g. to_base_n(38, 5) = 123

    Args:
        number (int): The number to convert
        base (int): The base to apply

    Returns:
        [str]: The string representation of the number
    """
    ret_str = ""
    curr_num = number
    while curr_num:
        ret_str = str(curr_num % base) + ret_str
        curr_num //= base

    return ret_str if number > 0 else "0"
