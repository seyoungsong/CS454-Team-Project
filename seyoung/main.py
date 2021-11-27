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


def main(idx: int):
    # idx = 22
    github_url = [
        d["url"] for d in read_json("github_result_sloc.json") if d["idx"] == idx
    ][0]
    github_url = github_url.rstrip("/").lower()
    dev_name, repo_name = github_url.replace("https://github.com/", "").split("/")
    logname = f"data/{dev_name}_{repo_name}.log"
    shebang = [
        # Shebang
        "#!/bin/sh"
    ]
    commands = [
        # delete repo dir if it exists
        "rm -rf repo clover clover.xml git.log tests.sh",
        # clone project from github
        f"git clone --depth 1 --recursive {github_url} repo",
        # check dependencies
        "java -version",
        "mvn --version",
        "git --version",
        # save git data (github url, timestamp, hash)
        "git --git-dir repo/.git config --get remote.origin.url > git.log",
        "git --git-dir repo/.git log -n 1 --format=%ct%n%H >> git.log",
        # test maven
        "mvn --file repo/pom.xml --fail-never clean test",
        # run clover
        "mvn --file repo/pom.xml --fail-never -Dmaven.clover.generateHtml=false clean clover:setup test clover:aggregate clover:clover",
        # copy clover.xml to cwd
        "cp repo/target/site/clover/clover.xml ./clover.xml",
        # identify unit tests from clover.xml and make tests.sh
        "python identify_tests.py",
        # make clover dir
        "mkdir -p clover",
        # run clover for single tests
        "bash tests.sh",
        # parse xml files to make data.json
        "python parse_data.py",
    ]
    n = len(commands)
    commands_echos = flatten(
        [(f'echo "[main][{i+1}/{n}] {s}"', s) for i, s in enumerate(commands)]
    )
    script_main = shebang + commands_echos
    write_list("main.sh", script_main)

    script_run = shebang + [
        # mkdir data if not exists, for log file
        "mkdir -p data",
        # run main.sh and log
        f"zsh main.sh 2>&1 | tee {logname}",
    ]
    write_list("run.sh", script_run)

    print("Done.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--idx", type=int, default=0)
    args = parser.parse_args()
    idx = args.idx
    main(idx)
