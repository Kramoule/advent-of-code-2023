from pathlib import Path

import main
import pytest


def get_input_lines(input_path: str) -> list[str]:
    input_text = Path(input_path)
    with input_text.open("r") as f:
        return f.readlines()


def test_single_line():
    game = main.parse_line("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")
    assert game.id == 5
    assert game.max_red == 6
    assert game.max_blue == 2
    assert game.max_green == 3


def test_part1_example():
    lines = get_input_lines("example.txt")
    games = []
    for line in lines:
        game = main.parse_line(line)
        if game.check_game_conditions(max_red=12, max_green=13, max_blue=14):
            games.append(game)
    assert sum([g.id for g in games]) == 8


def test_part1():
    lines = get_input_lines("inpexampleut.txt")
    games = []
    for line in lines:
        game = main.parse_line(line)
        if game.check_game_conditions(max_red=12, max_green=13, max_blue=14):
            games.append(game)
    print(sum([g.id for g in games]))


def test_part2_example():
    lines = get_input_lines("example.txt")
    games = []
    for line in lines:
        game = main.parse_line(line)
        games.append(game)
    assert sum([g.set_power() for g in games]) == 2286
