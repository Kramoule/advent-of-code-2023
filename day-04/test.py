from pathlib import Path

import pytest
from main import Card


def get_input_lines(input_path: str) -> list[str]:
    input_text = Path(input_path)
    with input_text.open("r") as f:
        return f.readlines()


def test_tokenize():
    line = "Card 2: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    card = Card.parse_card(line)
    expected_card = Card(
        id=2,
        winning_nb=[41, 48, 83, 86, 17],
        player_nb=[83, 86, 6, 31, 17, 9, 48, 53],
    )
    assert card == expected_card


def test_card_score():
    card = Card(
        id=3,
        winning_nb=[13, 32, 20, 16, 61],
        player_nb=[61, 30, 68, 82, 17, 32, 20, 19],
    )
    assert card.compute_score() == 4


def test_part1_example():
    lines = get_input_lines("example.txt")
    cards = []
    for l in lines:
        cards.append(Card.parse_card(l))

    scores = [c.compute_score() for c in cards]
    assert sum(scores) == 13


def test_part1_input():
    lines = get_input_lines("example.txt")
    cards = []
    for l in lines:
        cards.append(Card.parse_card(l))

    scores = [c.compute_score() for c in cards]
    assert sum(scores) == 13


def test_part2_example():
    lines = get_input_lines("example.txt")
    original_cards = []
    for l in lines:
        original_cards.append(Card.parse_card(l))

    scores = [c.compute_same_numbers() for c in original_cards]
    card_list = [1 for _ in original_cards]

    for i, c in enumerate(card_list):
        score = scores[i]
        for j in range(i + 1, i + 1 + score):
            if j >= len(card_list):
                break
            card_list[j] += c

    assert sum(card_list) == 30
