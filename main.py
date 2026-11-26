import os

TEXT = "Sorry, fridge delivery is 1-5 today and they charge £40 to rebook if nobody answers."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "wb") as entry_file:
        entry_file.write(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
