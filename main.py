import os
from pathlib import Path

TEXT = "Sorry, IT took my laptop in Monday's refresh; the replacement is imaged Friday, so I can't log in."


def resolve_output_dir() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


def main() -> None:
    output_dir = resolve_output_dir()
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
