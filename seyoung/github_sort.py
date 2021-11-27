import csv
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


def github_url_to_name(github_url: str):
    github_url = github_url.rstrip("/").lower()
    dev_name, repo_name = github_url.replace("https://github.com/", "").split("/")
    name = f"{dev_name}_{repo_name}"
    return name


def main():

    github_result_idx: list[dict] = read_json("github_result_idx.json")

    for d in github_result_idx:
        github_url = d["url"]
        name = github_url_to_name(github_url)
        csv_file = f"sloc/{name}.csv"

        with open(csv_file, "r", newline="", encoding="utf8") as f:
            reader = csv.reader(f)
            sloc = list(reader)

        d["sloc"] = int(sloc[1][2])

    github_result_idx.sort(key=lambda d: d["sloc"])
    github_result_idx = [{**d, "idx": i} for i, d in enumerate(github_result_idx)]

    write_json("github_result_sloc.json", github_result_idx)


if __name__ == "__main__":
    main()
