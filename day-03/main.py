from dataclasses import dataclass
from typing import Self

Array2D = list[list[str]]


class Board:
    array: Array2D
    gears: dict[(int, int), list[int]] = {}

    def __init__(self, array):
        if isinstance(array, list):
            self.array = self.make_2d_array(array)
        else:
            self.array = array

    @staticmethod
    def make_2d_array(lines: list[str]) -> Array2D:
        return [Board.tokenize_line(line) for line in lines]

    @staticmethod
    def is_symbol(value: str) -> bool:
        """A symbol in this case is anything other than a digit or a dot"""
        return not (value.isdigit() or value == ".")

    @staticmethod
    def tokenize_line(line: str) -> list[str]:
        return list(line.strip())

    def build_number(self, row: int, col: int) -> str:
        num_str = self.array[row][col]
        if not num_str.isdigit():
            return ""
        i = 1
        while (next_str := self.array[row][col + i]).isdigit():
            # print(next_str)
            num_str += next_str
            i += 1
            if col + i >= len(self.array[row]):
                break
        return num_str

    def has_neighbour_symbol(self, row: int, col: int) -> tuple[tuple, bool]:
        gear_pos = None
        for y in [-1, 0, 1]:
            for x in [-1, 0, 1]:
                if (
                    (x == y and x == 0)
                    or len(self.array) == row + y
                    or len(self.array[row]) == col + x
                ):
                    continue
                check_car = self.array[row + y][col + x]
                if Board.is_symbol(check_car):
                    if check_car == "*":
                        gear_pos = (row + y, col + x)
                    return gear_pos, True
        return gear_pos, False

    def walk_array(self) -> int:
        res = []
        x = 0
        print("")
        while x < len(self.array):
            y = 0
            while y < len(self.array[x]):
                value = self.array[x][y]
                number = self.build_number(x, y)
                if number:
                    next_to_symbol = False
                    for i in range(len(number)):
                        gear_pos, next_to_symbol = self.has_neighbour_symbol(x, y + i)
                        if gear_pos:
                            self.gears.setdefault(gear_pos, []).append(int(number))
                        if next_to_symbol:
                            break
                    if next_to_symbol:
                        res.append(int(number))
                    y += len(number) - 1
                y += 1
            x += 1
        print(res)
        return sum(res)

    def compute_gears(self):
        total = 0
        gears_values = self.gears.values()
        for l in gears_values:
            if len(l) != 2:
                continue
            gear_ratio = l[0] * l[1]
            total += gear_ratio
        return total
