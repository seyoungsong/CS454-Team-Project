import json
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element


def pp(root: Element):
    for child in root:
        print(child.tag, child.attrib)


tree = ET.parse("clover.xml")
coverage = tree.getroot()
testproject = coverage[1]
package = testproject[1]
files = [e for e in package if e.tag == "file"]
data = {f.attrib["name"]: [e.attrib for e in f if e.tag == "line"] for f in files}

with open("clover.json", "w") as f:
    json.dump(data, f, indent=4, sort_keys=True)
