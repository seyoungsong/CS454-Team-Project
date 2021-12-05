import argparse
import csv
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


def read_csv(csv_file):
    with open(csv_file, "r", newline="", encoding="utf8") as f:
        reader = csv.reader(f)
        sloc = list(reader)
    return int(sloc[1][2])


def write_csv(filename: str, to_csv: list):

    keys = to_csv[0].keys()

    with open(filename, "w", newline="", encoding="utf8") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(to_csv)


def total_duration(d: dict):
    tm = sum([t["duration"] for t in d["data"] if "duration" in t])
    return tm


json_files = sorted(glob.glob("data/*.json"))
outputs = []
for json_file in json_files:
    stem = Path(json_file).stem
    sloc_file = f"sloc/{stem}.csv"
    sloc = read_csv(sloc_file)

    d = read_json(json_file)
    repo = d["info"]["github"]["repo"]
    num_test = len(d["data"])
    td = total_duration(d)

    # ID, Subjects, SLOC, TLOC, #Test, Time(s)
    out = {
        "ID": -1,
        "Subjects": repo,
        "SLOC": sloc,
        "#Test": num_test,
        "Time (s)": f"{td:.3f}",
    }
    outputs.append(out)

outputs.sort(key=lambda x: x["Subjects"])

for i, o in enumerate(outputs):
    o["ID"] = i + 1

write_csv("subjects_table.csv", outputs)
