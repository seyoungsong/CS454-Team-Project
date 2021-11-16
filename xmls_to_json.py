import glob
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from pprint import pprint

full_clover_xml = "clover.xml"
full_clover_root = ET.parse(full_clover_xml).getroot()
unit_clover_xmls = glob.glob(f"clover/*.xml")
unit_clover_xmls.sort()


data = []
for unit_clover_xml in unit_clover_xmls:
    unit_test_name = Path(unit_clover_xml).stem.replace("clover_", "")
    class_name, method_name = unit_test_name.split("_")

    tree = ET.parse(unit_clover_xml)
    root = tree.getroot()

    time_duration = max(
        [
            float(e.attrib["testduration"])
            for e in full_clover_root.findall("./testproject/package/file/line")
            if "testduration" in e.attrib
            and "signature" in e.attrib
            and method_name == e.attrib["signature"].split("() : ")[0]
        ]
    )

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
    data.append(
        {
            "name": unit_test_name,
            "time": time_duration,
            "coverage": code_coverage,
        }
    )

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
