import glob
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from pprint import pprint

clover_xml_files = glob.glob(f"clover/*.xml")
clover_xml_files.sort()

coverage_by_test = {}
for clover_xml_file in clover_xml_files:
    test_name = Path(clover_xml_file).stem.replace("clover_", "")
    tree = ET.parse(clover_xml_file)
    root = tree.getroot()
    project = root[0]
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
    coverage_by_test[test_name] = coverage

with open("coverage_by_test.json", "w") as f:
    json.dump(coverage_by_test, f, indent=4, sort_keys=True)
