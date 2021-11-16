import glob
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from pprint import pprint

tree = ET.parse("clover.xml")
root = tree.getroot()

float(
    [
        e.attrib["testduration"]
        for e in root.findall("./testproject/package/file/line")
        if "signature" in e.attrib
        and "testGenerateNameBasedUUIDNameSpaceAndName" in e.attrib["signature"]
    ][0]
)

coverage = {}
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
            coverage[file_name] = nums
