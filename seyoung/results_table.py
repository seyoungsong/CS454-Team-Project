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

import numpy as np


def read_json(filename: str):
    with open(filename, "r", encoding="utf8") as f:
        obj = json.load(f)
    return obj


def write_csv(filename: str, ll: list):
    with open(filename, "w", newline="", encoding="utf8") as f:
        writer = csv.writer(f)
        writer.writerows(ll)


def get_avg(data: dict):
    names = [
        "Sequential Test Prioritization",
        "Parallel Test Prioritization ($c=2$)",
        "Parallel Test Prioritization ($c=4$)",
        "Parallel Test Prioritization ($c=8$)",
        "Parallel Test Prioritization ($c=16$)",
        "Asymmetric Test Prioritization ($1:2$)",
        "Asymmetric Test Prioritization ($1:3$)",
        "Asymmetric Test Prioritization ($1:4$)",
        "Asymmetric Test Prioritization ($1:1:1:1:4:4:4:4$)",
    ]
    scenarios = [
        [1],
        [1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2],
        [1, 3],
        [1, 4],
        [1, 1, 1, 1, 4, 4, 4, 4],
    ]
    output = {
        str(scenarios[i]): {"name": names[i], "APSC_c": [], "avg": "-1"}
        for i in range(len(scenarios))
    }
    suite = data[0]
    for suite in data:
        results = suite["results"]
        result = results[0]
        for result in results:
            scenario = str(result["scenario"])
            APSC_c = result["APSC_c"]
            output[scenario]["APSC_c"].append(APSC_c)
    k = list(output.keys())[0]
    for k in output:
        m = np.mean(output[k]["APSC_c"])
        output[k]["avg"] = f"{m:.3f}"
        _ = output[k].pop("APSC_c", None)
    return np.array([[d["name"], d["avg"]] for d in output.values()])


def main():
    left_column = [
        "**Setting**",
        "Sequential",
        "Parallel ($c=2$)",
        "Parallel ($c=4$)",
        "Parallel ($c=8$)",
        "Parallel ($c=16$)",
        "Asymmetric ($1:2$)",
        "Asymmetric ($1:3$)",
        "Asymmetric ($1:4$)",
        "Asymmetric ($1:1:1:1:4:4:4:4$)",
    ]
    results = [
        {
            "algorithm": "**GA**",
            "file": "results/ga.json",
        },
        {
            "algorithm": "**SA**",
            "file": "results/sa.json",
        },
        {
            "algorithm": "**AGA**",  # cost-aware greedy additional technique
            "file": "results/caag.json",
        },
    ]
    lc = np.array(left_column)
    result = results[0]
    output = np.array(lc[:, None])
    for result in results:
        algo = result["algorithm"]
        data = read_json(result["file"])
        avg = get_avg(data)
        cc = np.array([algo] + list(avg[:, 1]))
        output = np.hstack([output, cc[:, None]])

    F = output[1:, 1:]
    line = F[0]
    for line in F:
        l = np.array([float(s) for s in line])
        max_idx = l.argmax()
        ss = line[max_idx]
        line[max_idx] = f"**{ss}**"

    write_csv("results_table.csv", output)


# https://www.convertcsv.com/csv-to-markdown.htm
if __name__ == "__main__":
    main()
