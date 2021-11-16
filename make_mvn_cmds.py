import xml.etree.ElementTree as ET


def flatten(t):
    return [item for sublist in t for item in sublist]


def main():
    tree = ET.parse("clover/clover.xml")
    coverage = tree.getroot()
    testproject = coverage[1]
    package = testproject[1]
    files = [e for e in package if e.tag == "file"]
    test_list = flatten(
        [
            [
                (f.attrib["name"].split(".java")[0], d["signature"].split("() : ")[0])
                for d in [e.attrib for e in f if e.tag == "line"]
                if "testsuccess" in d
            ]
            for f in files
        ]
    )
    mvn_cmds = [
        f"mvn clean clover:setup -Dtest={class_name}#{method_name} test clover:aggregate clover:clover && cp target/site/clover/clover.xml ./clover_collection/clover_{class_name}_{method_name}.xml"
        for class_name, method_name in test_list
    ]
    mvn_cmds.sort()
    with open("mvn_cmds.sh", "w") as f:
        f.write("\n".join(mvn_cmds))
    print("Done")


if __name__ == "__main__":
    main()
