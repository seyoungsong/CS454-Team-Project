import argparse
import glob
import json
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from pprint import pprint
from subprocess import CompletedProcess
from xml.etree.ElementTree import Element


def read_json(filename: str):
    with open(filename, "r", encoding="utf8") as f:
        obj = json.load(f)
    return obj


def flatten(t):
    return [item for sublist in t for item in sublist]


def write_list(filename: str, l: list[str]):
    with open(filename, "w", encoding="utf8") as f:
        for s in l:
            f.write(f"{s}\n")


def main():
    github_result_sloc = read_json("github_result_sloc.json")
    ng = len(github_result_sloc)
    shebang = [
        # Shebang
        "#!/bin/sh"
    ]
    commands = [f"python main.py --idx {i}; clear; zsh run.sh" for i in range(ng)]
    n = len(commands)
    commands_echos = flatten(
        [(f'echo "[all][{i+1}/{n}] {s}"', s) for i, s in enumerate(commands)]
    )
    script_main = shebang + commands_echos
    write_list("all.sh", script_main)

    print("Done.")


if __name__ == "__main__":
    main()
