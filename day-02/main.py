from dataclasses import dataclass
from pathlib import Path


@dataclass
class Game:
    id: int
    max_red: int = 0
    max_blue: int = 0
    max_green: int = 0

    def check_game_conditions(
        self, max_red: int, max_blue: int, max_green: int
    ) -> bool:
        return (
            self.max_red <= max_red
            and self.max_blue <= max_blue
            and self.max_green <= max_green
        )

    def set_power(self):
        return self.max_red * self.max_blue * self.max_green


def get_input_lines(input_path: str) -> list[str]:
    input_text = Path(input_path)
    with input_text.open("r") as f:
        return f.readlines()


def parse_line(line: str) -> Game:
    line = line.replace("Game", "")
    id = int(line.split(":")[0].strip())
    game = Game(id=id)
    results = line.split(":")[1].strip()
    sets = results.split(";")
    for s in sets:
        cubes = [c.strip() for c in s.split(",")]
        for c in cubes:
            num = int(c.split(" ")[0])
            color = c.split(" ")[1]
            match color:
                case "red":
                    game.max_red = max(num, game.max_red)
                case "blue":
                    game.max_blue = max(num, game.max_blue)
                case "green":
                    game.max_green = max(num, game.max_green)
    return game


if __name__ == "__main__":
    game = parse_line("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")
    print(game)
