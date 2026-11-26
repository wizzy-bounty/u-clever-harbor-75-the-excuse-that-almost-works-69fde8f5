import os
from pathlib import Path

ENTRY_LINE = "Sorry, Mum fell; hospital's keeping her till Friday and Dad can't do stairs alone, so I need the week off."


def main():
    destination = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    destination.mkdir(parents=True, exist_ok=True)
    (destination / "entry.txt").write_bytes(ENTRY_LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
