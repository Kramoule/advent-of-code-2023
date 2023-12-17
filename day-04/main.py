from dataclasses import dataclass
from typing import Self


@dataclass
class Card:
    id: int
    winning_nb: list[int]
    player_nb: list[int]

    def compute_same_numbers(self):
        if not self.winning_nb:
            self.score = -1
        set_player = set(self.player_nb)
        set_winning = set(self.winning_nb)
        matches = len(set_player.intersection(set_winning))
        return matches

    def compute_score(self):
        matches = self.compute_same_numbers()
        return 0 if not matches else 2 ** (matches - 1)

    @staticmethod
    def parse_card(line: str) -> Self:
        card = line.split(":")[0]
        id = int(card.replace("Card ", ""))
        numbers = line.split(":")[1].split("|")
        winning_nb = numbers[0].strip().split()
        player_nb = numbers[1].strip().split()
        return Card(
            id=id,
            player_nb=[int(nb) for nb in player_nb],
            winning_nb=[int(nb) for nb in winning_nb],
        )
