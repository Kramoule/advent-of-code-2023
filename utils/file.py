from pathlib import Path


def get_input_lines(input_path: str) -> list[str]:
    input_text = Path(input_path)
    with input_text.open("r") as f:
        return f.readlines()
