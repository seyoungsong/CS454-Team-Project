import xml.etree.ElementTree as ET
from pathlib import Path
from pprint import pprint
from xml.etree.ElementTree import Element

# Structure of clover.xml
# coverage {'generated': '1637751772787', 'clover': '4.4.1'}
# project, testproject {'name': 'rome-parent', 'timestamp': '1637751765644'}
# metrics, package {'name': 'com.rometools.utils'}
# metrics, file {'path': '/Users/.../AlternativesTest.java', 'name': 'AlternativesTest.java'}
# metrics, class {'name': 'AlternativesTest'}, line {'complexity': '1', 'visibility': 'public', 'signature': 'testFirstNotNull() : void', 'num': '25', 'testsuccess': 'true', 'count': '1', 'testduration': '0.0', 'type': 'method'}


def write_list(filename: str, l: list[str]):
    with open(filename, "w", encoding="utf8") as f:
        for s in l:
            f.write(f"{s}\n")


def flatten(ll: list[list]) -> list:
    return [item for l in ll for item in l]


def ppe(root: Element):
    # pretty print XML element
    print(root.tag, root.attrib)
    for i, child in enumerate(root):
        print(f"{i}:", child.tag, child.attrib)


def ppl(es: list[Element]):
    # pretty print list of elements
    for i, e in enumerate(es):
        print(f"{i}:", e.tag, e.attrib)


def make_command(package: str, test_class: str, test_method: str, i: int, n: int):
    # Running a single method in a single test class
    # https://maven.apache.org/surefire/maven-surefire-plugin/examples/single-test.html
    test = f"{package}.{test_class}#{test_method}"
    name = f"clover#{package}#{test_class}#{test_method}"
    clover_xml = f"./clover/{name}.xml"
    log_file = f"./clover/{name}.log"

    cmd = f'echo "{i}/{n}: {test}" && mvn --file repo/pom.xml --fail-never --log-file {log_file} -Dmaven.clover.generateHtml=false -Dtest={test} clean clover:setup test clover:aggregate clover:clover && cp repo/target/site/clover/clover.xml {clover_xml}'
    return cmd


def identify_tests(clover_xml: str):
    tree = ET.parse(clover_xml)
    root = tree.getroot()

    unit_tests: list[dict[str, str]] = []

    _project, testproject = root
    testproject_name = testproject.attrib["name"]
    testproject_metrics = testproject.find("./metrics").attrib
    packages = testproject.findall("./package")

    # package = packages[0]
    for package in packages:
        package_name = package.attrib["name"]
        package_metrics = package.find("./metrics").attrib
        files = package.findall("./file")

        # file = files[0]
        for file in files:
            file_name = file.attrib["name"]
            class_name = Path(file_name).stem
            file_metrics = file.find("./metrics").attrib
            lines = file.findall("./line")
            methods = [
                e.attrib["signature"].split("() : ")[0]
                for e in lines
                if "testsuccess" in e.attrib
            ]
            tests = [
                {"package": package_name, "test_class": class_name, "test_method": s}
                for s in methods
            ]
            unit_tests += tests

    unit_tests.sort(
        key=lambda d: f'clover#{d["package"]}#{d["test_class"]}#{d["test_method"]}'
    )
    n = len(unit_tests)
    commands = [
        make_command(d["package"], d["test_class"], d["test_method"], i + 1, n)
        for i, d in enumerate(unit_tests)
    ]

    return commands


def main():
    # clover_xml is `clover.xml` file generated from the following commands:
    #   mvn --file repo/pom.xml clean clover:setup test clover:aggregate clover:clover --fail-never
    #   cp repo/target/site/clover/clover.xml ./clover.xml
    clover_xml = "clover.xml"

    commands = identify_tests(clover_xml)
    write_list("commands.sh", commands)

    print("Done.")


if __name__ == "__main__":
    main()
