from pathlib import Path

import pytest
from main import Board


@pytest.fixture
def example_board():
    lines = get_input_lines("example.txt")
    return Board(lines)


def get_input_lines(input_path: str) -> list[str]:
    input_text = Path(input_path)
    with input_text.open("r") as f:
        return f.readlines()


def test_tokenize():
    line = "..+.58."
    assert Board.tokenize_line(line) == [".", ".", "+", ".", "5", "8", "."]


def test_make_2d_array():
    lines = get_input_lines("example.txt")
    array = Board.make_2d_array(lines)
    assert len(array) == 10
    for col in array:
        assert len(col) == 10


def test_build_number(example_board):
    board = example_board
    assert board.build_number(6, 2) == "592"
    assert board.build_number(0, 0) == "467"
    assert board.build_number(0, 5) == "114"
    assert board.build_number(9, 1) == "664"


def test_has_neighbour(example_board):
    board = example_board
    assert board.has_neighbour_symbol(0, 0) is False
    assert board.has_neighbour_symbol(0, 2) is True
    assert board.has_neighbour_symbol(0, 9) is False


def test_walk_array(example_board):
    board = example_board
    assert board.walk_array() == 4361


def test_compute_gears(example_board):
    example_board.walk_array()
    assert example_board.compute_gears() == 467835
