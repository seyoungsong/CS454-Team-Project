import json
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element


def flatten(t):
    return [item for sublist in t for item in sublist]


def pp(root: Element):
    for child in root:
        print(child.tag, child.attrib)


tree = ET.parse("clover.xml")
coverage = tree.getroot()
testproject = coverage[1]
package = testproject[1]
files = [e for e in package if e.tag == "file"]
signatures = flatten(
    [
        [
            (f.attrib["name"].split(".java")[0], d["signature"].split("() : ")[0])
            for d in [e.attrib for e in f if e.tag == "line"]
            if "testsuccess" in d
        ]
        for f in files
    ]
)
cmds = [f"{test_class}#{method}" for test_class, method in signatures]
