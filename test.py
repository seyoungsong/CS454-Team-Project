import glob
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from pprint import pprint
from xml.etree.ElementTree import Element


def flatten(t):
    return [item for sublist in t for item in sublist]


def pp(root: Element):
    for e in root:
        d = [e.tag, e.attrib]
        pprint(d)


data_dir = "clover_by_test"
xml_files = glob.glob(f"{data_dir}/*.xml")
xml_files.sort()


output = {}
for xml_file in xml_files:
    test_name = Path(xml_file).stem.replace("clover_", "")
    tree = ET.parse(xml_file)
    root = tree.getroot()
    project = root[0]
    code_coverage = {}
    for package in project:
        files = [e for e in package if e.tag == "file"]
        for file in files:
            file_name = file.attrib["name"]
            lines = [e.attrib for e in file if e.tag == "line"]
            nums = []
            for line in lines:
                num = line["num"]
                if "count" in line and int(line["count"]) > 0:
                    nums.append(num)
                if "truecount" in line and int(line["truecount"]) > 0:
                    nums.append(f"{num}T")
                if "falsecount" in line and int(line["falsecount"]) > 0:
                    nums.append(f"{num}F")
            if nums:
                nums.sort()
                code_coverage[file_name] = nums
    output[test_name] = code_coverage


with open("code_coverage_by_test.json", "w") as f:
    json.dump(output, f, indent=4)
