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


github_result_idx = read_json("github_result_idx.json")
urls = [d["url"] for d in github_result_idx]
shebang = [
    # Shebang
    "#!/bin/sh"
]
commands = [
    f"rm -rf repo && git clone --depth 1 --recursive {github_url} repo && sloc --format csv repo > sloc/{github_url_to_name(github_url)}.csv"
    for github_url in urls
]
n = len(commands)
commands_echos = flatten(
    [(f'echo "[sort][{i+1}/{n}] {s}"', s) for i, s in enumerate(commands)]
)
script_main = shebang + commands_echos
write_list("batch_sloc.sh", script_main)

print("Done.")
