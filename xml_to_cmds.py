import json
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element


def flatten(t):
    return [item for sublist in t for item in sublist]


def pp(root: Element):
    for child in root:
        print(child.tag, child.attrib)


def main():
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

    cmds = [
        f"mvn clean clover:setup -Dtest={test_class}#{method} test clover:aggregate clover:clover && cp target/site/clover/clover.xml ./clover_by_test/clover_{test_class}_{method}.xml"
        for test_class, method in signatures
    ]

    with open("cmds.txt", "w") as f:
        f.write("\n".join(cmds))

    print("Done")


if __name__ == "__main__":
    main()
