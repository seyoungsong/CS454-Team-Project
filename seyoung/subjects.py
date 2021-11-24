import glob
from pathlib import Path


def flatten(t):
    return [item for sublist in t for item in sublist]


def write_list(filename: str, l: list[str]):
    with open(filename, "w") as f:
        f.write("\n".join(l))


def main():
    files = glob.glob("subjects/*.txt")
    texts = [Path(f).read_text() for f in files]
    lists = [s.strip().lower().split("\n") for s in texts]
    subjects = sorted(list(set(flatten(lists))))
    write_list("subjects.txt", subjects)
    print("Done.")


if __name__ == "__main__":
    main()
