import glob
import json
from pathlib import Path
from pprint import pprint


def flatten(t):
    return [item for sublist in t for item in sublist]


def write_list(filename: str, l: list[str]):
    with open(filename, "w") as f:
        f.write("\n".join(l))


def read_json(filename: str):
    with open(filename, "r", encoding="utf8") as f:
        obj = json.load(f)
    return obj


def write_json(filename: str, obj):
    with open(filename, "w", encoding="utf8") as f:
        json.dump(obj, f, indent=2)


def main():
    github_result: list[dict] = read_json("github_result.json")
    github_result = [
        d for d in github_result if d["url"].startswith("https://github.com/")
    ]
    for d in github_result:
        d.pop("search", None)
        d["url"] = str(d["url"]).lower()
    github_result.sort(key=lambda d: d["url"])

    for i, d in enumerate(github_result):
        d["idx"] = i
    github_result = [{**d, "idx": i} for i, d in enumerate(github_result)]
    write_json("github_result_idx.json", github_result)

    print("Done.")


if __name__ == "__main__":
    main()
