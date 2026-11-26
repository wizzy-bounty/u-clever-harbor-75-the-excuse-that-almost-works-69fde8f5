import os

ENTRY = "My bank froze my salary account after a fraud alert; I must verify ID in person before tonight's payroll."


def entry_text():
    return ENTRY


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as output_file:
        output_file.write(entry_text())


if __name__ == "__main__":
    main()
