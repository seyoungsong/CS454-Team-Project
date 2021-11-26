import glob
import json
from pathlib import Path


def flatten(t):
    return [item for sublist in t for item in sublist]


def write_list(filename: str, l: list[str]):
    with open(filename, "w") as f:
        f.write("\n".join(l))


def write_json(filename: str, obj):
    with open(filename, "w", encoding="utf8") as f:
        json.dump(obj, f, indent=2)


def github_search_url(repo_name: str):
    url = f"https://github.com/search?l=Java&o=desc&q={repo_name}&s=stars&type=Repositories"
    return url


def main():
    text = Path("subjects.txt").read_text()
    subjects = text.strip().split("\n")
    subjects.sort()
    search = [
        {"subject": s, "search": github_search_url(s), "url": ""} for s in subjects
    ]
    write_json("github_search.json", search)
    print("Done.")


if __name__ == "__main__":
    main()
