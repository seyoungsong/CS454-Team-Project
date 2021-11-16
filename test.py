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

filenames = glob.glob(f"{data_dir}/*.xml")

xml_file = filenames[0]


tree = ET.parse(xml_file)
root = tree.getroot()
project = root[0]
output = []
for package in project:
    files = [e for e in package if e.tag == "file"]
    for file in files:
        java_name = file.attrib["name"]
        lines = [e.attrib for e in file if e.tag == "line"]
        covered = []
        for line in lines:
            num = line["num"]
            if "count" in line and int(line["count"]) > 0:
                covered.append(num)
            if "truecount" in line and int(line["truecount"]) > 0:
                covered.append(f"{num}T")
            if "falsecount" in line and int(line["falsecount"]) > 0:
                covered.append(f"{num}F")
        if covered:
            output.append({java_name: covered})

pprint(output)
covered = output[0]["UUIDUtil.java"]
