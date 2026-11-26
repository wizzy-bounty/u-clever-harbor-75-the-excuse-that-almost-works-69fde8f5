import os
from pathlib import Path

LINE = "Boss, sorry, jury summons for Thursday, I called to swap days and the clerk just laughed."


def output_path():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / "entry.txt"


def main():
    output_path().write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
