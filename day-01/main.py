from pathlib import Path

numbers_str = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def get_input_lines(input_path: str) -> list[str]:
    input_text = Path(input_path)
    with input_text.open("r") as f:
        return f.readlines()


def part1() -> int:
    total = 0
    lines = get_input_lines("example.txt")
    for i, line in enumerate(lines, start=1):
        numbers = [n for n in line if n.isdigit()]
        number = numbers[0] + numbers[-1]
        total += int(number)
        print(f"{i} value: {number}, total: {total}")

    return total


def part2() -> int:
    total = 0
    lines = get_input_lines("example.txt")

    left_num = right_num = ""
    for j, line in enumerate(lines, start=1):
        end = len(line)
        # left check
        for i in range(0, len(line)):
            c = line[i]
            for n, str_n in enumerate(numbers_str, start=1):
                if c.isdigit():
                    left_num = c
                    break
                if line.find(str_n, i, i + len(str_n) + 1) != -1:
                    left_num = str(n)
                    break
            else:
                continue
            break

        # right check
        for i in range(0, len(line)):
            index = len(line) - i - 1
            c = line[index]
            for n, str_n in enumerate(numbers_str, start=1):
                if c.isdigit():
                    right_num = c
                    break
                if line.find(str_n, index) != -1:
                    right_num = str(n)
                    break
            else:
                continue
            break
        number = int(left_num + right_num)
        total += number
        print(f"{j} value: {number}, total: {total}")
    return total


if __name__ == "__main__":
    print(part2())
