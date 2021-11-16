import glob
import json
import xml.etree.ElementTree as ET
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
xml_file = xml_files[0]


tree = ET.parse(xml_file)
root = tree.getroot()
project = root[0]
code_coverage = {}
for package in project:
    files = [e for e in package if e.tag == "file"]
    for file in files:
        filename = file.attrib["name"]
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
            code_coverage[filename] = nums
