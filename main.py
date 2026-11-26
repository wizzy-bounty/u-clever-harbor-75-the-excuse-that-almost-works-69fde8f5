import os

ENTRY_TEXT = "Your rota gives me launch week off, and your own swap deadline passed Monday."
OUTPUT_NAME = "entry.txt"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, OUTPUT_NAME), "w", encoding="utf-8") as fh:
        fh.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
