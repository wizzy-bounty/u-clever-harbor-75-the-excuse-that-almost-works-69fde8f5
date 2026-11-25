import os


def resolve_output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    text = "My annual leave request for launch week was approved in January, I just forgot to tell you."
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
